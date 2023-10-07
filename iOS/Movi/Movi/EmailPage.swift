//
//  EmailPage.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/29/23.
//

import SwiftUI

struct EmailPage: View {
    @State var Email: String = ""
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack(alignment: .leading){
                    ZStack{
                        VStack(alignment: .leading){
                            Text("1/4")
                                .opacity(0.4)
                            Text("Enter your email")
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
                                if Email.isEmpty {
                                    Text("Your email address")
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                
                                if Email.count > 0 && !isEmailValid(){
                                    Image(systemName: "xmark")
                                        .font(.system(size: 22))
                                        .frame(maxWidth: .infinity, alignment: .trailing)
                                        .foregroundColor(.red)
                                } else if isEmailValid() {
                                    Image(systemName: "checkmark")
                                        .font(.system(size: 22))
                                        .frame(maxWidth: .infinity, alignment: .trailing)
                                        .foregroundColor(.green)
                                }
                                
                                TextField("", text: $Email)
                                    .frame(height: 40)
                                    .textInputAutocapitalization(.never)
                                    .overlay(RoundedRectangle(cornerRadius: 10.0).strokeBorder(Color.white, style: StrokeStyle(lineWidth: 1.0)).frame(width: 350, height: 60))
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
                                PasswordPage()
                            } label: {
                                Text("Next")
                                    .fontWeight(.bold)
                                    .frame(width: 350, height: 60)
                                    .background(isEmailValid() ? Color(hex: 0xF04650) : .gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                                    
                            }
                            .frame(maxWidth: .infinity, alignment: .center)
                            .simultaneousGesture(TapGesture().onEnded{
                                submitEmailHandler()
                            })
                            .disabled(!isEmailValid())
                        
                        HStack{
                            Text("Already have an account?")
                                .font(.system(size: 14))
                            NavigationLink {
                                Template()
                            } label: {
                                Text("Log in")
                                    .font(.system(size: 14))
                                    .fontWeight(.bold)
                            }
                            
                        }
                        .padding(10)
                        Spacer()
                    }
                    .offset(y:-120)
                    
                }
                
                
                
            }
//            .navigationBarTitle("Template")
            .foregroundColor(Color.white)
        }
        .navigationBarBackButtonHidden(true) // Hide the default back button
        .navigationBarItems(leading: CustomBackButton())
    }
    private func isEmailValid() -> Bool {
        if !Email.isEmpty{
            let emailRegex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"
            let emailPredicate = NSPredicate(format: "SELF MATCHES %@", emailRegex)
            return emailPredicate.evaluate(with: Email)
        }
        return false
    }
    
    private func submitEmailHandler(){
        print("Email: \(Email) is valid!")
    }
}

struct EmailPage_Previews: PreviewProvider {
    static var previews: some View {
        EmailPage()
    }
}

