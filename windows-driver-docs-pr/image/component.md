---
title: Component element
description: The required Component element identifies the component that the current DeviceCondition or ConditionHistoryEntry element describes.
keywords: ["Component element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Component
api_type:
- Schema
ms.date: 03/29/2023
---

# Component element

The required **Component** element identifies the component that the current [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element describes.

## Usage

```xml
<wscn:Component>
  text
</wscn:Component>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

- ADF
- Film
- MediaPath
- Platen

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ConditionHistoryEntry**](conditionhistoryentry.md) |
| [**DeviceCondition**](devicecondition.md) |

## Remarks

You can both extend and subset the allowed values for this element.

## See also

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)
