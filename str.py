import hashlib
import struct
import base64
import urllib

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



def hexstr2ascii(data):
    if data.startswith("0x"):
        data = data[2:]

    return data.decode("hex")


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


def enc_dec_otp(string, key):
    if len(string) != len(key):
        return ""

    size = xrange(len(string))

    res = [chr(ord(string[i]) ^ ord(key[i])) for i in size]

    return "".join(res)


