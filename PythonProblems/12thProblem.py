def defanging_ip_address(address):
    return address.replace(".", "[.]")

address = "255.100.50.0"
print(defanging_ip_address(address))