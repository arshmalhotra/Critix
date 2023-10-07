import SwiftUI

struct GrowingButton: ButtonStyle {
    let backgroundColor: Color
    let borderWidth: CGFloat

    init(backgroundColor: Color, borderWidth: CGFloat) {
        self.backgroundColor = backgroundColor
        self.borderWidth = borderWidth
    }

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .frame(width: 350)
            .background(backgroundColor)
            .overlay(RoundedRectangle(cornerRadius: 5)
                        .stroke(Color.white, lineWidth: borderWidth)
                    )
            .foregroundStyle(.white)
            .clipShape(RoundedRectangle(cornerSize: CGSize(width: 5, height: 10)))
            .scaleEffect(configuration.isPressed ? 1.2 : 1)
            .animation(.easeOut(duration: 0.2), value: configuration.isPressed)
    }
}

//extension Color {
//    init(hex: UInt) {
//        let red = Double((hex >> 16) & 0xFF) / 255.0
//        let green = Double((hex >> 8) & 0xFF) / 255.0
//        let blue = Double(hex & 0xFF) / 255.0
//        self.init(red: red, green: green, blue: blue)
//    }
//}

struct App_Title: View {
    var body: some View {
        NavigationStack{
            ZStack{
                Color(hex: 0x141D26)
                    .ignoresSafeArea()
                Image("Spotlight")
                    .resizable()
                    .aspectRatio(contentMode: /*@START_MENU_TOKEN@*/.fit/*@END_MENU_TOKEN@*/)
                    .edgesIgnoringSafeArea(.top)
                    .position(x: UIScreen.main.bounds.width / 2, y: 60)
                // maybe change offset amounts to .position and use UIscreen bounds like ^
                VStack{
                    Image("Home_logo")
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
                    
                    NavigationLink(destination: SignUp(), label: {
                        Button("Create Account"){}
                        .buttonStyle(GrowingButton(backgroundColor: Color(hex: 0xF04650), borderWidth:  CGFloat(0)))
                        .position(x:50, y:100)
                        .background(.blue)
                    })
                        
                        
                    

                    NavigationLink(destination: SignUp()){
                        Button("I already have an account") {
                        }
                        .buttonStyle(GrowingButton(backgroundColor: Color(hex: 0x141D26), borderWidth:  CGFloat(1)))
//                        .offset(x:0, y: -90)
                        .background(.green)
                    }
                }
            }
            
        }
        .navigationTitle("Main View")
        
    }
}

struct App_Title_Previews: PreviewProvider {
    static var previews: some View {
        App_Title()
    }
}
