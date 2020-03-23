

class Teltonika(object):

    @staticmethod
    def is_imei(imei: str) -> bool:
        # imei should be of length 15
        return False


# ack is socket.send(chr(01))

t = Teltonika()
assert t.is_imei('000F383632323539353838383334323930')
