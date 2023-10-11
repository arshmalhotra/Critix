//
//  MockMovieDetailsModel.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/11/23.
//

import Foundation

enum MockMovieDetailsModel {
        case SpiritedAway(_ detailLevel: DetailLevel = .search)
        case Barbie(_ detailLevel: DetailLevel = .search)
        case Oppenheimer(_ detailLevel: DetailLevel = .search)
        
        enum DetailLevel {
            case search
            case full
        }
        
    var detailModel: MovieDetailsModel {
        switch self {
        case .SpiritedAway(let detailLevel):
            let dummyData = MovieDetailsModel(fromTDMBSearch: ["id": 129,
                                                               "backdrop_path": "/Ab8mkHmkYADjU7wQiOkia9BzGvS.jpg",
                                                               "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
                                                               "release_date": "2001-07-20",
                                                               "title": "Spirited Away"])
            if detailLevel == .full {
                _ = dummyData!.append(fromOMDB: ["Rated":"PG",
                                                 "Runtime":"125 min",
                                                 "Genre":"Animation, Adventure, Family",
                                                 "Director":"Hayao Miyazaki",
                                                 "Writer":"Hayao Miyazaki",
                                                 "Actors":"Daveigh Chase, Suzanne Pleshette, Miyu Irino",
                                                 "Plot":"During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches and spirits, a world where humans are changed into beasts.",
                                                 "imdbID":"tt0245429"])
            }
            return dummyData!
        case .Barbie(let detailLevel):
            let dummyData = MovieDetailsModel(fromTDMBSearch: ["id": 346698,
                                                               "backdrop_path": "/ctMserH8g2SeOAnCw5gFjdQF8mo.jpg",
                                                               "poster_path": "/iuFNMS8U5cb6xfzi51Dbkovj7vM.jpg",
                                                               "release_date": "2023-07-19",
                                                               "title": "Barbie"])
            if detailLevel == .full {
                _ = dummyData!.append(fromOMDB: ["Rated":"PG-13",
                                                 "Runtime":"114 min",
                                                 "Genre":"Adventure, Comedy, Fantasy",
                                                 "Director":"Greta Gerwig",
                                                 "Writer":"Greta Gerwig, Noah Baumbach",
                                                 "Actors":"Margot Robbie, Ryan Gosling, Issa Rae",
                                                 "Plot":"Barbie suffers a crisis that leads her to question her world and her existence.",
                                                 "imdbID":"tt1517268"])
            }
            return dummyData!
        case .Oppenheimer(let detailLevel):
            let dummyData = MovieDetailsModel(fromTDMBSearch: ["id": 872585,
                                                               "backdrop_path": "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
                                                               "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
                                                               "release_date": "2023-07-19",
                                                               "title": "Oppenheimer"])
            if detailLevel == .full {
                _ = dummyData!.append(fromOMDB: ["Rated":"R",
                                                 "Runtime":"180 min",
                                                 "Genre":"Biography, Drama, History",
                                                 "Director":"Christopher Nolan",
                                                 "Writer":"Christopher Nolan, Kai Bird, Martin Sherwin",
                                                 "Actors":"Cillian Murphy, Emily Blunt, Matt Damon",
                                                 "Plot":"The story of American scientist, J. Robert Oppenheimer, and his role in the development of the atomic bomb.",
                                                 "imdbID":"tt15398776"])
            }
            return dummyData!
        }
    }
}
