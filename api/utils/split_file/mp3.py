import typing

from utils.utils import get_ms_time, get_base_file_name
from utils import logger

from pydub import AudioSegment


def get_start_end_time(requested_time: str):
    # TODO make custom exceptions
    parts = requested_time.split(".")
    if len(parts) != 2:
        logger.error("Invalid Part Specified")

    return get_ms_time(parts[0]), get_ms_time(parts[1])


def split_audio(data: dict[str, typing.Any]):
    audio = AudioSegment.from_file(data["source"])
    base_file_name = get_base_file_name(data["source"])
    for part in data["parts"]:
        start, end = get_start_end_time(part)

        if end <= start:
            return "Failure"

        segment = audio[start:end]
        file_name = f"{data['target']}/{base_file_name}_{part}.mp3"
        segment.export(file_name, format="mp3")
        logger.info(f"Successfully saved {file_name}")
