---
title: ScanDestination Element
description: The required ScanDestination element specifies a single scan destination on the client.
keywords: ["ScanDestination element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanDestination
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanDestination element

The required **ScanDestination** element specifies a single scan destination on the client.

## Usage

```xml
<wscn:ScanDestination>
  child elements
</wscn:ScanDestination>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ClientContext**](clientcontext.md) |
| [**ClientDisplayName**](clientdisplayname.md) |

## Parent elements

| Element |
|--|
| [**ScanDestinations**](scandestinations.md) |

## Remarks

The client includes one or more **ScanDestination** elements within the **ScanDestinations** element that it sends when it creates a subscription. The WSD Scan Service uses the information that is provided within **ScanDestination** to create appropriate [**ScanAvailableEvent**](scanavailableevent.md) event elements.

## See also

[**ClientContext**](clientcontext.md)

[**ClientDisplayName**](clientdisplayname.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestinations**](scandestinations.md)
