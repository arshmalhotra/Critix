//
//  Template.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/27/23.
//

import SwiftUI

struct Template: View {
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack{
                    Text("template")
                }
            }
            .navigationBarTitle("Template")
            .foregroundColor(Color.white)
        }
        .navigationBarBackButtonHidden(true) // Hide the default back button
        .navigationBarItems(leading: CustomBackButton())
    }
}

struct Template_Previews: PreviewProvider {
    static var previews: some View {
        Template()
    }
}
