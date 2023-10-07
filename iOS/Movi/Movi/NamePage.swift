//
//  NamePage.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/30/23.
//

import SwiftUI

struct NamePage: View {
    @State private var Name: String = ""
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack(alignment: .leading){
                    ZStack{
                        VStack(alignment: .leading){
                            Text("3/4")
                                .opacity(0.4)
                            Text("What's your name?")
                                .textInputAutocapitalization(.words)
                                .font(.largeTitle)
                                .fontWeight(.bold)
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(20)
                        .offset(y:120)
                        
                        
                    }
                    
                    Form {
                        Section {
                            ZStack (alignment: .leading){
                                if Name.isEmpty {
                                    Text("John Doe")
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                
                                TextField("", text: $Name)
                                    .textInputAutocapitalization(.words)
                                    .disableAutocorrection(true)
                                    .frame(height: 40)
                                    .overlay(RoundedRectangle(cornerRadius: 8.0).strokeBorder(Color.white, style: StrokeStyle(lineWidth: 1.0)).frame(width: 350, height: 60))
                            }
                            .listRowBackground(Color(hex: 0x141D26))
                            
                        }
                        .textCase(nil)
                    }
                    .background(Color.clear)
                    .scrollContentBackground(.hidden)
                    .tint(Color(hex: 0xF04650))
                    .offset(y:80)
                    
                    
                    VStack{
                        NavigationLink {
                                Template()
                            } label: {
                                Text("Next")
                                    .fontWeight(.bold)
                                    .frame(width: 350, height: 60)
                                    .background(isNameValid() ? Color(hex: 0xF04650) : .gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                                    
                            }
                            .frame(maxWidth: .infinity, alignment: .center)
                            .simultaneousGesture(TapGesture().onEnded{
                                submitNameHandler()
                            })
                            .disabled(!isNameValid())
                        
                        Spacer()
                    }
                    .offset(y:-100)
                    
                }
            }
            .foregroundColor(Color.white)
        }
        .navigationBarBackButtonHidden(true) // Hide the default back button
        .navigationBarItems(leading: CustomBackButton())
    }
    
    private func isNameValid() -> Bool {
        return !Name.isEmpty
    }
    
    private func submitNameHandler(){
        print("Name: \(Name) is valid!")
    }
}

struct NamePage_Previews: PreviewProvider {
    static var previews: some View {
        NamePage()
    }
}
