from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
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

@app.get("/send_message")
async def send_message(request: Request):
  print('sending email')
  param = request.query_params._dict
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

  # send_email("fatimatringali.thinkfit@gmail.com","naujuvjnnmszcabf","davidjohnlaguardia@gmail.com",html, param['subject'])
  # send_email("fatimatringali.thinkfit@gmail.com","naujuvjnnmszcabf","f.tringali92@gmail.com",html, param['subject'])








if __name__ == "__main__":
  # uvicorn main:app --reload
    uvicorn.run(app, host="localhost", port=7676)