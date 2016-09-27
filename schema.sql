{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red37\green37\blue37;\red234\green234\blue234;\red0\green0\blue0;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 CREATE TABLE nodes(
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\fi960\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 id INT PRIMARY KEY NOT NULL,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 lat FLOAT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 lon FLOAT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 user TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 uid INT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 version INT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 changeset INT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 timestamp TEXT
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 );
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl280\partightenfactor0
\cf4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 CREATE TABLE node_tags(
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\fi960\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 id INT REFERENCES nodes,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 key TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 value TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 type TEXT
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 );
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl280\partightenfactor0
\cf4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 CREATE TABLE ways(
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\fi960\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 id INT PRIMARY KEY NOT NULL,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 user TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 uid INT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 version TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 changeset INT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 timestamp TEXT
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 );
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl280\partightenfactor0
\cf4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 CREATE TABLE way_tags(
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\fi960\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 id INT REFERENCES ways,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 key TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 value TEXT,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 type TEXT
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 );
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl280\partightenfactor0
\cf4 \
\pard\pardeftab720\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 CREATE TABLE way_nodes(
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\fi960\sl360\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 id INT REFERENCES ways,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 node_id INT REFERENCES nodes,
\fs24 \cf4 \cb1 \strokec4 \

\fs26 \cf2 \cb3 \strokec2 position INT
\fs24 \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl300\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 );}