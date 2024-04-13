---
title: Job Element
description: The required Job element contains all elements that are associated with a scan job.
keywords: ["Job element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Job
api_type:
- Schema
ms.date: 04/28/2023
---

# Job element

The required **Job** element contains all elements that are associated with a scan job.

## Usage

```xml
<wscn:Job>
  child elements
</wscn:Job>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Documents**](documents.md) |
| [**JobStatus**](jobstatus.md) |
| [**ScanTicket**](scanticket.md) |

## Parent elements

| Element |
|--|
| [**ActiveJobs**](activejobs.md) |

## Remarks

A scan job (which the **Job** element represents) can contain one or more documents. The WSD Scan Service's processing instructions for both a job and its documents are executed at the **Job** level.

## See also

[**ActiveJobs**](activejobs.md)

[**Documents**](documents.md)

[**JobStatus**](jobstatus.md)

[**ScanTicket**](scanticket.md)
