def create_config(sender, **kwargs):
    from .models import Config
    from django.contrib.sites.models import Site
    if not Config.objects.filter(id=1):
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
    from django.contrib.sites.models import Site
    import datetime
    if not HorariosCulto.objects.filter(id=1):
        HorariosCulto.objects.create(weekday='Sábado', time=datetime.time(9, 0, 0))
        HorariosCulto.objects.create(weekday='Domingo', time=datetime.time(20, 0, 0))
        HorariosCulto.objects.create(weekday='Quarta', time=datetime.time(20, 0, 0))