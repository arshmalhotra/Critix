//
//  BrowseView.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/4/23.
//

import SwiftUI

struct BrowseView: View {
    @State private var searchResults: Array<MovieRowViewModel> = []
    
    var body: some View {
        VStack {
            SearchBarView(searchResults: $searchResults)
            ScrollView {
                VStack {
                    ForEach(searchResults) { movie in
                        MovieRowView(searchResultRowVM: movie)
                            .frame(maxWidth: .infinity, alignment: .leading)
                    }
                }
            }
        }
        .frame(maxHeight: .infinity, alignment: .top)
    }
}

struct BrowseView_Previews: PreviewProvider {
    static var previews: some View {
        BrowseView()
            .background(SystemColors.backgroundColor)
    }
}
