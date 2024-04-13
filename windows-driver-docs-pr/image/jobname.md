---
title: JobName Element
description: The required JobName element specifies the client-supplied, user-friendly name of the scan job.
keywords: ["JobName element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobName
api_type:
- Schema
ms.date: 04/28/2023
---

# JobName element

The required **JobName** element specifies the client-supplied, user-friendly name of the scan job.

## Usage

```xml
<wscn:JobName>
  text
</wscn:JobName>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid character string.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobDescription**](jobdescription.md) |
| [**JobEndState**](jobendstate.md) |
| [**JobSummary**](jobsummary.md) |

## Remarks

A client should supply a value to help users easily distinguish between jobs that they submitted.

The WSD Scan Service can provide a default **JobName** name in its [**DefaultScanTicket**](defaultscanticket.md) element. You can set this name in an implementation-specific manner.

The name of the user who submitted the job is specified in the [**JobOriginatingUserName**](joboriginatingusername.md) element.

## See also

[**DefaultScanTicket**](defaultscanticket.md)

[**JobDescription**](jobdescription.md)

[**JobEndState**](jobendstate.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**JobSummary**](jobsummary.md)
