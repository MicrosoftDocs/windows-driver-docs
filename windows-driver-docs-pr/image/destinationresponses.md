---
title: DestinationResponses Element
description: The required DestinationResponses element is a collection of all of the responses to a client's scan destination requests.
keywords: ["DestinationResponses element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DestinationResponses
api_type:
- Schema
ms.date: 04/21/2023
---

# DestinationResponses element

The required **DestinationResponses** element is a collection of all of the responses to a client's scan destination requests.

## Usage

```xml
<wscn:DestinationResponses>
  child elements
</wscn:DestinationResponses>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DestinationResponse**](destinationresponse.md) |

## Parent elements

| Element |
|--|
| &lt;wse:SubscribeResponse&gt; |

## Remarks

A WSD Scan Service must specify one [**DestinationResponse**](destinationresponse.md) child element in a **DestinationResponses** element for each [**ScanDestination**](scandestination.md) element that a client specifies in a **&lt;wse:Subscribe&gt;** request. The **&lt;wse:Subscribe&gt;** element is described in the specification.

## See also

[**DestinationResponse**](destinationresponse.md)

[**ScanDestination**](scandestination.md)
