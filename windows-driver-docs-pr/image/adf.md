---
title: ADF Element
description: The optional ADF element describes the capabilities of the automatic document feeder (ADF) that is attached to the scanner.
keywords: ["ADF element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADF
api_type:
- Schema
ms.date: 03/27/2023
---

# ADF element

The optional **ADF** element describes the capabilities of the automatic document feeder (ADF) that is attached to the scanner.

## Usage

```xml
<wscn:ADF>
  child elements
</wscn:ADF>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ADFBack**](adfback.md) |
| [**ADFFront**](adffront.md) |
| [**ADFSupportsDuplex**](adfsupportsduplex.md) |

## Parent elements

| Element |
|--|
| [**ScannerConfiguration**](scannerconfiguration.md) |

## Remarks

If the scan device has an ADF, the WSD Scan Service must provide configuration information for all **ADF** child elements.

## See also

[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ADFSupportsDuplex**](adfsupportsduplex.md)

[**ScannerConfiguration**](scannerconfiguration.md)
