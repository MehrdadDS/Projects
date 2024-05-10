from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.uix.filechooser import FileChooserIconView

class CameraApp(App):
    def build(self):
        # Layout
        layout = FloatLayout()

        # Camera
        self.camera = Camera(play=True)
        self.camera.resolution = (640, 480)
        layout.add_widget(self.camera)

        # Button to take a picture
        take_picture_button = Button(text="Take Picture", size_hint=(None, None), size=(150, 50),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.1})
        take_picture_button.bind(on_press=self.take_picture)
        layout.add_widget(take_picture_button)

        # Button to upload a picture
        upload_button = Button(text="Upload Picture", size_hint=(None, None), size=(150, 50),
                               pos_hint={'center_x': 0.5, 'center_y': 0.2})
        upload_button.bind(on_press=self.upload_picture)
        layout.add_widget(upload_button)

        return layout

    def take_picture(self, instance):
        # Capture and save the picture using Kivy's camera widget
        image_path = 'receipt_image.png'
        self.camera.export_to_png(image_path)
        print("Picture taken and saved as 'receipt_image.png'")

    def upload_picture(self, instance):
        # Open file chooser to select a picture
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.on_file_selected)
        layout = FloatLayout()
        layout.add_widget(file_chooser)
        self.popup = popup = Popup(title="Choose a Picture", content=layout, size_hint=(0.9, 0.9))
        popup.open()

    def on_file_selected(self, instance, selected):
        # Process the selected picture
        print("Selected file:", selected[0])
        # Do something with the selected file path
        self.popup.dismiss()

if __name__ == '__main__':
    CameraApp().run()
