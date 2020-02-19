import os

LogoUrl = input('logo url: ')
HeroUrl = input('image url: ')

DarkColor = input('dark color code: ')
HighlightColor = input('highlight color code: ')

CompanyName = input('company name: ')
CompanyPhone = input('company phone: ')
CompanyEmail = input('company email: ')
Address = input('company address: ')
WebsiteUrl = input('company website url: ')

ContactName1 = input('first contact name: ')
ContactEmail1 = input('first contact email: ')
ContactPhone1 = input('first contact phone: ')

ContactName2 = input('second contact name: ')
ContactEmail2 = input('second contact email: ')
ContactPhone2 = input('second contact phone: ')

HTML = '''<!DOCTYPE html>
<html>
<head>
    <title><<company_name>></title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,700,900&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #efefef;
            text-align: left;
            padding: 20px;
        }

        h1 {
            font-family: "Montserrat", sans-serif;
            font-size: 24pt;
            font-weight: 500;
            color: <<dark_color>>;
            margin-right: 25px;
        }

        h2 {
            font-family: "Montserrat", sans-serif;
            font-size: 20pt;
            font-weight: 500;
            color: #333333;
            line-height: 16px;
        }

        .bottom-border {
            border-bottom: 2.5px solid <<highlight_color>>;
            width: 75%;
        }

        h3 {
            font-family: "Montserrat", sans-serif;
            font-size: 14pt;
            font-weight: 500;
            color: #ffffff;
        }

        h4 {
            font-family: "Montserrat", sans-serif;
            font-size: 12pt;
            font-weight: 500;
            color: #ffffff;
        }

        .special {
            padding: 8px;
            padding-left: 10px;
        }

        p {
            font-family: "Montserrat", sans-serif;
            font-size: 10pt;
            font-weight: 400;
            color: #aaa;
            line-height: 150%;
        }

        .color {
            background-color: <<dark_color>>;
            margin-top: 25px;
        }

        .highlight-border {
            border-top: 10px solid <<highlight_color>>
        }

        .more-padding {
            margin-bottom: 50px;
        }

        .logo {
            height: 90px;
            margin-left: 25px;
        }

        .white {
            color: #fff;
        }

        .gray {
            background-color: #efefef;
        }

        .main {
                background-color: #fff;
                max-width: 1140px;
                margin-left: auto;
                margin-right: auto;
                padding: 20px;
        }

        .header {
            background: #FFFFFF;
            padding-top: 20px;
            padding-bottom: 15px;
        }

        .flex-container {
            display: flex;
            justify-content: space-between;
        }

        .content-section {
            background: #ffffff;
            padding-top: 0px;
        }

        .hero {
            background-position: center center;
            background-repeat: no-repeat;
            background-size: cover;
            background-image: url("<<hero_url>>");
            height: 400px;
            width: 50%;
            margin-top: -50px;
        }

        .column {
            width: 50%;
            padding: 20px;
        }

        .left {
            width: 50%;
        }

        .right {
            width: 50%;
        }

    </style>
</head>

<body>
<div class="main">
    <section class="header">
        <div class="flex-container">
            <img class="logo" src="<<logo_url>>">
            <h1>Capability Statement</h1>
        </div>
    </section>

    <section class="content-section">
        <div class="flex-container color highlight-border">
            <div class="flex-container left" style="padding-left:5px">
                <div class="column">
                    <h3><<contact_name_1>></h3>
                    <p><<contact_email_1>></p>
                    <p><<contact_phone_1>></p>
                    <br>
                    <h3><<contact_name_2>></h3>
                    <p><<contact_email_2>></p>
                    <p><<contact_phone_2>></p>
                </div>
                <div class="column">
                    <h3><<company_name>></h3>
                    <p><<company_email>></p>
                    <p><<company_phone>></p>
                    <p><<website_url>></p>
                    <br>
                    <p><<address>></p>
                </div>
            </div>
            <div class="hero right"></div>
        </div>
    </section>

    <section class="content-section">
        <div class="flex-container">
            <div class="column left">
                <div class="bottom-border"><h2>Corporate Overview</h2></div>
                <p class="more-padding">Our mission is to provide you the fastest, safest, and more affordable transportation
                    services - while maintaining exceptional customer service. Offering a full range of  
                    options including full truckload and less than truckload freight, we're your go-to
                    partner for full-scale logistics services. When you choose us, you're more than just 
                    a customer - you're part of our family.</p>
                <div class="bottom-border"><h2>Our Services</h2></div>
                <p class="more-padding">We offer innovative freight solutions and services that are designed with your bottom 
                    line in mind. Enjoy unparalled peace of mind with fast, efficient, and reliable transportation of your goods 
                    and shipments with best-in-class visibility to reduce shipper risk.
                    a customer - you're part of our family.</p>
                <div class="bottom-border"><h2>Digital Transportation</h2></div>
                <p class="more-padding">We're more than just a transporation business. We've invested in industry leading technology 
                    to bring you digitally-enabled services. Enjoy real-time information and advanced visibility on all operations, 
                    through our technology partners at FreightPath</p>
            </div>
            <div class="column right gray">
                <div class="color" style="border-left: 34px solid <<highlight_color>>">
                    <h4 class="special">Real Time Track & Trace</h4>
                </div>
                <p class="more-padding" style="padding-left:34px;">
                    Using industry leading cloud technology, you can track every order in real time, request quotes, and view invoices online 
                    with our customer portal. No phone calls, emails, or messy exchanges required.
                </p>
                <div class="color" style="border-left: 34px solid <<highlight_color>>">
                    <h4 class="special">Exceptional Customer Service</h4>
                </div>
                <p class="more-padding" style="padding-left:34px;">
                    We pride ourselves on our white-glove service. It's our guarantee to provide an exceptional experience that you can trust 
                    from the first quote through booking, delivery, and invoicing.
                </p>
                <div class="color" style="border-left: 34px solid <<highlight_color>>">
                    <h4 class="special">Automatic Documentation</h4>
                </div>
                <p class="more-padding" style="padding-left:34px;">
                    No need to worry about creating and managing your freight paperwork. We handle it all - from the shipping labels to the proof
                    of delivery. It's an all-inclusive service that's sure to delight.
                </p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <div class="flex-container color highlight-border" style="margin-top: 0px;">
            <div class="column">
                <h3>Get Started With Us</h3>
                <p>
                    Visit us online today or call us for a free personal freight consultation to see how you can leverage our best in 
                    class services for your business today.
                </p>
            </div>
            <div class="column">
                <h3><<company_name>></h3>
                <p><<company_email>></p>
                <p><<company_phone>></p>
            </div>
        </div>
    </section>

    <section class="content-section">
        <div class="flex-container" style="margin-top: 0px; background-color: <<highlight_color>>">
            <div class="column" style="padding-top: 5px;padding-bottom: 5px;">
                <p class="white"><<company_name>></p>
            </div>
            <div class="column" style="padding-top: 5px;padding-bottom: 5px;">
                <p class= "white" style="text-align: right;"><<website_url>></p>
            </div>
        </div>
    </section>
</div>
</body>
</html>'''

HTML = HTML.replace('<<logo_url>>', LogoUrl)
HTML = HTML.replace('<<hero_url>>', HeroUrl)
HTML = HTML.replace('<<dark_color>>', DarkColor)
HTML = HTML.replace('<<highlight_color>>', HighlightColor)
HTML = HTML.replace('<<company_name>>', CompanyName)
HTML = HTML.replace('<<company_phone>>', CompanyPhone)
HTML = HTML.replace('<<company_email>>', CompanyEmail)
HTML = HTML.replace('<<address>>', Address)
HTML = HTML.replace('<<website_url>>', WebsiteUrl)
HTML = HTML.replace('<<contact_name_1>>', ContactName1)
HTML = HTML.replace('<<contact_email_1>>', ContactEmail1)
HTML = HTML.replace('<<contact_phone_1>>', ContactPhone2)
HTML = HTML.replace('<<contact_name_2>>', ContactName2)
HTML = HTML.replace('<<contact_email_2>>', ContactEmail2)
HTML = HTML.replace('<<contact_phone_2>>', ContactPhone2)

if not os.path.exists('./docs'):
    os.mkdir('./docs')
    
HTMLFile = open('docs/brochure.html', 'w')
HTMLFile.write(HTML)
HTMLFile.close()

print(HTML)