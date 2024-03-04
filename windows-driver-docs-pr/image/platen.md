---
title: Platen Element
description: The optional Platen element describes the capabilities of the flatbed platen that is available on the scanner.
keywords: ["Platen element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Platen
api_type:
- Schema
ms.date: 05/01/2023
---

# Platen element

The optional **Platen** element describes the capabilities of the flatbed platen that is available on the scanner.

## Usage

```xml
<wscn:Platen>
  child elements
</wscn:Platen>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**PlatenColor**](platencolor.md) |
| [**PlatenMaximumSize**](platenmaximumsize.md) |
| [**PlatenMinimumSize**](platenminimumsize.md) |
| [**PlatenOpticalResolution**](platenopticalresolution.md) |
| [**PlatenResolutions**](platenresolutions.md) |

## Parent elements

| Element |
|--|
| [**ScannerConfiguration**](scannerconfiguration.md) |

## Remarks

If the scan device has a flatbed platen, the WSD Scan Service must provide configuration information for all **Platen** child elements.

## See also

[**PlatenColor**](platencolor.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**PlatenResolutions**](platenresolutions.md)

[**ScannerConfiguration**](scannerconfiguration.md)
