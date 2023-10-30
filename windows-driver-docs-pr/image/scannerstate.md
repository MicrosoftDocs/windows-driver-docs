---
title: ScannerState element
description: The required ScannerState element identifies the current state of the scanning portion of the scan device.
keywords: ["ScannerState element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerState
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerState element

The required **ScannerState** element identifies the current state of the scanning portion of the scan device.

## Usage

```xml
<wscn:ScannerState>
  text
</wscn:ScannerState>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following string values.

| Value | Description |
|--|--|
| Idle | The scanner is available and can start processing a new job. |
| Processing | The scanner is currently processing jobs. |
| Stopped | No jobs can be processed and intervention is needed. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerStatus**](scannerstatus.md) |
| [**StatusSummary**](statussummary.md) |

## Remarks

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

You can both extend and subset the allowed values for this element.

## See also

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStatus**](scannerstatus.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

[**StatusSummary**](statussummary.md)
