//
//  CreateProfilePage.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/30/23.
//
import SwiftUI

struct CreateProfilePage: View {
    @State private var Username: String = ""
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack(alignment: .leading){
                    ZStack{
                        VStack(alignment: .leading){
                            Text("4/4")
                                .opacity(0.4)
                            Text("Create your profile")
                                .textInputAutocapitalization(.words)
                                .font(.largeTitle)
                                .fontWeight(.bold)
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding(20)
                        .offset(y:120)
                        
                        
                    }
                    
                    Form {
                        Section(/*header: (Text("Username").font(.system(size: 16)).fontWeight(.semibold) + Text("*").foregroundColor(.red))*/) {
                            ZStack (alignment: .leading){
                                if Username.isEmpty {
                                    (Text("Enter username") + Text("*").foregroundColor(.red))
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                
                                TextField("", text: $Username)
                                    .frame(height: 40)
                                    .overlay(RoundedRectangle(cornerRadius: 8.0).strokeBorder(Color.white, style: StrokeStyle(lineWidth: 1.0)).frame(width: 350, height: 60))
                            }
                            .listRowBackground(Color(hex: 0x141D26))
                            
                        }
//                        .headerProminence(.increased)
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
                                    .background(isUsernameValid() ? Color(hex: 0xF04650) : .gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                                    
                            }
                            .frame(maxWidth: .infinity, alignment: .center)
                            .simultaneousGesture(TapGesture().onEnded{
                                submitUsernameHandler()
                            })
                            .disabled(!isUsernameValid())
                        
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
    
    private func isUsernameValid() -> Bool {
        return !Username.isEmpty
        // add db checks for db stuff here
    }
    
    private func submitUsernameHandler(){
        print("Username: \(Username) is valid!")
    }
}

struct CreateProfilePage_Previews: PreviewProvider {
    static var previews: some View {
        CreateProfilePage()
    }
}
