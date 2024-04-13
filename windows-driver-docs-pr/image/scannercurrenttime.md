---
title: ScannerCurrentTime Element
description: The required ScannerCurrentTime element indicates the current date and time according to the scanner's internal clock.
keywords: ["ScannerCurrentTime element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerCurrentTime
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerCurrentTime element

The required **ScannerCurrentTime** element indicates the current date and time according to the scanner's internal clock.

## Usage

```xml
<wscn:ScannerCurrentTime>
  text
</wscn:ScannerCurrentTime>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid value for the dateTime type. For more information about dateTime, see *XML Schema Part 2: Datatypes Second Edition*.**dateTimedateTime**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerStatus**](scannerstatus.md) |

## Remarks

The scanner's internal clock does not have to be a real-time clock. The clock can start at zero (0001-01-01T00:00:00Z) and start counting up when the device is turned on.

All times are based on the time at startup, so the client can calculate duration and relative time by reading the **ScannerCurrentTime** element and comparing it to the previous time value.

## See also

[**ScannerStatus**](scannerstatus.md)
