//
//  SignUp.swift
//  Movi
//
//  Created by Preetham Ramesh on 9/25/23.
//

import SwiftUI

// create a struct for a form?

struct SignUp: View {
    @State var Name: String = ""
    @State var Email: String = ""
    @State var Pwd: String = ""

    
    var body: some View {
        // here bc text is blue if directly in TextField
        let EmailPrompt: String = "example@gmail.com"
        
        
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                VStack (alignment: .leading){
                    Text("Sign Up")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding()
                        .foregroundColor(Color.white)
                        .multilineTextAlignment(.leading)
                    
                    Form {
                        Section(header: Text("Name").font(.system(size: 16)).fontWeight(.semibold) + Text("*").foregroundColor(.red)) {
                            ZStack (alignment: .leading){
                                if Name.isEmpty {
                                    Text("Enter your name") //placeholder text
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                TextField("", text: $Name)
                                    .frame(height: 40)
                                    .textInputAutocapitalization(.words)
                                    .overlay(RoundedRectangle(cornerRadius: 8.0).strokeBorder(Color.white, style: StrokeStyle(lineWidth: 1.0)).frame(width: 350, height: 60))
                            }
                            .listRowBackground(Color(hex: 0x141D26))
                        }
                        .textCase(nil) // remove all caps for input field titles
                        
                        Section(header: Text("Email").font(.system(size: 16)).fontWeight(.semibold) + Text("*").foregroundColor(.red)) {
                            ZStack (alignment: .leading){
                                if Email.isEmpty {
                                    Text(EmailPrompt)
                                        .foregroundColor(.white.opacity(0.4))
                                        .font(.system(size: 15))
                                }
                                TextField("", text: $Email)
                                    .frame(height: 40)
                                    .textInputAutocapitalization(.never)
                                    .overlay(RoundedRectangle(cornerRadius: 8.0).strokeBorder(Color.white, style: StrokeStyle(lineWidth: 1.0)).frame(width: 350, height: 60))
                            }
                            .listRowBackground(Color(hex: 0x141D26))
                            
                        }
                        .textCase(nil)
                        
                        
                        Section(header: Text("Create a password").font(.system(size: 16)).fontWeight(.semibold) + Text("*").foregroundColor(.red)) {
                            ZStack(alignment: .leading){
                                if Pwd.isEmpty {
                                    Text("At least 8 characters")
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
                    .background(Color(hex: 0x141D26))
                    .scrollContentBackground(.hidden)
                    .tint(Color(hex: 0xF04650))
                    
                    VStack{
                        NavigationLink {
                                Template()
                            } label: {
                                Text("Create Account")
                                    .frame(width: 350, height: 60)
                                    .background(isValid() ? Color(hex: 0xF04650) : .gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(4)
                                    
                            }
                            .frame(maxWidth: .infinity, alignment: .center)
                            .simultaneousGesture(TapGesture().onEnded{
                                createHandler()
                            })
                            .disabled(!isValid())
                        
                        HStack{
                            Text("Already have an account?")
                            NavigationLink {
                                Template()
                            } label: {
                                Text("Log in")
                                    .fontWeight(.bold)
                            }
                            
                        }
                        
                    }.padding(.bottom, 170)
                   
                    Spacer()
                }
            }
//            .navigationBarTitle("Sign Up")
            .foregroundColor(Color.white)
        }
        .navigationBarBackButtonHidden(true) // Hide the default back button
        .navigationBarItems(leading: CustomBackButton())
    }
    
    private func isValid() -> Bool {
        return !Name.isEmpty && validateEmail() && (Pwd.count >= 8)
    }
    
    private func validateEmail() -> Bool {
        if !Email.isEmpty{
            let emailRegex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"
            let emailPredicate = NSPredicate(format: "SELF MATCHES %@", emailRegex)
            return emailPredicate.evaluate(with: Email)
        }
        return false
    }
    
    private func createHandler() {
        print("Name: \(Name), Email: \(Email), Pasword: \(Pwd)")
    }
    
}

struct SignUp_Previews: PreviewProvider {
    static var previews: some View {
        SignUp()
    }
}
