# analysisshell

This little tool is a analysis shell embedded in ipython to manipulate data. 
I developed this for binary analysis and penetration testing. I just want to have a fast tool to do data transformations
within the ipython environment and be able to work with the transformed results. 

# How to use it

First you have to call the shell.py script. Then you will be in a ipython environment, where you can execute python code
directly. In this I imported my little helper modules. Just type dir(IMPORT_NAME) to see the available methods. For the string 
helper class st.py this would be the following list:

- assemble_x86_32
- assemble_x86_64
- b64dec
- b64enc
- c_bytearray
- disass_x86_32
- disass_x86_64
- grep
- hash_md5
- hash_sha1
- hash_sha224
- hash_sha256
- hash_sha512
- hex_dec
- hex_enc
- hexstr2ascii
- nmap_parse_ports
- nmap_parse_unknown_service
- otp
- path_unix2win
- path_win2unix
- split_into_slices
- url_dec
- url_enc
- xor_byte

A simple example would be a string, which should be hashed. You do this like this:
```python
"A string".hash_sha512()
```
I used the great forbiddenfruit module to be able to monkey patch the string class (for reasons of convenience). 
If you want to use a monkey patched module, you could only import the st.py module and do the following:

```python
st.hash_sha512("A string")
```
This will use the same functionality. 

