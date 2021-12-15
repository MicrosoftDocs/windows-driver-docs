---
title: ContentType element
description: The optional ContentType element specifies the main characteristics of the original document.
keywords: ["ContentType element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContentType wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/09/2020
---

# ContentType element

The optional **ContentType** element specifies the main characteristics of the original document.

## Usage

```xml
<wscn:ContentType wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ContentType wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| MustHonor | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |
| Override | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |
| UsedDefault | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |

## Text value

Required. One of the following values:

|Term  |Description  |
|---------|---------|
|Auto     |      The scan device will automatically detect the original type.   |
|Text     |     he document is mainly composed of distinct text that contrasts strongly with the background.    |
|Photo     |     The original is mainly composed of photographic images, where shades change gradually and edges are not distinct.    |
|Halftone     |   The original is mainly composed of halftoned images.      |
|Mixed     |     A multipage document with characteristics of more than one specific DocumentType.    |

You can both extend and subset values for this element.

## Child elements

There are no child elements.

## Parent elements

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

## Remarks

The client can specify the optional **MustHonor** attribute only when the **ContentType** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ContentType** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)
