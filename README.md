# Teltonika parser
Python 3 library for parsing Teltonika device <-> server communication.
Solely codec 12 is supported at the moment.

This is work in progress.

## Example
Example goes here.

## Todos
* Setup proper unit test handling
* Setup static analysis tool (to check type hints)
* Setup project at some CI tool (like Travis, but try smth new)
* Add ACK and reject response
* Parse first GPS coordinates and add unit tests
* Add example for setting up with TCP socket connection
* Setup new project to host TCP socket connection in scalable way, using Python
  async
* Support Codec 8 and 8 Extended
* Add support for UDP protocol

## Codec documentation
* https://wiki.teltonika-sas.com/view/Codec#Codec_12

### Integration examples
* https://community.teltonika-gps.com/4965/how-to-read-data-from-teltonika-fmb001-with-a-python-script
* https://stackoverflow.com/questions/47128207/connecting-teltonika-device-with-python-over-tcp
* https://github.com/Kein1945/GPS_Teltonika_Server

## License
LGPL. Please see `LICENSE` file in the root of this repo.
