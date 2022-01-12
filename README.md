# symbiota-tooltips

[![Updates Terms Endpoints](https://github.com/arbolitoloco/symbiota-tooltips/actions/workflows/update-api-terms.yml/badge.svg)](https://github.com/arbolitoloco/symbiota-tooltips/actions/workflows/update-api-terms.yml) [![pages-build-deployment](https://github.com/arbolitoloco/symbiota-tooltips/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/arbolitoloco/symbiota-tooltips/actions/workflows/pages/pages-build-deployment)

## An open API to help document Symbiota tools and terms

This repository contains API endpoints where one can fetch short explanations about [Symbiota](https://symbiota.org/docs/) pages or terms in a portal.
The short explanations provided here (along with optional links when available) are integrated with [Symbiota](https://github.com/BioKIC/Symbiota) code, so that tooltips are available dynamically, on demand, in pages and terms throughout the interface.

Endpoints include language tags, so that the content can be delivered in the idiom used by the interface.

There are also links directing users to related resources, such as help guides and tutorials made available at the [Symbiota Docs](https://github.com/BioKIC/symbiota-docs) website.

Created with the [Open Static API Kit](https://github.com/arbolitoloco/static-api).

## Usage

Get a term tooltip:

```
curl -G https://laura.rochaprado.com/symbiota-tooltips/api/v<version number>/terms/<term_id>.json
```

For instance, get `Catalog Number` tooltip:

```
curl -G https://laura.rochaprado.com/symbiota-tooltips/api/v<version number>/terms/catalogNumber.json
```

Get a page tooltip:

```
curl -G https://laura.rochaprado.com/symbiota-tooltips/api/v<version number>/<path_to_page_file>/<pagefilename.php>.json
```

For instance, get `Taxonomic Tree Viewer` tooltip:

```
curl -G https://laura.rochaprado.com/api/taxa/taxonomy/taxonomydisplay.php.json
```

## Data

JSON endpoints are generated based on CSV files in the `data` folder.
