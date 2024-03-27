---
title: InputSize Element
description: The optional InputSize element specifies the size of the original scan media.
keywords: ["InputSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn InputSize wscn MustHonor ""
api_type:
- Schema
ms.date: 04/28/2023
---

# InputSize element

The optional **InputSize** element specifies the size of the original scan media.

## Usage

```xml
<wscn:InputSize wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:InputSize wscn:MustHonor="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Child elements

| Element |
|--|
| [**DocumentSizeAutoDetect**](documentsizeautodetect.md) |
| [**InputMediaSize**](inputmediasize.md) |

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The **InputSize** element can contain the [**DocumentSizeAutoDetect**](documentsizeautodetect.md) or [**InputMediaSize**](inputmediasize.md) element, but not both. **DocumentSizeAutoDetect** specifies that the device utomatically detects the size of the original page. **InputMediaSize** specifies the size of the media to be scanned for the current job.

The client can specify the optional **MustHonor** attribute only when the **InputSize** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**DocumentSizeAutoDetect**](documentsizeautodetect.md)

[**InputMediaSize**](inputmediasize.md)
