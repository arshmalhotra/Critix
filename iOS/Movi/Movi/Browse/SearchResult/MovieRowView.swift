//
//  SearchResultRowView.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/7/23.
//

import SwiftUI

struct MovieRowView: View {
    let searchResultRowVM: MovieRowViewModel
    
    var imageHeight: CGFloat = 100
    var imageWidth: CGFloat = 75
    
    init(searchResultRowVM: MovieRowViewModel) {
        self.searchResultRowVM = searchResultRowVM
        self.imageHeight = (searchResultRowVM.genres != nil ? 150 : 100)
        self.imageWidth = self.imageHeight * 3 / 4
    }
    
    var body: some View {
        HStack(alignment: .top, spacing: 10) {
            AsyncImage(url: URL(string: searchResultRowVM.posterURL)) { phase in
                switch phase {
                case .empty:
                    self.imageBackgroundRectangle()
                case .success(let image):
                    image.resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(maxWidth: self.imageWidth, maxHeight: self.imageHeight)
                case .failure:
                    self.imageBackgroundRectangle()
                @unknown default:
                    self.imageBackgroundRectangle()
                }
            }
            VStack(alignment: .leading) {
                Text(searchResultRowVM.title)
                    .foregroundColor(SystemColors.primaryColor)
                    .font(.system(size: 18))
                    .fontWeight(.semibold)
                HStack {
                    if searchResultRowVM.releaseYear != nil {
                        Text(searchResultRowVM.releaseYear)
                    }
                    if searchResultRowVM.mpaRating != nil {
                        Text("·")
                            .fontWeight(.black)
                        Text(searchResultRowVM.mpaRating)
                    }
                    if searchResultRowVM.runtime != nil {
                        Text("·")
                            .fontWeight(.black)
                        Text(searchResultRowVM.runtime)
                    }
                }
                .foregroundColor(SystemColors.secondaryColor)
                if searchResultRowVM.genres != nil {
                    GenresView(genres: searchResultRowVM.genres)
                }
            }
        }
        .padding(.horizontal, 10)
        .padding(.vertical, 5)
    }
    
    private func imageBackgroundRectangle() -> some View {
        return Rectangle()
            .background(SystemColors.imageBackgroundColor)
            .foregroundColor(SystemColors.imageBackgroundColor)
            .frame(width: self.imageWidth, height: self.imageHeight)
    }
}

struct SearchResultRowView_Previews: PreviewProvider {
    static var previews: some View {
//        MovieRowView(searchResultRowVM: .constant(MovieRowViewModel(fromTDMBSearch: ["id": 346698,
//                                                                                     "poster_path": "/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
//                                                                                     "release_date": "2023-07-19",
//                                                                                     "title": "Barbie"])!))
        MovieRowView(searchResultRowVM: MovieRowViewModel(fromTDMBSearch: ["id": 9023,
                                                                           "poster_path": "/cUgYrz4twiJ3QgVGpRfey984NIB.jpg",
                                                                           "release_date": "2002-05-24",
                                                                           "title": "Spirit: Stallion of the Cimarron"])!)
        .frame(width: 393, alignment: .leading)
        .background(SystemColors.backgroundColor)
    }
}
