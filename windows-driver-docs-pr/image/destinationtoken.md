---
title: DestinationToken element
description: The required DestinationToken element contains a device-specific string that the scanner assigns to the current client destination.
keywords: ["DestinationToken element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DestinationToken
api_type:
- Schema
ms.date: 04/21/2023
---

# DestinationToken element

The required **DestinationToken** element contains a device-specific string that the scanner assigns to the current client destination.

## Usage

```xml
<wscn:DestinationToken>
  text
</wscn:DestinationToken>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid character string.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**CreateScanJobRequest**](createscanjobrequest.md) |
| [**DestinationResponse**](destinationresponse.md) |

## Remarks

The client includes the **DestinationToken** token when it sends a [**CreateScanJobRequest**](createscanjobrequest.md) operation element after the [**ScanAvailableEvent**](scanavailableevent.md) event. The WSD Scan Service uses the specified string to check that the correct client is sending the scan request.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DestinationResponse**](destinationresponse.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)
