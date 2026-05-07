import supervision as sv


class ObjectTracker:
    def __init__(self):
        #nesneleri frameler arasıdna atakip eder id verir yolo her frame bağımsızdır bu sebeple id atarız ve bi sayılan bi daha sayılamz
        self.tracker = sv.ByteTrack()

    def update(self, detections):
        tracked_objects = self.tracker.update_with_detections(
            detections
        )

        return tracked_objects