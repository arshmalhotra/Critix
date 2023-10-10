//
//  SearchBarView.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/6/23.
//

import SwiftUI

struct SearchBarView: View {
    @Binding var searchResults: [MovieRowViewModel]
    
    @StateObject private var movieSearchVM = SearchBarViewModel()
    @FocusState private var searchIsFocused: Bool
    @State private var showCancelButton = false
    
    var body: some View {
        HStack {
            HStack {
                Image(systemName: "magnifyingglass")
                    .foregroundColor((searchIsFocused ? SystemColors.primaryColor : SystemColors.secondaryColor))
                TextField("", text: $movieSearchVM.searchText)
//                    .onReceive(movieSearchVM.$debouncedText) { (dt) in
//                        debouncedSearchText = dt
//                    }
                    .focused($searchIsFocused)
                    .frame(height: 50)
                    .foregroundColor(SystemColors.primaryColor)
                    .background {
                        ZStack {
                            if movieSearchVM.searchText == "" {
                                HStack {
                                    Text("Search for a movie")
                                        .foregroundColor(SystemColors.secondaryColor)
                                    Spacer()
                                }
                                .frame(maxWidth: .infinity)
                            }
                        }
                    }
                
                if movieSearchVM.searchText != "" {
                    Button(action: {
                        movieSearchVM.searchText = ""
                    }) {
                        Image(systemName: "multiply.circle.fill")
                            .foregroundColor(SystemColors.secondaryColor)
                    }
                    .transition(.opacity)
                }
            }
            .onChange(of: searchIsFocused) { bool in
                withAnimation(.easeInOut(duration: 0.2)) {
                    showCancelButton = bool
                }
            }
            .padding(.horizontal)
            .background(SystemColors.backgroundColor)
            .cornerRadius(5)
            .overlay(
                RoundedRectangle(cornerRadius: 5)
                    .stroke(
                        (searchIsFocused ? SystemColors.primaryColor : SystemColors.secondaryColor),
                        lineWidth: 1))

            if showCancelButton {
                Button("Cancel") {
                    movieSearchVM.searchText = ""
                    searchIsFocused = false
                }
                .foregroundColor(SystemColors.primaryColor)
                .transition(.move(edge: .trailing))
            }
        }
        .onChange(of: movieSearchVM.searchText, perform: { searchValue in
            if searchValue.isEmpty {
                searchResults = []
            }
        })
        .onChange(of: movieSearchVM.debouncedText, perform: queryTMDBSearch)
        .padding(.horizontal, 10)
    }
    
    private func queryTMDBSearch(queryString: String) -> Void {
        if queryString.isEmpty {
            searchResults = []
            return
        }
        let headers = ["accept": "application/json",
                       "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOGZmNjNlZDgwOWQ4OTU3ZDBjY2E4YmE4YTU5YzU4NCIsInN1YiI6IjY0ZjZkYjkzYThiMmNhMDEzODRhNzQ1OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ynGTfr0GBqlv38DsKPbrBOQayUsAUoBM-Y6-85D2y4A"]
        
        /**
         * TODO: Move the apikey out of the file
         * TODO: Make a server call instead which then calls the OMDB API
         */
//        let apiKey = "a036a667"
        
        let escapedQuery = queryString.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)

        let request = NSMutableURLRequest(
            url: NSURL(string: "https://api.themoviedb.org/3/search/movie?query=\(escapedQuery!)&include_adult=false&language=en-US&page=1")! as URL,
            cachePolicy: .useProtocolCachePolicy,
            timeoutInterval: 10.0)
        request.httpMethod = "GET"
        request.allHTTPHeaderFields = headers

        let session = URLSession.shared
        let dataTask = session.dataTask(with: request as URLRequest) { (data, response, error) -> Void in
            if let error = error {
                fatalError("Error getting response from TMDB. \(error as Any)")
                return
            }
            guard let httpResponse = response as? HTTPURLResponse,
                  (200...299).contains(httpResponse.statusCode) else {
                fatalError("Status code error. \(String(describing: response as? HTTPURLResponse))")
                return
            }
            guard let mimeType = httpResponse.mimeType, mimeType == "application/json",
               let data = data else {
                fatalError("Could not process data. \(String(describing: data))")
                return
            }
            do {
                let dataDict = try JSONSerialization.jsonObject(with: data) as? [String: Any]
                if let results = dataDict?["results"] as? Array<Dictionary<String, Any>> {
                    searchResults = results.compactMap({ resultDict in
                        MovieRowViewModel(fromTDMBSearch: resultDict)
                    })
                }
            } catch {
                fatalError("Could not serialize JSON from data. \(String(describing: data))")
                return
            }
        }

        dataTask.resume()
    }
}

struct SearchBarView_Previews: PreviewProvider {
    static var previews: some View {
        SearchBarView(searchResults: .constant([]))
    }
}
