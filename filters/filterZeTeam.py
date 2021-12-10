import cv2


def FilterZeTeam(image):
    filter =cv2.putText(image, "#AGLT_CORP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return filter