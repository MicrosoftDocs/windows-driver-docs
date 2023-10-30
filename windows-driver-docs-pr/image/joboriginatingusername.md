---
title: JobOriginatingUserName element
description: The required JobOriginatingUserName element specifies the name of the user who submitted the scan job.
keywords: ["JobOriginatingUserName element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobOriginatingUserName
api_type:
- Schema
ms.date: 04/28/2023
---

# JobOriginatingUserName element

The required **JobOriginatingUserName** element specifies the name of the user who submitted the scan job.

## Usage

```xml
<wscn:JobOriginatingUserName>
  text
</wscn:JobOriginatingUserName>
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

The client or the security infrastructure, if any, provides the **JobOriginatingUserName** element. A client should supply a value to help users easily distinguish between the jobs that they submitted and jobs that other users submitted.

The WSD Scan Service can provide a default **JobOriginatingUserName** name in its [**DefaultScanTicket**](defaultscanticket.md) element. You can set this name in an implementation-specific manner.

The name of the job is specified in the [**JobName**](jobname.md) element.

## See also

[**DefaultScanTicket**](defaultscanticket.md)

[**JobDescription**](jobdescription.md)

[**JobEndState**](jobendstate.md)

[**JobName**](jobname.md)

[**JobSummary**](jobsummary.md)
