---
title: JobElements element
description: The required JobElements element contains all of the job-related elements that a client requests through a call to GetJobElementsRequest.
keywords: ["JobElements element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobElements
api_type:
- Schema
ms.date: 04/28/2023
---

# JobElements element

The required **JobElements** element contains all of the job-related elements that a client requests through a call to [**GetJobElementsRequest**](getjobelementsrequest.md).

## Usage

```xml
<wscn:JobElements>
  child elements
</wscn:JobElements>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ElementData for parent JobElements**](elementdata-for-jobelements-element.md) |

## Parent elements

| Element |
|--|
| [**GetJobElementsResponse**](getjobelementsresponse.md) |

## Remarks

The WSD Scan Service returns the **JobElements** element in [**GetJobElementsResponse**](getjobelementsresponse.md).

## See also

[**ElementData for parent JobElements**](elementdata-for-jobelements-element.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetJobElementsResponse**](getjobelementsresponse.md)
