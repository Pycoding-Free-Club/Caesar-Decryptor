# Import CaesarDecryptor Modeul
from caesar import CaesarDecryptor

# Create caesar class
caesar = CaesarDecryptor()

# Test
text = "hello world"

text = caesar.calculate(text, 3)

# khoor zruog
print(text)

text = caesar.calculate(text, -3)

# hello world
print(text)
