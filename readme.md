### Prepare

```bash
mkdir -p vault/data
```

Install: refer to https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install

Production deployment: refer to https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-deploy

You could refer to the `config.hcl` attached in this repo. It comes with the TLS script.

### Launch server

```bash
vault server -config=config.hcl
```

### Init

```bash
vault operator init
# check the init_info.txt to see the example output
```

Run the following command at least 3 times and put different Unseal keys:

```bash
vault operator unseal
```

### CLI Login:

```bash
vault login
# enter root token
```

### Bypass self-signed TLS cert in M$ edge:

https://stackoverflow.com/questions/62699391/how-to-bypass-certificate-errors-using-microsoft-edge

Also check the `create_key.sh`.

### Others

login to https://127.0.0.1:8200/ui/vault/secrets using root token
menu -> Secrets Engines -> Enable new engine -> KV -> Next -> Rename Path -> Enable Engine

Enable github:

```bash
vault auth enable github
vault write auth/github/config organization=tradingun
```

Add key-value:

```bash
vault kv put -mount=secret binance apikey=123 apitoken=456
```

Create default policy token

```bash
vault token create -policy=default
```

To use hvac, you need to at least create a "secret" kv inside the secrets engines menu.

Also for non-root policy users, add the following hcl to ACL policies:

```hcl
path "secret/*" {
    capabilities = ["create", "update", "read", "list"]
}
```
