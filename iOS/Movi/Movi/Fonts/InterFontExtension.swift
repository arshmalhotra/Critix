//
//  InterFontTypes.swift
//  Movi
//
//  Created by Arsh Malhotra on 10/10/23.
//

import Foundation
import SwiftUI

extension Font {
    enum InterWeight {
        case regular
        case medium
        case semibold
        case bold
        
        var associatedFont: String {
            switch self {
            case .regular:
                return "Inter-Regular"
            case .medium:
                return "Inter-Medium"
            case .semibold:
                return "Inter-SemiBold"
            case .bold:
                return "Inter-Bold"
            }
        }
    }
    
    static func inter(_ weight: InterWeight = .regular, size: CGFloat = 16) -> Font {
        return .custom(weight.associatedFont, size: size)
    }
}
