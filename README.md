SandyChargeAllTheThings
=======================

Helping connect people that still have power with those that dont so people can keep their phone charged and stay in touch with loved ones and emergency services. Concept: Chargins Points for phones and laptops: Wanted, Offered, Received on a Map with realtime collaboration

geoJSON Map Layers (static)
---------------------------
https://maps.google.com/maps/ms?ie=UTF8&authuser=0&msa=0&output=kml&msid=208094071398215428671.0004cd3cf2b712e2b42f0&foo=bar
converted using http://ogre.adc4gis.com/
to: PowerOutageMaps.js (geoJSON)

geoJSON Map Layers (dynamic)
----------------------------
TODO: There will be a layer populated by people who submit the human.io forms.

Suggested Implementation:
*human.io to ask for submissions / contributions from people.
*pubnub to push updates from the client to the dB
*mongoDB to store crowd-source POIs
*leaflet.js

References
----------
http://www.geojson.org/

http://leafletjs.com/

http://human.io/docs/python

http://ogre.adc4gis.com/
