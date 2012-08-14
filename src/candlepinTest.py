import rhsm.connection as connection

def register(host=None, 
             ssl_port=None, 
             cert_file=None, 
             key_file=None,
             proxy_hostname=None, 
             proxy_port=None, 
             proxy_user=None, 
             proxy_password=None, 
             username=None, 
             password=None):

    server_hostname = host
    server_port = ssl_port or 443

    cp = connection.UEPConnection(host=server_hostname,
                                  ssl_port=server_port,
                                  handler=server_prefix,
                                  cert_file=cert_file, key_file=key_file,
                                  proxy_hostname=proxy_hostname,
                                  proxy_port=proxy_port,
                                  proxy_user=proxy_user,
                                  proxy_password=proxy_password,
                                  username=username,
                                  password=password)

def subscribe():
    pass
