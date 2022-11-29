#!/bin/bash
Solr/solr-9.0.0/bin/solr start -c
Solr/solr-9.0.0/bin/solr create -c swisstour
Solr/solr-9.0.0/bin/solr create -c getyourguide
Solr/solr-9.0.0/bin/solr create -c viator
Solr/solr-9.0.0/bin/post -c swisstour test1/test1/switzerlandtours.json
Solr/solr-9.0.0/bin/post -c getyourguide test1/test1/getyourguide.json
Solr/solr-9.0.0/bin/post -c viator test1/test1/holland.json
