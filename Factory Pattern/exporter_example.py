from abc import ABC, abstractmethod

class VideoExporter(ABC):

    @abstractmethod
    def prepare_export(self, video_data):
        """ Prepares video data for exporting"""

    @abstractmethod
    def export(self, path):
        """ Prepares video data for exporting"""

class AudioExporter(ABC):

    @abstractmethod
    def prepare_export(self, audio_data):
        """ Prepares video data for exporting"""

    @abstractmethod
    def export(self, path):
        """ Prepares video data for exporting"""

class HighQVideoExporter(VideoExporter):

    def prepare_export(self, video_data):
        print(f"prepare high quality export video-> {video_data}")

    def export(self, path):
        print(f"Export high quality video -> {path}")

class MedQVideoExporter(VideoExporter):

    def prepare_export(self, video_data):
        print(f"prepare medium quality export video-> {video_data}")

    def export(self, path):
        print(f"Export medium quality video-> {path}")

class LowQVideoExporter(VideoExporter):

    def prepare_export(self, video_data):
        print(f"prepare low quality export video -> {video_data}")

    def export(self, path):
        print(f"Export low quality video-> {path}")

class HighQAudioExporter(AudioExporter):

    def prepare_export(self, audio_data):
        print(f"prepare high quality export audio-> {audio_data}")

    def export(self, path):
        print(f"Export high quality audio-> {path}")

class MedQAudioExporter(AudioExporter):

    def prepare_export(self, audio_data):
        print(f"prepare medium quality export audio -> {audio_data}")

    def export(self, path):
        print(f"Export medium quality audio -> {path}")

class LowQAudioExporter(AudioExporter):

    def prepare_export(self, audio_data):
        print(f"prepare low quality export audio -> {audio_data}")

    def export(self, path):
        print(f"Export low quality audio -> {path}")

class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass

class HighQExporterFactory(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return HighQVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return HighQAudioExporter()


class MedQExporterFactory(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return MedQVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MedQAudioExporter()


class LowQExporterFactory(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LowQVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LowQAudioExporter()

def get_factory(choice) -> ExporterFactory:
    factories = {
        "low": LowQExporterFactory(),
        "med": MedQExporterFactory(),
        "high": HighQExporterFactory()
    }
    return factories[choice]

if __name__ == "__main__":
    choice = "high"

    factory = get_factory(choice)

    v_exp = factory.get_video_exporter()
    a_exp = factory.get_audio_exporter()

    v_exp.prepare_export("sample video")
    v_exp.export("sample video path")

    a_exp.prepare_export("sample audio")
    a_exp.export("sample audio path")