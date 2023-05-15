---
title: Resolution element
description: The optional Resolution element specifies the resolution of the scanned image.
keywords: ["Resolution element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Resolution wscn MustHonor ""
api_type:
- Schema
ms.date: 05/01/2023
---

# Resolution element

The optional **Resolution** element specifies the resolution of the scanned image.

## Usage

```xml
<wscn:Resolution wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Resolution wscn:MustHonor="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Child elements

| Element |
|--|
| [**Height**](height.md) |
| [**Width**](width.md) |

## Parent elements

| Element |
|--|
| [**MediaBack**](mediaback.md) |
| [**MediaFront**](mediafront.md) |

## Remarks

The **Resolution** element contains a single [**Width**](width.md) x [**Height**](height.md) pair that describes the desired scan resolution. If the **Height** element is missing, the **Width** value is used, yielding a square resolution (for example, 300 x 300).

**Resolution** values are in pixels per inch.

The client can specify the optional **MustHonor** attribute only when the **Resolution** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**Height**](height.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**Width**](width.md)
