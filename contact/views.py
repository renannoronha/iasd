from django.shortcuts import render, redirect
from home.views import BaseView
import smtplib, ssl
from django.conf import settings

# Create your views here.
class ContactView(BaseView):
    template_name = 'contact/contact.html'
    title = 'Contato'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        port = 465
        context = ssl.create_default_context()
        sender = 'comunicacaoiasdcentralfoz@gmail.com'
        receivers = ['comunicacaoiasdcentralfoz@gmail.com']

        message = f"""Subject: Mensagem do Site: {request.POST['subject']}\n\n
        Nome: {request.POST['name']}
        Email: {request.POST['email']}
        Assunto: {request.POST['subject']}
        Mensagem: {request.POST['message']}
        """

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender, settings.EMAIL_PASSWORD)
                server.sendmail(sender, receivers, message,)
        except smtplib.SMTPException:
            print("Error: unable to send email")
        return redirect('contact')

class ContactView(BaseView):
    template_name = 'contact/donate.html'
    title = 'Ofertar'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['title'] = self.title + ' - ' + context['config'].nome
        return render(request, self.template_name, context)
