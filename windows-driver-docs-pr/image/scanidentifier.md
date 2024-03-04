---
title: ScanIdentifier Element
description: The required ScanIdentifier element contains a device-specific string that the scanner provides through a ScanAvailableEvent event.
keywords: ["ScanIdentifier element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanIdentifier
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanIdentifier element

The required **ScanIdentifier** element contains a device-specific string that the scanner provides through a [**ScanAvailableEvent**](scanavailableevent.md) event.

## Usage

```xml
<wscn:ScanIdentifier>
  text
</wscn:ScanIdentifier>
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
| [**ScanAvailableEvent**](scanavailableevent.md) |

## Remarks

The client can send the **ScanIdentifier** element to the WSD Scan Service in a [**CreateScanJobRequest**](createscanjobrequest.md) operation element. The WSD Scan Service can use **ScanIdentifier** to ensure that the correct client is requesting the scan after a user has selected the destination.

The **ScanIdentifier** value must be unique for every [**ScanAvailableEvent**](scanavailableevent.md) instance.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**ScanAvailableEvent**](scanavailableevent.md)
