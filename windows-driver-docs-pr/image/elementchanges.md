---
title: ElementChanges Element
description: The required ElementChanges element contains the changes to the ScannerDescription, ScannerConfiguration, DefaultScanTicket, and vendor-extended elements.
keywords: ["ElementChanges element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ElementChanges
api_type:
- Schema
ms.date: 04/24/2023
---

# ElementChanges element

The required **ElementChanges** element contains the changes to the [**ScannerDescription**](scannerdescription.md), [**ScannerConfiguration**](scannerconfiguration.md), [**DefaultScanTicket**](defaultscanticket.md), and vendor-extended elements.

## Usage

```xml
<wscn:ElementChanges>
  child elements
</wscn:ElementChanges>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DefaultScanTicket**](defaultscanticket.md) |
| [**ScannerConfiguration**](scannerconfiguration.md) |
| [**ScannerDescription**](scannerdescription.md) |

## Parent elements

| Element |
|--|
| [**ScannerElementsChangeEvent**](scannerelementschangeevent.md) |

## Remarks

The WSD Scan Service must include an **ElementChanges** element when it generates a [**ScannerElementsChangeEvent**](scannerelementschangeevent.md) element. Each child element of **ElementChanges** must contain all of its required child elements. If an optional element is missing from the returned XML, the WSD Scan Service is indicating to the client that the service no longer supports that element.

## See also

[**DefaultScanTicket**](defaultscanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElementsChangeEvent**](scannerelementschangeevent.md)
