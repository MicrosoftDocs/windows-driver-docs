---
title: ConditionHistory element
description: The optional ConditionHistory element is a collection of ConditionHistoryEntry elements that provide details about recent conditions and errors on the scanner.
keywords: ["ConditionHistory element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ConditionHistory
api_type:
- Schema
ms.date: 03/29/2023
---

# ConditionHistory element

The optional **ConditionHistory** element is a collection of [**ConditionHistoryEntry**](conditionhistoryentry.md) elements that provide details about recent conditions and errors on the scanner.

## Usage

```xml
<wscn:ConditionHistory>
  child elements
</wscn:ConditionHistory>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ConditionHistoryEntry**](conditionhistoryentry.md) |

## Parent elements

| Element |
|--|
| [**ScannerStatus**](scannerstatus.md) |

## Remarks

A client can query the scanner's **ConditionHistory** element by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

The conditions vary in severity from informational to critical.

## See also

[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStatus**](scannerstatus.md)
