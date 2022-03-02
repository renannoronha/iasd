def create_AboutPrimeiraSecao(sender, **kwargs):
    from .models import AboutPrimeiraSecao
    from django.contrib.sites.models import Site
    if not AboutPrimeiraSecao.objects.all().first():
        AboutPrimeiraSecao.objects.create(
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

def create_AboutSegundaSecao(sender, **kwargs):
    from .models import AboutSegundaSecao
    from django.contrib.sites.models import Site
    if not AboutSegundaSecao.objects.all().first():
        AboutSegundaSecao.objects.create(
            site=Site.objects.get_current(),
            upperText='Bem-vindo',
            titulo='IASD Central de Foz do Iguaçu',
            texto='Nossa fé é centralizada em Cristo, por isso buscamos viver Ele, até o dia de viver com Ele. Nossa missão é compartilhar com você o que vivemos. Aceite o convite: Venha e viva Cristo!',
            botaoLink='about',
            botaoText='Conheça mais sobre nós...',
        )

def create_AboutTerceiraSecao(sender, **kwargs):
    from .models import AboutTerceiraSecao
    from django.contrib.sites.models import Site
    if not AboutTerceiraSecao.objects.all().first():
        AboutTerceiraSecao.objects.create(
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