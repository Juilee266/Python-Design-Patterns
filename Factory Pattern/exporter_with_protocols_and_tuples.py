from typing import Protocol, Tuple


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

FACTORIES = {
        "low": (LowQVideoExporter, LowQAudioExporter),
        "med": (MedQVideoExporter, MedQAudioExporter),
        "high": (HighQVideoExporter, HighQAudioExporter)
    }

def get_factory(quality: str) -> Tuple[VideoExporter, AudioExporter]:
    v_exp_class, a_exp_class = FACTORIES[quality]
    return v_exp_class(), a_exp_class()

if __name__ == "__main__":
    choice = "high"

    v_exp, a_exp = get_factory(choice)
    v_exp.prepare_export("sample video")
    v_exp.export("sample video path")

    a_exp.prepare_export("sample audio")
    a_exp.export("sample audio path")