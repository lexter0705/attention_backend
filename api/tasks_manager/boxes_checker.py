from api.models import ErrorMessage, Labels
from config import LabelsConfig


class BoxesChecker:
    def __init__(self, config: LabelsConfig):
        if not isinstance(config, LabelsConfig):
            raise TypeError('config is not LabelsConfig')

        self.__config = config

    def check_boxes(self, labels: Labels) -> list[ErrorMessage]:
        result = []
        for l in labels.boxes:
            if l.name in self.__config.error_labels:
                print(l.name)
                result.append(ErrorMessage(type="warning", object_name=l.name, warning_type="error"))
            elif l.name in self.__config.warning_labels:
                result.append(ErrorMessage(type="warning", object_name=l.name, warning_type="warning"))
        return result
