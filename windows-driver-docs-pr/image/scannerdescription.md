---
title: ScannerDescription Element
description: ScannerDescription element
keywords: ["ScannerDescription element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerDescription
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerDescription element

## Usage

```xml
<wscn:ScannerDescription>
  child elements
</wscn:ScannerDescription>
```

## Attributes

There are no attributes.

## Text value

None

## Child elements

| Element |
|--|
| [**ScannerInfo**](scannerinfo.md) |
| [**ScannerLocation**](scannerlocation.md) |
| [**ScannerName**](scannername.md) |

## Parent elements

| Element |
|--|
| [**ElementChanges**](elementchanges.md) |
| [**ElementData for parent ScannerElements**](elementdata-for-scannerelements-element.md) |

## Remarks

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The **ScannerDescription** element contains information about the scanner that rarely or never changes. A client retrieves this information by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation element.

## See also

[**ElementChanges**](elementchanges.md)

[**ElementData for parent ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerInfo**](scannerinfo.md)

[**ScannerLocation**](scannerlocation.md)

[**ScannerName**](scannername.md)
