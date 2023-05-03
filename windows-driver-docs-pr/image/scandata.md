---
title: ScanData element
description: The required ScanData element contains the binary data that represents the scanned image.
keywords: ["ScanData element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanData
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanData element

The required **ScanData** element contains the binary data that represents the scanned image.

## Usage

```xml
<wscn:ScanData/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**RetrieveImageResponse**](retrieveimageresponse.md) |

## Remarks

The **ScanData** element contains an **xop:Include** element that specifies the location of the scan data relative to the SOAP Envelope/Body of a [**RetrieveImageResponse**](retrieveimageresponse.md) operation element. The actual scan data is appended to the SOAP Envelope/Body as a binary attachment.

## See also

[**RetrieveImageResponse**](retrieveimageresponse.md)
