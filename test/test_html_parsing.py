from parser import InkuMail

articles = [
    {
        "title": "Inkubio",
        "color": "#008542",
        "articles": [
            {
                "title": "Inkubion ja FK:n Tosi kiva",
                "body": "Inkubio ja fk haaveilee yhdessä lumesta joku päivä ja muuta leipätekstiä"
            }
        ]
    },
    {
        "title": "Other",
        "color": "#34ebde",
        "articles": [
            {
                "title": "Muu artsu",
                "body": "Tää on toinen artsu jossa on hyvää tekstiä"
            },
            {
                "title": "Jälkimmäinen muu artsu",
                "body": "Tän artikkelin pitäis ilmestyä edellisen jälkeen"
            }
        ]
    }
]

im = InkuMail()
im.main()
with open("test.html", "w+", encoding="utf-8") as f:
    f.write(im.mail.prettify())
