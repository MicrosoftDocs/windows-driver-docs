---
title: DeviceConditionCleared Element
description: The required DeviceConditionCleared element contains information about a previously reported DeviceCondition condition that has been cleared.
keywords: ["DeviceConditionCleared element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DeviceConditionCleared
api_type:
- Schema
ms.date: 04/21/2023
---

# DeviceConditionCleared element

The required **DeviceConditionCleared** element contains information about a previously reported [**DeviceCondition**](devicecondition.md) condition that has been cleared.

## Usage

```xml
<wscn:DeviceConditionCleared>
  child elements
</wscn:DeviceConditionCleared>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ConditionClearTime**](conditioncleartime.md) |
| [**ConditionId**](conditionid.md) |

## Parent elements

| Element |
|--|
| [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) |

## Remarks

The **DeviceConditionCleared** element contains the [**ConditionId**](conditionid.md) and [**ConditionClearTime**](conditioncleartime.md) elements, which specify the condition identifier and time at which the condition was cleared, respectively. The WSD Scan Service sends the **DeviceConditionCleared** element to a client in a [**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md) event element.

## See also

[**ConditionClearTime**](conditioncleartime.md)

[**ConditionId**](conditionid.md)

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)
