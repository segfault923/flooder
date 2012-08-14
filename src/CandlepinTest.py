import logging
import rhsm.connection as connection

class CandlepinTest():

    def __init__(self,
                 host=None, 
                 ssl_port=None, 
                 server_prefix=None,
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

        self.cp = connection.UEPConnection(host=server_hostname,
                                           ssl_port=server_port,
                                           handler=server_prefix,
                                           cert_file=cert_file, key_file=key_file,
                                           proxy_hostname=proxy_hostname,
                                           proxy_port=proxy_port,
                                           proxy_user=proxy_user,
                                           proxy_password=proxy_password,
                                           username=username,
                                           password=password)

    def register(self,
                 name=None,
                 type=None,
                 facts=None,
                 owner_key=None,
                 environment_id=None,
                 activation_keys=None,
                 installed_products=None):
        
        consumername = name or 'test_system'
        consumertype = type or 'system'  
        consumerfacts = facts or {}

        logging.info('Registering consumer\n')
        self.cp.registerConsumer(name=consumername,
                                 type=consumertype,
                                 facts=consumerfacts,
                                 owner=owner_key,
                                 environment=environment_id,
                                 keys=activation_keys,
                                 installed_products=installed_products)

    def subscribe(self):
        logging.info('Subscribing consumer\n')
