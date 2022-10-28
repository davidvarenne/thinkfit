from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse,Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import JSONResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender,password,receiver,html,subject):
  sender_email = sender
  receiver_email = receiver
  password = password

  message = MIMEMultipart("alternative")
  message["Subject"] = subject
  message["From"] = sender_email
  message["To"] = receiver_email

  part2 = MIMEText(html, "html")
  message.attach(part2)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 

@app.get("/contacts")
async def render(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
  
@app.get("/comingsoon")
async def render(request: Request):
    return templates.TemplateResponse("comingsoon.html", {"request": request})

@app.get("/sitemap.xml")
async def render(request: Request):
  data = """<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">


<url>
  <loc>https://www.fatimatringalithinkfit.com/</loc>
  <lastmod>2022-10-28T09:08:16+00:00</lastmod>
  <priority>1.00</priority>
</url>
<url>
  <loc>https://www.fatimatringalithinkfit.com/contacts</loc>
  <lastmod>2022-10-28T09:08:16+00:00</lastmod>
  <priority>0.80</priority>
</url>


</urlset>
  """
  return Response(content=data, media_type="application/xml")

@app.get("/send_message")
async def send_message(request: Request):
  print('sending email')
  param = request.query_params._dict

  if '@' not in param["email"]:
    pass
    message = False
  else:
    html = """
            <html>
              <body>
                <p>Ciao, hai un nuovo messaggio da:
                  """f'{param["name"]}'"""<br>
                  """f'{param["message"]}'"""<br>
                  """f'{param["email"]}'"""
                </p>
              </body>
            </html>
            """

    send_email("fatimatringali.thinkfit@gmail.com","naujuvjnnmszcabf","davidjohnlaguardia@gmail.com",html, param['subject'])
    send_email("fatimatringali.thinkfit@gmail.com","naujuvjnnmszcabf","f.tringali92@gmail.com",html, param['subject'])
    message = True

  return JSONResponse(content=message)





if __name__ == "__main__":
  # uvicorn main:app --reload
    uvicorn.run(app, host="localhost", port=7777)