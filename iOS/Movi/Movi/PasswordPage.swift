//
//  PasswordPage.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/29/23.
//

import SwiftUI

struct PasswordPage: View {
    @State private var Pwd: String = ""
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack(alignment: .leading){
                    ZStack{
                        VStack(alignment: .leading){
                            Text("2/4")
                                .opacity(0.4)
                            Text("Create a password")
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
                                if Pwd.isEmpty {
                                    Text("Enter password")
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                
                                SecureField("", text: $Pwd)
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
                    
                    VStack(alignment: .leading, spacing: 3){
                        HStack{
                            Image(systemName: "checkmark")
                            Text("At least 8 characters")
                                
                        }.foregroundColor(isPwdLong() ? .green.opacity(0.8) : .white.opacity(0.4))
                        HStack{
                            Image(systemName: "checkmark")
                            Text("Includes capital letter(s)")
                                
                        }.foregroundColor(hasCapLetter() ? .green.opacity(0.8) : .white.opacity(0.4))
                        HStack{
                            Image(systemName: "checkmark")
                            Text("Includes number(s)")
                                
                                
                        }.foregroundColor(hasNum() ? .green.opacity(0.8) : .white.opacity(0.4))
                        
                    }
                    .font(.system(size: 13))
                    .padding(24)
                    .offset(y:-95)
                    
                    
                    
                    VStack{
                        NavigationLink {
                                NamePage()
                            } label: {
                                Text("Next")
                                    .fontWeight(.bold)
                                    .frame(width: 350, height: 60)
                                    .background(isPwdValid() ? Color(hex: 0xF04650) : .gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                                    
                            }
                            .frame(maxWidth: .infinity, alignment: .center)
                            .simultaneousGesture(TapGesture().onEnded{
                                submitPwdHandler()
                            })
                            .disabled(!isPwdValid())
                        
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
    
    private func isPwdLong() -> Bool {
        return Pwd.count >= 8
    }
    
    private func hasNum() -> Bool {
        let numRange = Pwd.rangeOfCharacter(from: .decimalDigits)
        return numRange != nil
    }
    
    private func hasCapLetter() -> Bool {
        for char in Pwd {
            if char.isUppercase {
                return true
            }
        }
        return false
    }
    
    private func isPwdValid() -> Bool {
        return isPwdLong() && hasNum() && hasCapLetter()
    }
    
    private func submitPwdHandler(){
        print("Email: \(Pwd) is valid!")
    }
}

struct PasswordPage_Previews: PreviewProvider {
    static var previews: some View {
        PasswordPage()
    }
}
