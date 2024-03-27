---
title: Time Element
description: The required Time element specifies the time at which a condition occurred.
keywords: ["Time element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Time
api_type:
- Schema
ms.date: 05/02/2023
---

# Time element

The required **Time** element specifies the time at which a condition occurred.

## Usage

```xml
<wscn:Time>
  text
</wscn:Time>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid value for the dateTime type. For more information about dateTime, see XML Schema Part 2: Datatypes Second Edition.**dateTimedateTime**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ConditionHistoryEntry**](conditionhistoryentry.md) |
| [**DeviceCondition**](devicecondition.md) |

## Remarks

The specified **Time** is according to the internal clock of the scanner.

## See also

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)
