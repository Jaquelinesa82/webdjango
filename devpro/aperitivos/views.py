from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo:' ' Motivação', 'youtube_id': 123215}
    return render(request, 'aperitivos/video.html', context={'video': video})
