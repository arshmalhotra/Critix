//
//  SearchBarViewModel.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/6/23.
//

import Foundation
import Combine

class SearchBarViewModel: ObservableObject {
    @Published var debouncedText = ""
    @Published var searchText = ""
    
    private var subscriptions = Set<AnyCancellable>()
    
    init() {
        $searchText
            .debounce(for: .seconds(1), scheduler: DispatchQueue.main)
            .sink { [weak self] dt in
                self?.debouncedText = dt
            }
            .store(in: &subscriptions)
    }
}
