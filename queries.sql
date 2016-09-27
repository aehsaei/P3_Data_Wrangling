{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red148\green6\blue75;\red245\green245\blue245;\red38\green38\blue38;
\red14\green114\blue164;\red19\green36\blue126;\red0\green0\blue0;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl460\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  (\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 UNION ALL\cf4 \strokec4  \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  way_tags) tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 key\cf2 \strokec2 =\cf6 \strokec6 'postcode'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 5\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  (\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 UNION ALL\cf4 \strokec4  \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  way_tags) tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 key\cf2 \strokec2 =\cf6 \strokec6 'street'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 5\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 user\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  nodes\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 uid\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 5\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 user\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  ways\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 uid\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 5\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  (\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 UNION ALL\cf4 \strokec4  \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  way_tags) tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 key\cf2 \strokec2 =\cf6 \strokec6 'religion'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 10\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  (\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 UNION ALL\cf4 \strokec4  \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  way_tags) tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 key\cf2 \strokec2 =\cf6 \strokec6 'amenity'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 10\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \strokec4 , \cf5 \strokec5 COUNT\cf4 \strokec4 (\cf2 \strokec2 *\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  count \cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  (\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 UNION ALL\cf4 \strokec4  \cb1 \uc0\u8232 \cb3  \'a0\'a0\'a0\'a0\'a0\cf2 \strokec2 SELECT\cf4 \strokec4  \cf2 \strokec2 *\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  way_tags) tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 key\cf2 \strokec2 =\cf6 \strokec6 'highway'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  \cf5 \strokec5 tags\cf4 \strokec4 .\cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  count \cf2 \strokec2 DESC LIMIT 10\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 COUNT(*) as count\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  way_tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  key\cf2 \strokec2 =\cf6 \strokec6 'bicycle' and \cf4 \strokec4 value=\cf6 \strokec6 '\cf4 \strokec4 yes\cf6 \strokec6 '\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  key, \cf5 \strokec5 value\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  value, \cf5 \strokec5 COUNT(*) as count\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  node_tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  key\cf2 \strokec2 =\cf6 \strokec6 'natural'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  value
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf4 \cb3 \strokec4 ORDER BY count DESC LIMIT 10;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  id, value\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  node_tags\cb1 \uc0\u8232 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  key\cf2 \strokec2 =\cf6 \strokec6 'ele'\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 GROUP BY\cf4 \strokec4  id
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf4 \cb3 \strokec4 ORDER BY value DESC LIMIT 5;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf2 \cb3 \strokec2 SELECT\cf4 \strokec4  id, \cf5 \strokec5 value\cf4 \cb1 \strokec4 \uc0\u8232 \cf2 \cb3 \strokec2 FROM\cf4 \strokec4  node_tags 
\fs24 \cf7 \cb1 \strokec7 \

\fs26 \cf2 \cb3 \strokec2 WHERE\cf4 \strokec4  id IN (SELECT id FROM node_tags WHERE key\cf2 \strokec2 =\cf6 \strokec6 'natural' AND value='peak') AND key='ele'
\fs24 \cf7 \cb1 \strokec7 \

\fs26 \cf2 \cb3 \strokec2 ORDER BY\cf4 \strokec4  value \cf2 \strokec2 DESC LIMIT 10\cf4 \strokec4 ;
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
\pard\pardeftab720\sl460\partightenfactor0

\fs26 \cf4 \cb3 \strokec4 SELECT id, value
\fs24 \cf7 \cb1 \strokec7 \

\fs26 \cf4 \cb3 \strokec4 FROM node_tags
\fs24 \cf7 \cb1 \strokec7 \

\fs26 \cf4 \cb3 \strokec4 WHERE id IN ( \cf2 \strokec2 SELECT\cf4 \strokec4  \cf5 \strokec5 id\cf4 \strokec4  \cf2 \strokec2 FROM\cf4 \strokec4  node_tags \cf2 \strokec2 WHERE\cf4 \strokec4  id IN (SELECT id FROM node_tags WHERE key\cf2 \strokec2 =\cf6 \strokec6 'natural' AND value='peak') AND key='ele' \cf2 \strokec2 ORDER BY\cf4 \strokec4  value \cf2 \strokec2 DESC LIMIT 10 \cf4 \strokec4 ) AND
\fs24 \cf7 \cb1 \strokec7 \

\fs26 \cf4 \cb3 \strokec4 key=\cf6 \strokec6 'name'
\fs24 \cf7 \cb1 \strokec7 \
\pard\pardeftab720\sl280\partightenfactor0
\cf7 \
}