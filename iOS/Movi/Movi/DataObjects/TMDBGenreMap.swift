//
//  TMDBGenreMap.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/7/23.
//

import Foundation

class TMDBGenreMap: ObservableObject {
    static var genreMap = [28: "Action",
                               12: "Adventure",
                               16: "Animation",
                               35: "Comedy",
                               80: "Crime",
                               99: "Documentary",
                               18: "Drama",
                               10751: "Family",
                               14: "Fantasy",
                               36: "History",
                               27: "Horror",
                               10402: "Music",
                               9648: "Mystery",
                               10749: "Romance",
                               878: "Science Fiction",
                               10770: "TV Movie",
                               53: "Thriller",
                               10752: "War",
                               37: "Western"]
    
    class func value(forGenreId: Int) -> String {
        return genreMap[forGenreId] ?? "Speculative Fiction"
    }
}
