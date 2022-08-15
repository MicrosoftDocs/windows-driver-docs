---
title: Name Element for DeviceCondition and ConditionHistoryEntry element
description: The required Name element names the current error condition that is specified in a DeviceCondition or ConditionHistoryEntry element.
keywords: ["Name Element for DeviceCondition and ConditionHistoryEntry element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Name
api_type:
- Schema
ms.date: 09/28/2021
---

# Name Element for DeviceCondition and ConditionHistoryEntry element

The required **Name** element names the current error condition that is specified in a [**DeviceCondition**](devicecondition.md) or [**ConditionHistoryEntry**](conditionhistoryentry.md) element.

## Usage

```xml
<wscn:Name>
  text
</wscn:Name>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| Calibrating | The scan device is calibrating its internal components to prepare to acquire images. |
| CoverOpen | One of more covers on the scan device are open. |
| InputTrayEmpty | The automatic document feeder (ADF) input has no media. |
| InterlockOpen | The interlock is open. |
| InternalStorageFull | The internal storage component that is currently being written to is full. |
| LampError | The scanner lamp is failing and image acquisition cannot proceed. |
| LampWarming | The scanner lamp is warming to prepare to acquire images. |
| MediaJam | Media is jammed in one of the input sources, so image acquisition failed. |
| MultipleFeedError | The ADF was fed more than one piece of media simultaneously. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ConditionHistoryEntry**](conditionhistoryentry.md) |
| [**DeviceCondition**](devicecondition.md) |

## Remarks

Some error names are valid for only certain [**Component**](component.md) elements.

You can both extend and subset the allowed values for this element.

## See also

[**Component**](component.md)

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**DeviceCondition**](devicecondition.md)
