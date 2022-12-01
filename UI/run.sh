#!/bin/bash
Solr/solr-9.0.0/bin/solr start -c
Solr/solr-9.0.0/bin/solr create -c swisstour
Solr/solr-9.0.0/bin/solr create -c getyourguide
Solr/solr-9.0.0/bin/solr create -c viator
Solr/solr-9.0.0/bin/post -c swisstour CourseProject/CourseProject/crawls/swiss_tours.json
Solr/solr-9.0.0/bin/post -c getyourguide CourseProject/CourseProject/crawls/get_your_guide.json
Solr/solr-9.0.0/bin/post -c viator CourseProject/CourseProject/crawls/viator_las_vegas.json CourseProject/CourseProject/crawls/viator_netherlands_1.json CourseProject/CourseProject/crawls/viator_netherlands_2.json CourseProject/CourseProject/crawls/viator_paris.json CourseProject/CourseProject/crawls/viator_new_york.json
