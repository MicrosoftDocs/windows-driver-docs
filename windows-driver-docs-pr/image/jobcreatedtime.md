---
title: JobCreatedTime Element
description: The optional JobCreatedTime element specifies the time at which the job was created.
keywords: ["JobCreatedTime element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobCreatedTime
api_type:
- Schema
ms.date: 04/28/2023
---

# JobCreatedTime element

The optional **JobCreatedTime** element specifies the time at which the job was created.

## Usage

```xml
<wscn:JobCreatedTime>
  text
</wscn:JobCreatedTime>
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
| [**JobStatus**](jobstatus.md) |

## Remarks

A job is *created* when the job is submitted to the system.

The specified time refers to the internal clock of the scan device and does not need to be a real time clock.

## See also

[**JobStatus**](jobstatus.md)
