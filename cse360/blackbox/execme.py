#!/usr/bin/exec-suid -- /usr/local/bin/python -I

from pwn import *

p = process(['java', '-jar', '/challenge/UserNameValidator.jar'])

p.interactive()
