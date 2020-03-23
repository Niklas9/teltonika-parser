

import binascii
import struct

# https://wiki.teltonika-sas.com/view/Codec#Codec_12
s = '00000000000000900C010600000088494E493A323031392F372F323220373A3232205254433A323031392F372F323220373A3533205253543A32204552523A312053523A302042523A302043463A302046473A3020464C3A302054553A302F302055543A3020534D533A30204E4F4750533A303A3330204750533A31205341543A302052533A332052463A36352053463A31204D443A30010000C78F'

uhs = binascii.unhexlify(s)

print(uhs)
print('bytes :: {}, {}'.format(uhs[0:4], struct.unpack('>L', uhs[0:4])[0]))
print('data size :: {}, {}'.format(uhs[4:8], struct.unpack('>L', uhs[4:8])[0]))
print('codec id :: {}, {}'.format(uhs[8:9], struct.unpack('<L', uhs[8:9])[0]))
print('response quantity 1 :: {}'.format(uhs[9:10]))
print('response type :: {}'.format(uhs[10:11]))
print('response size :: {}, {}'.format(uhs[11:15], struct.unpack('>L', uhs[11:15])[0]))
