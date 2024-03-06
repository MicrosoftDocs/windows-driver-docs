---
title: ConditionId Element
description: The required ConditionId element uniquely identifies the device condition that was cleared.
keywords: ["ConditionId element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ConditionId
api_type:
- Schema
ms.date: 03/29/2023
---

# ConditionId element

The required **ConditionId** element uniquely identifies the device condition that was cleared.

## Usage

```xml
<wscn:ConditionId>
  text
</wscn:ConditionId>
```

## Attributes

There are no attributes.

## Text value

Required. An integer value that is equivalent to the Id attribute of a previously reported DeviceCondition element.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DeviceConditionCleared**](deviceconditioncleared.md) |

## Remarks

The **ConditionId** element must be the **Id** attribute of a **DeviceCondition** element that the WSD Scan Service previously reported through [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md).

## See also

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)
