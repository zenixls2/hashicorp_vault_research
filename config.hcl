storage "raft" {
  path = "./vault/data"
  node_id = "node1"
}

listener "tcp" {
  address = "127.0.0.1:8200"
  tls_disable = "false"
  tls_cert_file = "/home/zenix/src/vault_config/certificate.crt"
  tls_key_file = "/home/zenix/src/vault_config/private.key"
}

api_addr = "https://127.0.0.1:8200"
cluster_addr = "https://127.0.0.1:8201"
ui = true
