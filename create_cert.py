from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Générer une clé privée
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Créer un certificat auto-signé
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"FR"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"France"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Paris"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Kaio3"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"kaio3.com"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"kaio3.com")]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Sauvegarder la clé privée
with open("key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Sauvegarder le certificat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM)) 