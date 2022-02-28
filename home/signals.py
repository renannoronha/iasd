def create_config(sender, **kwargs):
    from .models import Config
    from django.contrib.sites.models import Site
    if not Config.objects.all().first():
        Config.objects.create(
            site=Site.objects.get_current(),
            nome='IASD Central de Foz',
            telefone='+55 45 99999-9999',
            email='email@email.com',
            endereco='Av. República Argentina, 552 85851-200 Foz do Iguaçu, PR',
            facebook='https://www.facebook.com/iasd.fozcentral',
            youtube='https://www.youtube.com/channel/UCsLvHS14G27MukIDiVDgiWQ',
            twitter='',
            instagram='https://www.instagram.com/iasdcentralfoz2/',
            textoRodape='Lancem sobre Ele toda a ansiedade porque Ele tem cuidado de vós. I Pedro 5:7',
        )

def create_horario(sender, **kwargs):
    from .models import HorariosCulto
    import datetime
    if not HorariosCulto.objects.all().first():
        HorariosCulto.objects.create(weekday='Sábado', time=datetime.time(9, 0, 0))
        HorariosCulto.objects.create(weekday='Domingo', time=datetime.time(20, 0, 0))
        HorariosCulto.objects.create(weekday='Quarta', time=datetime.time(20, 0, 0))

def create_primeiraSecao(sender, **kwargs):
    from .models import PrimeiraSecao
    from django.contrib.sites.models import Site
    if not PrimeiraSecao.objects.all().first():
        PrimeiraSecao.objects.create(
            site=Site.objects.get_current(),
            icone1='flaticon-church',
            titulo1='Adoração',
            texto1='Deus é espírito, e é necessário que os seus adoradores o adorem em espírito e em verdade. João 4:24',
            icone2='flaticon-pray',
            titulo2='Oração',
            texto2='E tudo o que pedirem em oração, se crerem, vocês receberão. Mateus 21:22',
            icone3='flaticon-love',
            titulo3='Amor de Deus',
            texto3='Porque Deus tanto amou o mundo que deu o seu Filho Unigênito, para que todo o que nele crer não pereça, mas tenha a vida eterna. João 3:16',
            servicesTitulo='Os justos clamam, o Senhor os ouve e os livra de todas as tribulações. Salmos 34:17'
        )

def create_segundaSecao(sender, **kwargs):
    from .models import SegundaSecao
    from django.contrib.sites.models import Site
    if not SegundaSecao.objects.all().first():
        SegundaSecao.objects.create(
            site=Site.objects.get_current(),
            upperText='Bem-vindo',
            titulo='IASD Central de Foz do Iguaçu',
            texto='Nossa fé é centralizada em Cristo, por isso buscamos viver Ele, até o dia de viver com Ele. Nossa missão é compartilhar com você o que vivemos. Aceite o convite: Venha e viva Cristo!',
            botaoLink='about',
            botaoText='Conheça mais sobre nós...',
        )

def create_terceiraSecao(sender, **kwargs):
    from .models import TerceiraSecao
    from django.contrib.sites.models import Site
    if not TerceiraSecao.objects.all().first():
        TerceiraSecao.objects.create(
            site=Site.objects.get_current(),
            titulo='Igreja Adventista no Mundo',
            dado1='Membros',
            valor1=1000000,
            dado2='Pastores',
            valor2=65000,
            dado3='Doações',
            valor3=500000,
            dado4='Igrejas',
            valor4=1547,
        )