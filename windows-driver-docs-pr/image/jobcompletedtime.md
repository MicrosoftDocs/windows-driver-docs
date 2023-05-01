---
title: JobCompletedTime element
description: The optional JobCompletedTime element specifies the time at which the scan job was completed.
keywords: ["JobCompletedTime element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobCompletedTime
api_type:
- Schema
ms.date: 04/28/2023
---

# JobCompletedTime element

The optional **JobCompletedTime** element specifies the time at which the scan job was completed.

## Usage

```xml
<wscn:JobCompletedTime>
  text
</wscn:JobCompletedTime>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid value for the dateTime type. For more information about dateTime, see *XML Schema Part 2: Datatypes Second Edition.***dateTimedateTime**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobEndState**](jobendstate.md) |
| [**JobStatus**](jobstatus.md) |

## Remarks

A scan job is *complete* when all processing has completed, either because scanning and document transfer completed successfully or because a fatal error was encountered.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## See also

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)
