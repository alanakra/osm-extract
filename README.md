# MATRIMOINE PROJECT - EXTRACTING DATA FROM OPENSTREETMAP (VIA GEODATAMINE)

This repo contains a script for extracting named places from OpenStreetMap using [GeoDataMine](https://geodatamine.fr/) and converting them into a Python Dictionary of Tuples.

Extract from a CSV file input

``` csv
    2.7439253;48.4342121998324;node/2890030601;sports_centre;ANFA - Aviron du Pays de Fontainebleau;;rowing;;;"77441";Samois-sur-Seine
```

Extract from a Python file output

``` python
    {
        ('ANFA - Aviron du Pays de Fontainebleau', 77441, 'Samois-sur-Seine')
    }
```