#!/bin/bash

/opt/bitnami/mysql/bin/mysql -u ${MYSQL_USER} -D ${MYSQL_DATABASE} -p${MYSQL_PASSWORD} <<EOF
CREATE TABLE tg_websites (
    website_id  int NOT NULL AUTO_INCREMENT,
    name        varchar(255),
    url         varchar(255),
  PRIMARY KEY (website_id )
);

CREATE TABLE tg_gtmetrix_scans (
   gtmetrix_id  int NOT NULL AUTO_INCREMENT,
   website_id   int(255),
   date         varchar(255),
   yslow        int(255),
   num_requests int(255),
   page_size    int(255),
   wait_time    int(255),
   connect_time int(255),
   css_size     int(255),
   css_time     int(255),
   js_size      int(255),
   js_time      int(255),
   image_size   int(255),
   Image_time   int(255),
   report_url   int(255),
   PRIMARY KEY (gtmetrix_id) 
);
INSERT INTO tg_websites (name,url) VALUES (
    '{$TG_WEBSITE_NAME}',
    '${TG_WEBSITE_URL}')
EOF
