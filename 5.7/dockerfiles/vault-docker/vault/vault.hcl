storage "consul" {
    address = "0.0.0.0:8300"
    path = "/vault/data"
}
//backend "file" {
//    path = "/vault/data"
//}


listener "tcp" {
    address = "0.0.0.0:8200"
    cluster_addr = "http://0.0.0.1:8201"
    tls_disable = 1
}
disable_mlock = true