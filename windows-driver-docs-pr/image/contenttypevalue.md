---
title: ContentTypeValue Element
description: The required ContentTypeValue element specifies one document content type that the scan device supports.
keywords: ["ContentTypeValue element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ContentTypeValue
api_type:
- Schema
ms.date: 03/29/2023
---

# ContentTypeValue element

The required **ContentTypeValue** element specifies one document content type that the scan device supports.

## Usage

```xml
<wscn:ContentTypeValue>
  text
</wscn:ContentTypeValue>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| Auto | The device will automatically detect the original document type. |
| Text | The original document is composed of distinct text that contrasts strongly with the background. |
| Photo | The original document is composed of photographic images, where shades change gradually and edges aren't distinct. |
| Halftone | The original is composed of halftoned images. |
| Mixed | The original document is a multi-page document with characteristics of more than one specific document content type. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ContentTypesSupported**](contenttypessupported.md) |

## Remarks

You can both extend and subset the allowed values for this element.

## See also

[**ContentTypesSupported**](contenttypessupported.md)
