---
title: ContentTypesSupported element
description: The required ContentTypesSupported element contains a list of keywords that describe the different document content types that the scanner supports.
keywords: ["ContentTypesSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ContentTypesSupported
api_type:
- Schema
ms.date: 03/29/2023
---

# ContentTypesSupported element

The required **ContentTypesSupported** element contains a list of keywords that describe the different document content types that the scanner supports.

## Usage

```xml
<wscn:ContentTypesSupported>
  child elements
</wscn:ContentTypesSupported>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ContentTypeValue**](contenttypevalue.md) |

## Parent elements

| Element |
|--|
| [**DeviceSettings**](devicesettings.md) |

## Remarks

Each [**ContentTypeValue**](contenttypevalue.md) element that is listed in a **ContentTypesSupported** element describes the main characteristics of the original document. The client will pick one content type for its [**ScanTicket**](scanticket.md) from this list when initiating a scan.

## See also

[**ScanTicket**](scanticket.md)
