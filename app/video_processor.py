import cv2
import time
from app.detector import ObjectDetector
from app.tracker import ObjectTracker
from app.counter import ObjectCounter

#sistem burada birleştirir her şeyi 
class VideoProcessor:
    def __init__(self, video_path, mode="all"):
        self.video_path = video_path
        self.mode = mode

        self.detector = ObjectDetector()

        self.tracker = ObjectTracker()

        self.counter = ObjectCounter()

    def process(self):
#video okumayı burada yapar ilgili pathten gelen videoyu alır değişkene atar 
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print("Video açılamadı.")
            return
        frame_count = 0
        prev_time=0
        while True:
            #frame alır
            ret, frame = cap.read()
            frame_count +=1

            if frame_count %1 != 0:
                continue

            if not ret:
                break
#cpu yükünü azaltmak için resize yapar fps artar
            frame = cv2.resize(frame, (640, 480))
            if self.counter.roi is None:
                self.counter.set_roi(
                    frame.shape[1],
                    frame.shape[0]
                    )
           
            detections, class_names = self.detector.detect(
                frame,
                self.mode
            )

            tracked_objects = self.tracker.update(
                detections
            )

            x1_roi, y1_roi, x2_roi, y2_roi = (
                self.counter.roi
            )

            cv2.rectangle(
                frame,
                (x1_roi, y1_roi),
                (x2_roi, y2_roi),
                (0, 0, 255),
                2
            )

            for i, track_id in enumerate(
                tracked_objects.tracker_id
            ):
                if track_id is None:
                    continue

                x1, y1, x2, y2 = map(
                    int,
                    tracked_objects.xyxy[i]
                )
#nesnslerin merkezini hesaplar
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                self.counter.count(
                    track_id,
                    center_x,
                    center_y
                )

                class_name = class_names[i]

                label = (
                    f"ID {track_id} | {class_name}"
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    frame,
                    (center_x, center_y),
                    5,
                    (255, 0, 0),
                    -1
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

            total = self.counter.get_count()

            cv2.putText(
                frame,
                f"Count: {total}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                3
            )
            current_time = time.time()
            fps= 1 / (current_time-prev_time)
            prev_time = current_time
            cv2.putText(
                frame,
                f"FPS:{int(fps)}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                color=(255,255,0), 
                thickness=3
            )
            cv2.imshow(
                "Araç & İnsan Sayma",
                frame
            )

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        cap.release()

        cv2.destroyAllWindows()