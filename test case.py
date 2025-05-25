import validators

print(validators.url("example.com"))         # False
print(validators.url("http://example.com"))  # True
print(validators.url("https://example.com")) # True