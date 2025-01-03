std::string generateSalt(int length) {
    std::string salt;
    salt.resize(length);
    RAND_bytes(reinterpret_cast<unsigned char*>(salt.data()), length);
    return salt;
}

std::string hashPassword(const std::string& password, const std::string& salt) {
    return password + salt; // substitua com sua lógica de hash
}

int main() {
    std::string password = "mypassword";
    std::string salt = generateSalt(16);
    std::string hashedPassword = hashPassword(password, salt);

    std::cout << "Salt: " << salt << std::endl;
    std::cout << "Hashed Password: " << hashedPassword << std::endl;

    return 0;
}
