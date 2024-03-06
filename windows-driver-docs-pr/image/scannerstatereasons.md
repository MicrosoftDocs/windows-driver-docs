---
title: ScannerStateReasons Element
description: The required ScannerStateReasons element is a list of ScannerStateReason elements that describes all of the reasons why the scanner is in its current state.
keywords: ["ScannerStateReasons element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerStateReasons
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerStateReasons element

The required **ScannerStateReasons** element is a list of [**ScannerStateReason**](scannerstatereason.md) elements that describes all of the reasons why the scanner is in its current state.

## Usage

```xml
<wscn:ScannerStateReasons>
  child elements
</wscn:ScannerStateReasons>
```

## Attributes

There are no attributes.

## Text value

None

## Child elements

| Element |
|--|
| [**ScannerStateReason**](scannerstatereason.md) |

## Parent elements

| Element |
|--|
| [**ScannerStatus**](scannerstatus.md) |
| [**StatusSummary**](statussummary.md) |

## Remarks

The **ScannerStateReasons** element is a list of **ScannerStateReason** elements, each of which describes a reason why the scanner is in its current state.

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

## See also

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStateReason**](scannerstatereason.md)

[**ScannerStatus**](scannerstatus.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

[**StatusSummary**](statussummary.md)
