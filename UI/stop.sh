#!/bin/bash
Solr/solr-9.0.0/bin/solr delete -c swisstour
Solr/solr-9.0.0/bin/solr delete -c getyourguide
Solr/solr-9.0.0/bin/solr delete -c viator
Solr/solr-9.0.0/bin/solr stop -all