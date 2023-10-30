---
title: ConditionHistoryEntry element
description: The required ConditionHistoryEntry element provides details about one of the past conditions on the scanner.
keywords: ["ConditionHistoryEntry element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ConditionHistoryEntry wscn Id "..."
api_type:
- Schema
ms.date: 03/29/2023
---

# ConditionHistoryEntry element

The required **ConditionHistoryEntry** element provides details about one of the past conditions on the scanner.

## Usage

```xml
<wscn:ConditionHistoryEntry wscn:Id="..."
  Id = "xs:string">
  child elements
</wscn:ConditionHistoryEntry wscn:Id="...">
```

## Attributes

| Attribute  | Type      | Required | Description                                     |
|------------|-----------|----------|-------------------------------------------------|
| ****Id**** | xs:string | No       | Required. An integer from 1 through 2147483648. |

## Child elements

| Element |
|--|
| [**ClearTime**](cleartime.md) |
| [**Component**](component.md) |
| [**Name forParents DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md) |
| [**Severity**](severity.md) |
| [**Time**](time.md) |

## Parent elements

| Element |
|--|
| [**ConditionHistory**](conditionhistory.md) |

## Remarks

The WSD Scan Service specifies a unique identifier in the **Id** attribute for this **ConditionHistoryEntry** element. The client can use **Id**, along with the value of the [**Time**](time.md) element, to determine if an error condition is new or has gone away. The WSD Scan Service must not reuse the identifier for as long as possible. This delay ensures that clients can accurately keep track of individual **ConditionHistoryEntry** elements.

You cannot extend the allowed values for **Id**.

## See also

[**ClearTime**](cleartime.md)

[**Component**](component.md)

[**ConditionHistory**](conditionhistory.md)

[**DeviceCondition**](devicecondition.md)

[**Name forParents DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md)

[**Severity**](severity.md)

[**Time**](time.md)
