import cv2


def get_video_writer(path, width, height, fps):
    """
    En stabil çözüm:
    OpenCV -> AVI (XVID)
    MP4 encoding FFmpeg'e bırakılır
    """

    # AVI stabil codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    writer = cv2.VideoWriter(
        path,
        fourcc,
        fps,
        (width, height),
        True
    )

    if not writer.isOpened():
        raise RuntimeError(
            "VideoWriter could not be opened. "
            "XVID codec failed."
        )

    return writer
