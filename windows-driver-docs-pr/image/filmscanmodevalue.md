---
title: FilmScanModeValue element
description: The required FilmScanModeValue element identifies a specific film exposure type that the film scanning option supports.
keywords: ["FilmScanModeValue element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FilmScanModeValue
api_type:
- Schema
ms.date: 09/27/2021
---

# FilmScanModeValue element

The required **FilmScanModeValue** element identifies a specific film exposure type that the film scanning option supports.

## Usage

```xml
<wscn:FilmScanModeValue>
  text
</wscn:FilmScanModeValue>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| NotApplicable | The default scan input source is no longer the film option; therefore, FilmScanModeValue is no longer an applicable value for the DefaultScanTicket element. NotApplicable is valid only in a DefaultScanTicket element. |
| ColorSlideFilm | Film images are in the normal color space. |
| ColorNegativeFilm | Film images are negatives of the normal color space. |
| BlackandWhiteNegativeFilm | Film images are black and white negatives of the captured images. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**FilmScanModesSupported**](filmscanmodessupported.md) |

## Remarks

You can both extend and subset the allowed values for this element.

## See also

[**DefaultScanTicket**](defaultscanticket.md)

[**FilmScanModesSupported**](filmscanmodessupported.md)
