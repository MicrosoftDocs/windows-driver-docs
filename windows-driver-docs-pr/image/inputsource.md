---
title: InputSource element
description: The optional InputSource element specifies the source of the original document on the scanning device.
keywords: ["InputSource element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn InputSource wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 09/27/2021
---

# InputSource element

The optional **InputSource** element specifies the source of the original document on the scanning device.

## Usage

```xml
<wscn:InputSource wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:InputSource wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |
| **Override** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |
| **UsedDefault** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true. |

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| ADF | The document should be delivered by a document feeding device, scanning only the front side of each page. |
| ADFDuplex | The document should be delivered by a document feeding device, scanning both sides of each page. |
| Film | The document should be scanned by using the film scanning option. |
| Platen | The document should be scanned from the scanner platen. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The client can specify the optional **MustHonor** attribute only when the **InputSource** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **InputSource** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can both extend and subset the allowed values for this element.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)
