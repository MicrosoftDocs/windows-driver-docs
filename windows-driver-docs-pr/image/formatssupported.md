---
title: FormatsSupported Element
description: The required FormatsSupported element is a collection of elements that list the document file formats that the scanner supports.
keywords: ["FormatsSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FormatsSupported
api_type:
- Schema
ms.date: 04/25/2023
---

# FormatsSupported element

The required **FormatsSupported** element is a collection of elements that list the document file formats that the scanner supports.

## Usage

```xml
<wscn:FormatsSupported>
  child elements
</wscn:FormatsSupported>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**FormatValue**](formatvalue.md) |

## Parent elements

| Element |
|--|
| [**DeviceSettings**](devicesettings.md) |

## Remarks

Each [**FormatValue**](formatvalue.md) element specifies a file format that describes both the file type and compression type.

## See also

[**DeviceSettings**](devicesettings.md)

[**FormatValue**](formatvalue.md)
