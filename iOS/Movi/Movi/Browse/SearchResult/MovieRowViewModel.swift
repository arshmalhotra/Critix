//
//  SearchResultRowViewModel.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/7/23.
//

import Foundation

class MovieRowViewModel: ObservableObject, Identifiable {
    var id: String!
    var posterURL: String!
    var backdropURL: String!
    var title: String!
    var releaseYear: String!
    var mpaRating: String!
    var runtime: String!
    var genres: [String]!
    
    init?(fromOMDB movieJSON: Dictionary<String, Any>) {
        guard let id = movieJSON["imdbID"] as? String,
              let title = movieJSON["Title"] as? String,
              let year = movieJSON["Year"] as? String,
              let poster = movieJSON["Poster"] as? String else {
            return nil
        }
        
        self.id = id
        self.title = title
        self.releaseYear = year
        self.posterURL = poster
        
    }
    
    init?(fromTDMBSearch movieJSON: Dictionary<String, Any>) {
        guard let id = movieJSON["id"] as? Int,
              let title = movieJSON["title"] as? String,
              let pURL = createTmdbURL(withPath: movieJSON["poster_path"] as? String),
              let releaseDate = movieJSON["release_date"] as? String else {
            return nil
        }
        
        self.id = String(id)
        self.title = title
        self.posterURL = pURL
        self.releaseYear = String(releaseDate.prefix(4))
        
        if let bURL = createTmdbURL(withPath: movieJSON["backdrop_path"] as? String) {
            self.backdropURL = bURL
        }
    }
    
    private func createTmdbURL(withPath: String?) -> String? {
        if let path = withPath {
            return "https://image.tmdb.org/t/p/original/\(path)"
        }
        return nil
    }
}
