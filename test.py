import hvac
import sys

client = hvac.Client(
    url="https://127.0.0.1:8200",
    cert=("./certificate.crt", "./private.key"),
    #token="hvs.Vvc4rAgiOaOJXRRDcgdDN86G",
    #token="hvs.CAESIIRGLMZsa6jdnN_CYRAGlwyFoViVohAqQKyPDNeoymNVGh4KHGh2cy55RzAyRHVVQkdkeWV5b0xnQUpMb1M1TUM",
    token="hvs.CAESILRapb-0vBtIW9OITqFiePOq8GYBaAB6WyZgAhekAd4YGh4KHGh2cy5acTI5YzhpMm9uUjNSbGxHaTh4cWJtNGM",
    verify="./certificate.crt")
print(client.is_authenticated())
#client.secrets.kv.v2.create_or_update_secret('binance', secret=dict(apikey='1234', apitoken='4567'))
read_response = client.secrets.kv.read_secret_version(path="binance")
print(read_response)
