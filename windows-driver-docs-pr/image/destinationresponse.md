---
title: DestinationResponse Element
description: The required DestinationResponse element contains the response information for a single ScanDestination registration.
keywords: ["DestinationResponse element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DestinationResponse
api_type:
- Schema
ms.date: 04/21/2023
---

# DestinationResponse element

The required **DestinationResponse** element contains the response information for a single [**ScanDestination**](scandestination.md) registration.

## Usage

```xml
<wscn:DestinationResponse>
  child elements
</wscn:DestinationResponse>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| &lt;Any vendor-defined elements&gt; |
| [**ClientContext**](clientcontext.md) |
| [**DestinationToken**](destinationtoken.md) |

## Parent elements

| Element |
|--|
| [**DestinationResponses**](destinationresponses.md) |

## Remarks

The **DestinationResponse** element contains the [**ClientContext**](clientcontext.md) element from its matching [**ScanDestination**](scandestination.md) element so that the client can identify the response. **DestinationResponse** also contains a [**DestinationToken**](destinationtoken.md) element for use in all [**CreateScanJobRequest**](createscanjobrequest.md) operation elements from this destination.

## See also

[**ClientContext**](clientcontext.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DestinationResponses**](destinationresponses.md)

[**DestinationToken**](destinationtoken.md)

[**ScanDestination**](scandestination.md)
