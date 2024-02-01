---
title: ClearTime Element
description: The required ClearTime element specifies the time at which a condition was cleared.
keywords: ["ClearTime element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ClearTime
api_type:
- Schema
ms.date: 03/28/2023
---

# ClearTime element

The required **ClearTime** element specifies the time at which a condition was cleared.

## Usage

```xml
<wscn:ClearTime>
  text
</wscn:ClearTime>
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

## Remarks

The specified time is according to the internal clock of the scanner.

## See also

[**ConditionHistoryEntry**](conditionhistoryentry.md)
