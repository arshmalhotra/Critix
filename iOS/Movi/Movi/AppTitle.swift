import SwiftUI

// set app colors to environment colors
extension Color {
    init(hex: UInt) {
        let red = Double((hex >> 16) & 0xFF) / 255.0
        let green = Double((hex >> 8) & 0xFF) / 255.0
        let blue = Double(hex & 0xFF) / 255.0
        self.init(red: red, green: green, blue: blue)
    }
}

struct AppTitle: View {
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                Image("Spotlight")
                    .resizable()
                    .aspectRatio(contentMode: /*@START_MENU_TOKEN@*/.fit/*@END_MENU_TOKEN@*/)
                    .edgesIgnoringSafeArea(.top)
                    .position(x: UIScreen.main.bounds.width / 2, y: 100)
                // maybe change offset amounts to .position and use UIscreen bounds like ^
                VStack{
                    Image("Clapper")
                        .resizable()
                        .aspectRatio(contentMode: /*@START_MENU_TOKEN@*/.fit/*@END_MENU_TOKEN@*/)
                        .padding(.all, 50.0)
                        .offset(x: 0, y: -100)
                    Text("Critix")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(Color.white)
                        .multilineTextAlignment(.center)
                        .offset(x:0, y: -110)
                    
                    
                    NavigationLink {
                            EmailPage()
                        } label: {
                            Text("Create Account")
                                .frame(width: 350, height: 60)
                                .background(Color(hex: 0xF04650))
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                
                        }
                        .offset(y:-100)
              
                        
                    NavigationLink {
                            SignUp()
                        } label: {
                            Text("I already have an account")
                                .frame(width: 350, height: 60)
                                .background(Color(hex: 0x141D26))
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .overlay(
                                    RoundedRectangle(cornerRadius: 10)
                                        .stroke(Color.white, lineWidth: 1)
                                )
                        }
                        .offset(y:-100)
                    
                }
            }
        }
        .navigationTitle("Main View")

        
    }
}

struct CustomBackButton: View {
    @Environment(\.presentationMode) var presentationMode

    var body: some View {
        Button(action: {
            self.presentationMode.wrappedValue.dismiss()
        }) {
            Image(systemName: "chevron.backward")
                .imageScale(.large)
                .foregroundColor(.white)
                
        }
    }
}

struct AppTitle_Previews: PreviewProvider {
    static var previews: some View {
        AppTitle()
    }
}
