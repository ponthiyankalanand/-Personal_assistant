import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("music/02 Dil Diyan Gallan - Tiger Zinda Hai.mp3")
play_obj = wave_obj.play()
play_obj.wait_done()
