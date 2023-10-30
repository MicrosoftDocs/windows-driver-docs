---
title: DeviceCondition element
description: The optional DeviceCondition element provides details about one of the scanner's currently active conditions.
keywords: ["DeviceCondition element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DeviceCondition wscn Id "..."
api_type:
- Schema
ms.date: 04/21/2023
---

# DeviceCondition element

The optional **DeviceCondition** element provides details about one of the scanner's currently active conditions.

## Usage

```xml
<wscn:DeviceCondition wscn:Id="..."
  Id = "xs:string">
  child elements
</wscn:DeviceCondition wscn:Id="...">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Id** | xs:string | No | Required. An integer from 1 through 2147483648. |

## Child elements

| Element |
|--|
| [**Component**](component.md) |
| [**Name Elementfor DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md) |
| [**Severity**](severity.md) |
| [**Time**](time.md) |

## Parent elements

| Element |
|--|
| [**ActiveConditions**](activeconditions.md) |

## Remarks

The WSD Scan Service specifies a unique identifier in the **Id** attribute for this **DeviceCondition** element. The client can use **Id**, along with the value of the [**Time**](time.md) element, to determine if an error condition is new or has gone away. The WSD Scan Service must not reuse the identifier for as long as possible. This delay ensures that clients can accurately keep track of individual **DeviceCondition** elements.

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

## See also

[**ActiveConditions**](activeconditions.md)

[**Component**](component.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name Elementfor DeviceCondition and ConditionHistoryEntry**](name-element-for-devicecondition-and-conditionhistoryentry.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

[**Severity**](severity.md)

[**Time**](time.md)
