from ultralytics import YOLO
import supervision as sv


class ObjectDetector:
    def __init__(self, model_path="../models/yolov8n.pt"):
        self.model = YOLO(model_path)

        self.vehicle_classes = [
            "car",
            "bus",
            "truck",
            "motorcycle"
        ]

    def detect(self, frame, mode="all"):
        results = self.model(frame, verbose=False, conf = 0.4)[0] # %40 altındaki doğruuk oranlarını alma 

        detections = sv.Detections.from_ultralytics(results)

        class_names = []

        filtered_indices = []

        for i, class_id in enumerate(detections.class_id):
            class_name = self.model.names[class_id]

            if mode == "human":
                if class_name != "person":
                    continue

            elif mode == "vehicle":
                if class_name not in self.vehicle_classes:
                    continue

            elif mode == "all":
                if (
                    class_name != "person"
                    and class_name not in self.vehicle_classes
                ):
                    continue

            filtered_indices.append(i)
            class_names.append(class_name)

        detections = detections[filtered_indices]

        return detections, class_names      