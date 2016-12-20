import random

class go:

    @staticmethod
    def simple_string_obfus(string, func_name="get_str"):
        print "func {}() string {{\n".format(func_name)
        print "\tvar buffer bytes.Buffer\n"

        i = random.randint(0x11, 0xFF)

        for e in string:
            print '\tbuffer.WriteString( fmt.Sprintf("%c", {} ^ {}) )'.format(hex(ord(e) ^ i), hex(i))
            i = (i + 1) % 0x100

        print "\n\treturn buffer.String()\n"

        print "}"

