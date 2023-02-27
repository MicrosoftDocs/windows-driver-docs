---
title: JobHistory element (optional)
description: The optional JobHistory element contains information about scan jobs that have recently completed processing.
keywords: ["JobHistory element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobHistory
api_type:
- Schema
ms.date: 07/06/2020
---

# JobHistory element (optional)

The optional **JobHistory** element contains information about scan jobs that have recently completed processing.

## Usage

```xml
<wscn:JobHistory>
  child elements
</wscn:JobHistory>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Job**](job.md) |
| [**JobSummary**](jobsummary.md) |

## Parent elements

| Element |
|--|
| [**GetJobHistoryResponse**](getjobhistoryresponse.md) |
| [**JobTable**](jobtable.md) |

## Remarks

The **JobHistory** element contains a subset of the most recent jobs that have finished processing. These jobs could have scanned, been aborted, or failed for other reasons. The maximum number of jobs in this list depends on the device.

A client can ask for job history through the [**GetJobHistoryRequest**](getjobhistoryrequest.md) operation element. The WSD Scan Service returns this history in a [**GetJobHistoryResponse**](getjobhistoryresponse.md) operation element.

## See also

[**GetJobHistoryRequest**](getjobhistoryrequest.md)

[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)
