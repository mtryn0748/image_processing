class ObjectCounter:
    def __init__(self):
        self.counted_ids = set()

        self.total_count = 0

        self.roi = None

    def set_roi(self, frame_width, frame_height):

        x1 = int(frame_width * 0.3)
        y1 = int(frame_height * 0.3)

        x2 = int(frame_width * 0.7)
        y2 = int(frame_height * 0.7)

        self.roi = (x1, y1, x2, y2)

    def is_inside_roi(self, x, y):
        x1, y1, x2, y2 = self.roi

        return (
            x1 <= x <= x2
            and y1 <= y <= y2
        )

    def count(self, track_id, center_x, center_y):

        if track_id in self.counted_ids:
            return

        if self.is_inside_roi(
            center_x,
            center_y
        ):
            self.total_count += 1

            self.counted_ids.add(track_id)

    def get_count(self):
        return self.total_count