---
title: ClientDisplayName element
description: The required ClientDisplayName element specifies the string that the scanner should display in its user interface.
keywords: ["ClientDisplayName element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ClientDisplayName
api_type:
- Schema
ms.date: 03/28/2023
---

# ClientDisplayName element

The required **ClientDisplayName** element specifies the string that the scanner should display in its user interface.

## Usage

```xml
<wscn:ClientDisplayName>
  text
</wscn:ClientDisplayName>
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
| [**ScanDestination**](scandestination.md) |

## Remarks

The displayed name enables a user to select the requesting client as a scan destination. When the user chooses this display name and presses the scan button, the WSD Scan Service will send a [**ScanAvailableEvent**](scanavailableevent.md) event to the scan destination that subscribed to receive it.

## See also

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)
