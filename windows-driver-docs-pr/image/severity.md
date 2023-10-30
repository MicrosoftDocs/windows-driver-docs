---
title: Severity element
description: The required Severity element specifies the severity level of the current DeviceCondition or ConditionHistoryEntry element.
keywords: ["Severity element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Severity
api_type:
- Schema
ms.date: 09/28/2021
---

# Severity element

The required **Severity** element specifies the severity level of the current [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element.

## Usage

```xml
<wscn:Severity>
  text
</wscn:Severity>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| Informational | This condition is purely for user information and has no noticeable effect on the image acquisition process. |
| Warning | This condition is not currently affecting processing, but the condition might become Critical if it is not attended to. |
| Critical | The device cannot continue processing until this condition is resolved. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ConditionHistoryEntry**](conditionhistoryentry.md) |
| [**DeviceCondition**](devicecondition.md) |

## Remarks

The WSD Scan Service determines the **Severity** level that is assigned to each error condition.

You can both extend and subset the allowed values for this element.

## See also

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)
