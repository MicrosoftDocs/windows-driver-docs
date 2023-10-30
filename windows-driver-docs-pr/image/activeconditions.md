---
title: ActiveConditions element
description: The required ActiveConditions element is a collection of all of the currently active conditions or errors on the scan device.
keywords: ["ActiveConditions element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ActiveConditions
api_type:
- Schema
ms.date: 03/27/2023
---

# ActiveConditions element

The required **ActiveConditions** element is a collection of all of the currently active conditions or errors on the scan device.

## Usage

```xml
<wscn:ActiveConditions>
  child elements
</wscn:ActiveConditions>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DeviceCondition**](devicecondition.md) |

## Parent elements

| Element |
|--|
| [**ScannerStatus**](scannerstatus.md) |

## Remarks

The **ActiveConditions** element is a list of [**DeviceCondition**](devicecondition.md) elements that describe all of the currently active conditions or errors in the device. Device conditions can vary in severity from informational to critical.

## See also

[**DeviceCondition**](devicecondition.md)

[**ScannerStatus**](scannerstatus.md)
