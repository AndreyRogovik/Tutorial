import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QMimeData
from PIL import Image
import rembg
import io

class ImageView(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px dashed gray;")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].isLocalFile():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.setPixmap(QPixmap(file_path))
        self.parent().remove_background(file_path)  # Call the remove_background method with the file path

class ImageBackgroundRemover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Background Remover")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.image_view = ImageView(self)
        self.result_view = QLabel(self)
        self.result_view.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_view)
        layout.addWidget(self.result_view)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def remove_background(self, input_image_path):
        with open(input_image_path, "rb") as f:
            img = f.read()
        result = rembg.remove(img)
        img = Image.open(io.BytesIO(result)).convert("RGBA")

        # Create a new image with a transparent background
        transparent_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        transparent_img.paste(img, (0, 0), mask=img)

        output_path = "C:\\Users\\AR\\Desktop\\New folder\\output.png"  # Specify the desired output path
        transparent_img.save(output_path, "PNG")

        # Display the result
        self.display_result(transparent_img)

    def display_result(self, result_image):
        image_data = result_image.convert("RGBA")
        pixmap = self.pil_to_pixmap(image_data)
        self.result_view.setPixmap(pixmap)

    def pil_to_pixmap(self, image):
        image = image.convert("RGBA")
        data = image.tobytes("raw", "RGBA")
        q_image = QImage(data, image.size[0], image.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(q_image)
        return pixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageBackgroundRemover()
    window.show()
    sys.exit(app.exec_())
