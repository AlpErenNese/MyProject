import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont

class Win(QMainWindow):
    def __init__(self):
        super().__init__()

    
        # QMainWindow nesnesinin boyutunu ayarlayın
        self.resize(550, 250)

        # QLabel öğesini tanımlayın ve pencereye ekleyin
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 450, 50)
        self.setWindowTitle('Hava Durumu')

        # QLabel nesnesinin fontunu değiştirin
        font = QFont('Arial', 14, QFont.Bold)
        self.label.setFont(font)

        # Hava durumu verilerini almak için get_weather() metodunu çağırın
        self.get_weather()

    def get_weather(self):
        city = 'Istanbul'
        api_key = '14cee3eedfbf58aa91ac2a57cc6461c8'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            if temperature is not None:
                text = f"Hava Durumu: {weather_description}, {temperature:.0f}°C"
            else:
                text = "Hava durumu bilgisi alınamadı."
        else:
            text = "Hava durumu bilgisi alınamadı."

        # QLabel öğesinin metnini güncelleyin
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Win sınıfından bir örnek oluşturun ve pencereyi görüntüleyin
    win = Win()
    win.show()

    sys.exit(app.exec_())