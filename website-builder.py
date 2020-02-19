import os

LogoUrl = input('logo url: ')
ButtonUrl = input('button url: ')

Color = input('highlight color code: ')
Name = input('company name: ')

Img1 = input('image 1 url: ')
Img2 = input('image 2 url: ')
Img3 = input('image 3 url: ')
Img4 = input('image 4 url: ')

Meta = '''<title>''' + Name + '''</title>
<link href="https://fonts.googleapis.com/css?family=Roboto:400,500,700,900&display=swap" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1.0">'''

Style = '''<style>body { background-color: #fff; text-align: left; } 
h1 { font-family: "Roboto", sans-serif; font-size: 24pt; font-weight: 900; color: ''' + Color + '''; } 
p { font-family: "Roboto", sans-serif; font-size: 14pt; font-weight: 400; color: #aaa; line-height: 150%; } 
.subtitle { font-size: 20pt; font-weight: 700; } 
.logo { height: 40px; } .white { color: #fff } 
.translucent { opacity: 50%; } 
.centered { text-align: center; } 
.button { padding: 15px; padding-left: 30px; padding-right: 30px; background-color: ''' + Color + '''; font-family: "Roboto", sans-serif; font-size: 10pt; font-weight: 700; color:#fff; border: none; border-radius: 0px; } 
.main { background-color: #fff; max-width: 1140px; margin-left: auto; margin-right: auto; } 
.header { background: #FFFFFF; padding-top: 20px; padding-bottom: 25px; } 
.flex-container { display: flex; justify-content: space-between; padding-left: 5px; padding-right: 5px; } 
.content-section { background: #ffffff; padding-top: 0px; padding-bottom: 50px; } 
.hero { background-position: center center; background-repeat: no-repeat; background-size: cover; background-image: url("''' + Img1 + '''"); height: 500px; width: 100%; } 
.services-image-1 { background-position: center center; background-repeat: no-repeat; background-size: cover; background-image: url("''' + Img2 + '''"); height: 300px; width: 50%; } 
.services-image-2 { background-position: center center; background-repeat: no-repeat; background-size: cover; background-image: url("''' + Img3 + '''"); height: 300px; width: 50%; } 
.cta-image { background-position: center center; background-repeat: no-repeat; background-size: cover; background-image: url("''' + Img4 + '''"); height: 300px; width: 50%; } 
.column { width: 50%; } 
.content { position: relative; top: 35%; -ms-transform: translateY(-35%); transform: translateY(-35%); } 
.left { padding-right: 25px; } 
.right { padding-left: 25px; } 
.highlight { background-color: ''' + Color + '''; padding-top: 100px; padding-bottom: 100px; padding-left: 50px; padding-right: 50px; }
@media screen and (max-width: 800px) {
.flex-container{flex-wrap: wrap;}
.column{width: 100%;}
.cta-image{visibility: hidden;height: 50px;}
.services-image-2{width: 100%;order: -1;}
.services-image-1{width: 100%;}
.left{padding-right: 0px;}
.right{padding-left: 0px;}}</style>'''

Header = '<!DOCTYPE html><html><head>' + Meta + Style + '</head>'

NavBar = '''<section class="header">
        <div class="flex-container">
            <img class="logo" src="'''+ LogoUrl +'''">
            <a href="'''+ ButtonUrl +'''" class="button">Book Now</a>
        </div>
    </section>'''

Hero = '''<section class="content-section">
        <div class="hero"></div>
        <div class="flex-container">
            <div class="column left">
                <h1>Book a Shipment Now</h1>
                <a href="'''+ ButtonUrl +'''" class="button">Book Now</a>
            </div>
            <div class="column right">
                <p class="subtitle">We provide fast, efficient, and reliable transportation with best-in-class visibility, efficiency, and transparency.</p>
            </div>
        </div>
    </section>'''

SectionLeft = '''<section class="content-section">
        <div class="flex-container">
            <div class="services-image-1 left"></div>
            <div class="column right">
                <div class="content">
                    <h1>Industry-Leading Technology</h1>
                    <p>We're providing you exceptional visibility on top of our exceptional delivery services. Track every order in real time, request quotes, and view invoices with our customer portal.</p>
                </div>
            </div>
        </div>
    </section>'''

SectionRight = '''<section class="content-section">
        <div class="flex-container">
            <div class="column left">
                <div class="content">
                    <h1>Commitment To Customer Success</h1>
                    <p>Our goal is to always be delighting our customers with exceptional service. Whether this means extra care, timely delivery, or fair rates, we care about you experience booking and moving with us.</p>
                </div>
            </div>
            <div class="services-image-2 right"></div>
        </div>
    </section>'''

Section = '''<section class="content-section">
        <div class="highlight centered">
            <h1 class="white centered">Our Clients</h1>
            <p class="white translucent centered">We're committed to providing exceptional transportation services to all of our clients. When you work with us, you're more than just another customer, you're a part of our family.</p>
        </div>
    </section>'''

CTA = '''<section class="content-section">
        <div class="flex-container">
            <div class="column left">
                <div class="content">
                    <h1>Book a Shipment Now</h1>
                    <a href="'''+ ButtonUrl +'''" class="button">Book Now</a>
                </div>
            </div>
            <div class="cta-image right"></div>
        </div>
    </section>'''

Body = '''<body><div class="main">''' + NavBar + Hero + SectionLeft + SectionRight + Section + CTA + '''</div></body></html>'''

HTML = Header + Body

if not os.path.exists('./docs'):
    os.mkdir('./docs')

HTMLFile = open('docs/index.html', 'w')
HTMLFile.write(HTML)
HTMLFile.close()

print(HTML)