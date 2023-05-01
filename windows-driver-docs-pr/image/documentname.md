---
title: DocumentName element
description: The required DocumentName element contains the name of the document that the client supplies.
keywords: ["DocumentName element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DocumentName
api_type:
- Schema
ms.date: 04/24/2023
---

# DocumentName element

The required **DocumentName** element contains the name of the document that the client supplies.

## Usage

```xml
<wscn:DocumentName>
  text
</wscn:DocumentName>
```

## Attributes

There are no attributes.

## Text value

Required. Any character string.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentDescription**](documentdescription.md) |

## Remarks

The WSD Scan Service must supply a value to store the document on the client.

## See also

[**DocumentDescription**](documentdescription.md)
