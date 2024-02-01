---
title: FilmScanModesSupported Element
description: The required FilmScanModesSupported element contains a list of film exposure types that the film scanning option supports.
keywords: ["FilmScanModesSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmScanModesSupported
api_type:
- Schema
ms.date: 04/25/2023
---

# FilmScanModesSupported element

The required **FilmScanModesSupported** element contains a list of film exposure types that the film scanning option supports.

## Usage

```xml
<wscn:FilmScanModesSupported>
  child elements
</wscn:FilmScanModesSupported>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**FilmScanModeValue**](filmscanmodevalue.md) |

## Parent elements

| Element |
|--|
| [**Film**](film.md) |

## Remarks

The **FilmScanModesSupported** element contains one or more [**FilmScanModeValue**](filmscanmodevalue.md) child elements. Each **FilmScanModeValue** element identifies a film exposure type that the film scanning option supports.

## See also

[**Film**](film.md)

[**FilmScanModeValue**](filmscanmodevalue.md)
