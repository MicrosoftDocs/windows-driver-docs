---
title: StatusSummary element
description: The required StatusSummary element contains a summary of the scan device's current status.
keywords: ["StatusSummary element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn StatusSummary
api_type:
- Schema
ms.date: 05/02/2023
---

# StatusSummary element

The required **StatusSummary** element contains a summary of the scan device's current status.

## Usage

```xml
<wscn:StatusSummary>
  child elements
</wscn:StatusSummary>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ScannerState**](scannerstate.md) |
| [**ScannerStateReasons**](scannerstatereasons.md) |

## Parent elements

| Element |
|--|
| [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) |

## Remarks

The WSD Scan Service must include the **StatusSummary** element when it sends a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event element to the client. The scanner's current state and reasons for why it is in this state are specified in the [**ScannerState**](scannerstate.md) and [**ScannerStateReasons**](scannerstatereasons.md) elements, respectively.

## See also

[**ScannerStateReasons**](scannerstatereasons.md)

[**ScannerState**](scannerstate.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)
