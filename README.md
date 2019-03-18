# MyTV Remote Control Infrared Protocol

Last month I decided to learn a little more about communication protocols, so I picked up the first thing next to me that could send a signal to another device. Near my pc there was the remote control of my television (MyTV). So I set up my Arduino board and acquired the signal sent from the remote control.

## Getting Started

Follow "Prerequisites" and "Installing" sections to run the software.

## Prerequisites

Things that you need to have to run the code:
* [git](https://git-scm.com/downloads)
* [Python 2.7](https://www.python.org/downloads/)
* [Arduino IDE](https://www.arduino.cc/en/Main/Software)
* [Arduino© board](https://www.arduino.cc/en/Main/Boards) or [alternatives](https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems)
* [Arduino© Infrared receiver module](https://www.ebay.it/itm/2PCS-X-VS1838B-IR-Infrarot-Empfanger-Modul-Infrared-Sensor-For-Arduino/352569939258?hash=item5216ce553a:g:-zUAAOSwZKlcPpIz) or [Infrared receiver sensor](https://www.ebay.it/itm/3-Pezzi-38Khz-Universal-IR-Infrared-Receiver-TL1838-VS1838B-arduino-compatibile/252815426074?hash=item3adcf9421a:g:MlUAAOSwjL5ZLDJK)

## Installing

### Clone the repository

```bash
git clone "https://github.com/SamuelePerticarari/Analyze-MyTV-Remote-Control-Infrared-Protocol.git" "Analyze-MyTV-Remote-Control-Infrared-Protocol"
```

### Setup the board
Connect the sensor to the board like that.
![Setup board](https://raw.githubusercontent.com/SamuelePerticarari/Analyze-MyTV-Remote-Control-Infrared-Protocol/master/setup-img/setup.png "Setup board")

### Flash the software to the board
1.  Connect the board to your laptop.
2.  Open [Arduino IDE](https://www.arduino.cc/en/Main/Software)
3.  Open "/Analyze-MyTV-Remote-Control-Infrared-Protocol/src/Arduino Project/ReadFromInfraredSensor/ReadFromInfraredSensor.ino"
4.  Make sure that board is recognized.
5.  Flash software.

### Run the Python program

```bash
cd "Analyze-MyTV-Remote-Control-Infrared-Protocol\src"
```
Replace COM4 with YOUR serial port.
```bash
python ReadFromSerialAndDecode.py COM4
```
1.  Wait for serial intialization.
2.  Press enter on your keyboard to start listening from serial.
3.  Press a button on the remote control.
4.  Read decoded Infrared signal


## Demo Output

```
C:\Users\Developer>cd Desktop

C:\Users\Developer\Desktop>git clone "https://github.com/SamuelePerticarari/Analyze-MyTV-Remote-Control-Infrared-Protocol.git" "Analyze-MyTV-Remote-Control-Infrared-Protocol"
Cloning into 'Analyze-MyTV-Remote-Control-Infrared-Protocol'...
remote: Enumerating objects: 27, done.
remote: Counting objects: 100% (27/27), done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 27 (delta 7), reused 9 (delta 3), pack-reused 0
Unpacking objects: 100% (27/27), done.

C:\Users\Developer\Desktop>cd "Analyze-MyTV-Remote-Control-Infrared-Protocol\src"

C:\Users\Developer\Desktop\Analyze-MyTV-Remote-Control-Infrared-Protocol\src>python ReadFromSerialAndDecode.py COM4
Serial connected to: COM4
WAITING FOR SERIAL TO BE READY...
PRESS ENTER TO START READING FROM SERIAL...
WAITING FOR TRIGGER... (PRESS A BUTTON ON THE REMOTE CONTROL)
READING FROM SERIAL...
TRIGGER OK!
END OF SIGNAL...

DECODED:     11111111 00100000 11110111 00001000 0
HEX DECODED: 0xff 0x20 0xf7 0x8 0x0

C:\Users\Developer\Desktop\Analyze-MyTV-Remote-Control-Infrared-Protocol\src>
```

## Extra

You can visually see some captured infrared signals opening file index.html inside "Signals visualization" folder.

![Graph Channel 1](https://raw.githubusercontent.com/SamuelePerticarari/Analyze-MyTV-Remote-Control-Infrared-Protocol/master/Signals%20visualization/sample/Channel%201.png)

## Disclaimer

Sometimes if the serial doesn't set up correctly, the results might be corrupted.

## Tools
* Open source Javascript Graph plotter [Plotly](https://plot.ly/javascript/)
* [Atom text editor](https://atom.io/)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
