from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>PoC | Mohamed-Elbadry</title>
  </head>

  <body>
    <div class="container-lg px-3 my-5 markdown-body">

      <center><h1>Takeover PoC</a></h1>
      <p>This is a Takeover PoC by Mohamed Elbadry! This issue is being reported to your security team If not please contact me for more info</p><br><br>

<h3>Contacts</h3>
  <li>
    <ul>
      <li>me@melbadry9.xyz</li>
      <li>https://hackerone.com/melbadry9</li>
      <li>https://twitter.com/_melbadry9</li>
    </ul>
  </li></center>

    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
    <script>anchors.add();</script>

  </body>
</html>"""
