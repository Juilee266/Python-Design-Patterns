from typing import Protocol, Tuple, Type
from dataclasses import dataclass

class VideoExporter(Protocol):

    def prepare_export(self, video_data):
        """ Prepares video data for exporting"""

    def export(self, path):
        """ Prepares video data for exporting"""

class AudioExporter(Protocol):

    def prepare_export(self, audio_data):
        """ Prepares video data for exporting"""

    def export(self, path):
        """ Prepares video data for exporting"""

class HighQVideoExporter:

    def prepare_export(self, video_data):
        print(f"prepare high quality export video-> {video_data}")

    def export(self, path):
        print(f"Export high quality video -> {path}")

class MedQVideoExporter:

    def prepare_export(self, video_data):
        print(f"prepare medium quality export video-> {video_data}")

    def export(self, path):
        print(f"Export medium quality video-> {path}")

class LowQVideoExporter:

    def prepare_export(self, video_data):
        print(f"prepare low quality export video -> {video_data}")

    def export(self, path):
        print(f"Export low quality video-> {path}")

class HighQAudioExporter:

    def prepare_export(self, audio_data):
        print(f"prepare high quality export audio-> {audio_data}")

    def export(self, path):
        print(f"Export high quality audio-> {path}")

class MedQAudioExporter():

    def prepare_export(self, audio_data):
        print(f"prepare medium quality export audio -> {audio_data}")

    def export(self, path):
        print(f"Export medium quality audio -> {path}")

class LowQAudioExporter:

    def prepare_export(self, audio_data):
        print(f"prepare low quality export audio -> {audio_data}")

    def export(self, path):
        print(f"Export low quality audio -> {path}")

@dataclass
class MediaExporter:
    video: VideoExporter
    audio: AudioExporter

@dataclass
class MediaExporterFactory:
    video_class: Type[VideoExporter]
    audio_class: Type[AudioExporter]

    def __call__(self, *args, **kwargs):
        return MediaExporter (
            self.video_class(),
            self.audio_class()
        )


FACTORIES = {
        "low": MediaExporterFactory(LowQVideoExporter, LowQAudioExporter),
        "med": MediaExporterFactory(MedQVideoExporter, MedQAudioExporter),
        "high": MediaExporterFactory(HighQVideoExporter, HighQAudioExporter)
    }

def get_factory(quality: str) -> MediaExporterFactory:
    return FACTORIES[quality]

if __name__ == "__main__":
    choice = "med"

    factory = get_factory(choice)
    media_factory = factory()
    media_factory.video.prepare_export("sample video")
    media_factory.video.export("sample video path")

    media_factory.audio.prepare_export("sample audio")
    media_factory.audio.export("sample audio path")