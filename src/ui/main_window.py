from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from utils.sprite_generator import generate_pet_sprite, save_pet_sprite

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PixelPal")
        self.setGeometry(100, 100, 300, 300)
        
        # Generate and save pet sprite
        pet_image = generate_pet_sprite(size=64)
        save_pet_sprite(pet_image)
        
        # Create QLabel to display the sprite
        self.pet_label = QLabel(self)
        self.pet_label.setPixmap(QPixmap('resources/images/pet_sprite.png'))
        self.pet_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.pet_label)