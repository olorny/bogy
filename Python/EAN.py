def calculate_checksum(ean_prefix):
    checksum = 0
    for index in range(len(ean_prefix)):
        digit = int(ean_prefix[index])
        if index % 2 == 0:
            weight = 3
        else:
            weight = 1
        checksum += digit * weight
    
    while checksum >= 10:
        checksum = checksum - 10
    
    return checksum

def validate_ean(ean):
    checksum = calculate_checksum(ean[:-1])
    last_digit = int(ean[-1])

    return checksum == last_digit

### MAIN ###
ean_input = input("Bitte geben Sie die vollständige 13-stellige EAN oder die ersten 12 Stellen ein: ")

if len(ean_input) == 13:
    if validate_ean(ean_input):
        print("Die EAN ist gültig.")
    else:
        print("Die EAN ist ungültig.")
elif len(ean_input) == 12:
    checksum = calculate_checksum(ean_input)
    print(f"Die berechnete Prüfziffer für die angegebene EAN ist: {checksum}")
else:
    print("Ungültige Eingabe. Bitte geben Sie entweder eine vollständige 13-stellige EAN oder die ersten 12 Stellen ein.")