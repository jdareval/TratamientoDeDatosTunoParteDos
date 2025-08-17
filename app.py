# Archivo que contiene la codificación de la API
# API de busqueda de indicadores de compromiso (IOC)
from fastapi import FastAPI, status

#Inicializa la palicación FastAPI
app = FastAPI(
    title="API DE BUESQUEDA DE INDICADORES DE COMPROMISO (IOC)",
    description="Un microservicio para buscar hashes de archivos y dominios" \
    "en una base de datos simulada de inteligencia de amenazas.",
    version="1.0.0",
)
# ----- Base de Datos Simulada -----
# En un ambiente de produccion, estos datos se obtienen de una BD como
# PostgreSQL, Redis etc.
# Para este ejercicio se utiliza un diccionario de Python como base de datos
KNOWN_MALWARE_HASHES = {
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f": "WannaCry Ransomware",
    "e88954461a787325b413636402722122": "Emotet Trojan",
    "d41d8cd98f00b204e9800998ecf8427e": "Test Hash (vacío)",
}
KNOWN_MALICIOUS_DOMAINS = {
    "evil-updates.net": "Servidor de Comando y Control (C2) para troyano bancario",
    "secure-login-portal.com": "Campaña de Phishing dirigida a entidades financieras",
    "microsoft-updates.org": "Dominio de typosquatting para distribución de malware"
}
# ______________________________________________________________________
# --------- EndPoint de la API --------
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Búsqueda de (IOC). Use /docs para ver la documentación."}

# feature principal
@app.get("/api/lookup/hash/{file_hash}", status_code=status.HTTP_200_OK)
def lookup_hash(file_hash: str):
    """
    Busca un hash de archivo en la base de datos simulada.
    """
    threat_name = KNOWN_MALWARE_HASHES.get(file_hash.lower())
    if threat_name:
        return {
            "status": "known_malicius",
            "hash": file_hash,
            "threat_name": threat_name
        }
    return {
        "status": "clean",
        "hash": file_hash,
        "message": "El hash no fue encontrado en la base de datos de amenazas."
    }
# Endpoint para verificar si un hash de archivo es malicioso.
@app.get("/api/lookup/hash/{file_hash}", status_code=status.HTTP_200_OK)
def lookup_hash(file_hash: str):
    """
    Busca un hash de archivo (MD5, SHA1, SHA256) en la base de datos de amenazas.
    """
    threat_name = KNOWN_MALWARE_HASHES.get(file_hash.lower())
    
    if threat_name:
        return {
            "status": "known_malicious",
            "hash": file_hash,
            "threat_name": threat_name
        }
    
    return {
        "status": "clean",
        "hash": file_hash,
        "message": "El hash no fue encontrado en la base de datos de amenazas."
    }
