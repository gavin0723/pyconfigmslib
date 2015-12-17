# encoding=utf8

""" The elasticsearch config section
    Author: lipixun
    Created Time : 一 12/ 7 10:44:19 2015

    File Name: _elasticsearch.py
    Description:

"""

import logging

from elasticsearch import Elasticsearch

from ..section import ReferConfigSection

esLogger = logging.getLogger('elasticsearch.trace')

DEFAULT_TIMEOUT = 30 * 1000     # 30s

class ElasticsearchConfigSection(ReferConfigSection):
    """The elasticsearch config section
    Known configs:
        - hosts                     (Required)A single host or a list of hosts
        - timeout                   The timeout in ms
    TODO:
        Add support to transport class and kwargs
    """
    TYPE = 'elasticsearch'

    logger = logging.getLogger('config.elasticsearch')

    def __reference__(self, config):
        """Get the referenced value
        """
        return self.createClientbyConfig(config)

    def __release__(self, value):
        """Release the value
        """
        pass

    @classmethod
    def createClientbyConfig(cls, config):
        """Create elasticsearch client by config
        """
        hosts = config['hosts']
        if isinstance(hosts, basestring):
            hosts = (hosts, )
        timeout = config.get('timeout', DEFAULT_TIMEOUT)
        cls.logger.info('Connecting to elasticsearch with hosts: %s timeout [%s]', hosts, timeout)
        # Create the client
        return Elasticsearch(hosts, timeout = float(timeout) / 1000.0)

