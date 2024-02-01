---
title: ColorProcessing Element
description: The optional ColorProcessing element specifies the color-processing mode of the input source on the scanner.
keywords: ["ColorProcessing element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ColorProcessing wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 03/29/2023
---

# ColorProcessing element

The optional **ColorProcessing** element specifies the color-processing mode of the input source on the scanner.

## Usage

```xml
<wscn:ColorProcessing wscn:MustHonor=""                      wscn:Override=""                      wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ColorProcessing wscn:MustHonor=""                      wscn:Override=""                      wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

For a list and description of the color processing Modes, see ColorEntry.[**ColorEntry**](colorentry.md)

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**MediaFront**](mediafront.md) |

## Remarks

The client can specify the optional **MustHonor** attribute only when the **ColorProcessing** element is contained within a [**CreateScanJobRequest**](createscanjobrequest.md) hierarchy. For more information about **MustHonor** and its usage, see **CreateScanJobRequest**.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ColorProcessing** element is contained within a [**DocumentFinalParameters**](documentfinalparameters.md) hierarchy. For more information about **Override** and **UsedDefault** and their usage, see **DocumentFinalParameters**.

## See also

[**ColorEntry**](colorentry.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**MediaFront**](mediafront.md)
