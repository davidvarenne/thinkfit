from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from fastapi.responses import JSONResponse
# import win32com.client as win32


# def send_email(body, subject, receiver, attachments='', mode = 'text'):

#     assert(isinstance(subject, str))


#     outlook = win32.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.To = receiver
#     mail.Subject = subject

#     if mode =='text':
#         mail.Body = body
#     elif mode == 'html':
#         mail.HTMLBody  = body
        
#     #In case you want to attach a file to the email
#     if attachments!='':
#         for attach in attachments:
#             mail.Attachments.Add(attach)

#     mail.Send()

#     return


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/home")
async def render(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 

@app.get("/contacts")
async def render(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/send_message")
async def send_message(request: Request):
  print('sending email')
  param = request.query_params._dict
  body = """<html> 
                    <body> 
                    <div>"""f'{param["name"]}'"""</div> 
                    <div>"""f'{param["email"]}'"""</div> 
                    <div>"""f'{param["subject"]}'"""</div> 
                    <div>"""f'{param["message"]}'"""</div> 
                    </body>
            </html> 
          """
  # send_email(body, subject = param["subject"], receiver = 'David.Laguardia@statkraft.com', attachments='', mode = 'html')


# if __name__ == "__main__":
  # uvicorn main:app --reload
    # uvicorn.run(app, host="localhost", port=7676)