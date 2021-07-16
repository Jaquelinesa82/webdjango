from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Motivação', 'youtube_id': '9iZLDnW_vwU'},
    {'slug': 'instalacao', 'titulo': 'Instalação', 'youtube_id': 'XdFUpFUDt88'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
