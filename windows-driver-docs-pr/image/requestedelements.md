---
title: RequestedElements Element
description: The required RequestedElements element identifies the elements that the client wants data for when it calls GetScannerElementsRequest or GetJobElementsRequest.
keywords: ["RequestedElements element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn RequestedElements
api_type:
- Schema
ms.date: 05/01/2023
---

# RequestedElements element

The required **RequestedElements** element identifies the elements that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

## Usage

```xml
<wscn:RequestedElements>
  child elements
</wscn:RequestedElements>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Name for RequestedElements Element**](name-for-requestedelements-element.md) |

## Parent elements

| Element |
|--|
| [**GetJobElementsRequest**](getjobelementsrequest.md) |
| [**GetScannerElementsRequest**](getscannerelementsrequest.md) |

## Remarks

The **RequestedElements** element contains one or more **Name** elements for parent **RequestedElements** elements that identify the data that the client is querying.

## See also

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name for RequestedElements Element**](name-for-requestedelements-element.md)
