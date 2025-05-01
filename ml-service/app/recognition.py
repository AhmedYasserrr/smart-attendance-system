import os
import random
import string

import cv2
import numpy as np
from deepface import DeepFace
from utils import Configuration


class Recognition:
    def __init__(self):
        self.config = Configuration().load_config()

    def find(self, img: np.ndarray) -> list:
        matches = DeepFace.find(
            img_path=img,
            db_path=self.config["img_db_path"],
            model_name=self.config["model_name"],
            detector_backend=self.config["detector_backend"],
            distance_metric=self.config["distance_metric"],
        )[0]

        matches["identity"] = matches["identity"].apply(
            lambda path: os.path.basename(os.path.dirname(path))
        )

        results = [
            {"identity": match.identity, "distance": match.distance}
            for match in matches.itertuples(index=False)
        ]
        return results

    def save(self, img: np.ndarray, name: str) -> str:
        if not os.path.exists(self.config["img_db_path"]):
            os.makedirs(self.config["img_db_path"])

        rand = self._generate_random_string()
        path = os.path.join(self.config["img_db_path"], name, f"{name}_{rand}.jpg")

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        cv2.imwrite(path, img)
        return path

    def _generate_random_string(self, length: int = 8) -> str:
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))
