//
//  GenreTileView.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/7/23.
//

import SwiftUI

struct GenreTagView: View {
    var genre: String
    
    var body: some View {
        Text(genre)
            .foregroundColor(SystemColors.primaryColor)
            .fontWeight(.medium)
            .padding(.horizontal, 10)
            .padding(.vertical, 8)
            .cornerRadius(5)
            .overlay(RoundedRectangle(cornerRadius: 5).stroke(SystemColors.secondaryColor, lineWidth: 2))
    }
}

struct GenreTileView_Previews: PreviewProvider {
    static var previews: some View {
        GenreTagView(genre: "Comedy")
            .background(SystemColors.backgroundColor)
    }
}
