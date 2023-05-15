---
title: ImageInformation element
description: The required ImageInformation element contains information about the resulting image data from a scan made with a ScanTicket element that is currently being validated.
keywords: ["ImageInformation element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ImageInformation
api_type:
- Schema
ms.date: 04/25/2023
---

# ImageInformation element

The required **ImageInformation** element contains information about the resulting image data from a scan made with a [**ScanTicket**](scanticket.md) element that is currently being validated.

## Usage

```xml
<wscn:ImageInformation>
  child elements
</wscn:ImageInformation>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**MediaBackImageInfo**](mediabackimageinfo.md) |
| [**MediaFrontImageInfo**](mediafrontimageinfo.md) |

## Parent elements

| Element |
|--|
| [**CreateScanJobResponse**](createscanjobresponse.md) |
| [**ValidationInfo**](validationinfo.md) |

## Remarks

The WSD Scan Service returns the **ImageInformation** element through the [**CreateScanJobResponse**](createscanjobresponse.md) operation element. Scan applications can use the data that is specified within **ImageInformation** to decode the image within an image file.

## See also

[**CreateScanJobResponse**](createscanjobresponse.md)

[**MediaBackImageInfo**](mediabackimageinfo.md)

[**MediaFrontImageInfo**](mediafrontimageinfo.md)

[**ValidationInfo**](validationinfo.md)
