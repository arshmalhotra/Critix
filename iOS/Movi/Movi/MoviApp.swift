//
//  MoviApp.swift
//  Movi
//
//  Created by Arsh Malhotra on 8/22/23.
//

import SwiftUI

@main
struct MoviApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            BrowseView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
                .background(SystemColors.backgroundColor)
        }
    }
}
