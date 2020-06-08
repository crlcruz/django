from django import forms
from django.core.mail import EmailMessage
from core.models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject = 'Email enviado da pagina contato do site django2',
            body = conteudo,
            from_email = 'contato@seudominio.com.br',
            to = ['contato@seudominio.com.br',],
            headers = {'Replay-to': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'qtde', 'imagem']