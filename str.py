import hashlib
import struct
import base64
import urllib
import sys

try:
    import keystone
except ImportError:
    print "Please install keystone"
    print "sudo pip install keystone-engine"
    print "Depenencies: at least cmake (probably llvm, too)"
    sys.exit(-1)

try:
    import capstone
except ImportError:
    print "Please install capstone"
    print "sudo pip install capstone"
    sys.exit(-1)



def nmap_parse_ports(ports_string):
    return [ e.split("/")[0] for e in ports_string.split("\n") ]


def nmap_parse_unknown_service(data_str):
    return data_str.replace("\.",".").replace("\\x20"," ").replace("SF:", "").replace("\\n", "\n").replace("\\x08"," ").replace("\\0","")




def hash_md5(data):
    return hashlib.md5(data).hexdigest().upper()


def hash_sha1(data):
    return hashlib.sha1(data).hexdigest().upper()


def hash_sha224(data):
    return hashlib.sha224(data).hexdigest().upper()


def hash_sha512(data):
    return hashlib.sha512(data).hexdigest().upper()



def base64_dec(data):
    return base64.b64decode(data)


def base64_enc(data):
    return base64.b64encode(data)



def url_enc(in_str):
    return urllib.quote_plus(in_str)

def url_dec(in_str):
    return urllib.unquote(in_str)


def path_win2unix(str_path):
    return "/".join( str_path.split("\\") )

def path_unix2win(str_path):
    return "\\".join( str_path.split("/") )


def hexstr2ascii(data):
    if data.startswith("0x"):
        data = data[2:]

    return data.decode("hex")

def hex_enc(data):
    return data.encode("hex")

def hex_dec(data):
    return data.decode("hex")


def split_into_slices(coll, num):
    return [coll[i:i+num] for i in range(0, len(coll), num)]


def str2bytearray(string):
    if not string:
        return ""

    s = "char byte_array[] = {"

    for e in string:
        s += hex(ord(e)) + ", "

    if "0x0," in s:
        print "[!] ERROR null byte in byte array!"
        return ""

    s = s + "0x0};"

    return s


def disass_x86_64(data, start_addr=0x1000):
    res = ""

    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    for i in md.disasm(data, start_addr):
        line = "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)
        #print(line)
        res += line + "\n"

    return res


def disass_x86_32(data, start_addr=0x1000):
    res = ""

    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)
    for i in md.disasm(data, start_addr):
        line = "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)
        #print(line)
        res += line + "\n"

    return res


def assemble_x86_32(code):
    try:
        ks = keystone.Ks(keystone.KS_ARCH_X86,
                keystone.KS_MODE_32)
        encoding, count = ks.asm(code)
        print("%s = %s (number of statements: %u)" %(code, encoding, count))

        return encoding
    except keystone.KsError as e:
        print("ERROR: %s" %e)

        return None



def assemble_x86_64(code):
    try:
        ks = keystone.Ks(keystone.KS_ARCH_X86,
                         keystone.KS_MODE_64)
        encoding, count = ks.asm(code)
        print("%s = %s (number of statements: %u)" %(code, encoding, count))

        return encoding
    except keystone.KsError as e:
        print("ERROR: %s" %e)

        return None



def otp(string, key):
    if len(string) != len(key):
        return ""

    size = xrange(len(string))

    res = [chr(ord(string[i]) ^ ord(key[i])) for i in size]

    return "".join(res)


def xor_byte(string, keybyte):
    res_str = ""

    for c in string:
        xored_val = ord(c) ^ keybyte

        if xored_val == 0:
            print "[!] ERROR xored value is a null byte!"
            return ""

        res_str += chr(xored_val)

    return res_str


