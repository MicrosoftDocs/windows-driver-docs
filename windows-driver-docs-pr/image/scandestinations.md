---
title: ScanDestinations Element
description: The required ScanDestinations element is a collection of all of the scan destinations that a client wants to register with the scan device.
keywords: ["ScanDestinations element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanDestinations
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanDestinations element

The required **ScanDestinations** element is a collection of all of the scan destinations that a client wants to register with the scan device.

## Usage

```xml
<wscn:ScanDestinations>
  child elements
</wscn:ScanDestinations>
```

## Attributes

There are no attributes.

## Text value

None

## Child elements

| Element |
|--|
| [**ScanDestination**](scandestination.md) |

## Parent elements

| Element |
|--|
| &lt;wse:Subscribe&gt; |

## Remarks

The client must send the **ScanDestinations** element in the **&lt;wse:Subscribe&gt;** request operation element to register one or more scan destinations with the WSD Scan Service. The client subscribes during client setup before obtaining scan ticket information from the WSD Scan Service. The **&lt;wse:Subscribe&gt;** element is defined in the specification.

The **ScanDestinations** element give clients the flexibility to register for multiple unique scan destinations at once.

## See also

[**ScanDestination**](scandestination.md)
