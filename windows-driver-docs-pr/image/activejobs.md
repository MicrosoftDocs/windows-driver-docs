---
title: ActiveJobs element
description: The required ActiveJobs element contains a list of all currently active scan jobs.
keywords: ["ActiveJobs element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ActiveJobs
api_type:
- Schema
ms.date: 03/27/2023
---

# ActiveJobs element

The required **ActiveJobs** element contains a list of all currently active scan jobs.

## Usage

```xml
<wscn:ActiveJobs>
  child elements
</wscn:ActiveJobs>
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
| [**GetActiveJobsResponse**](getactivejobsresponse.md) |
| [**JobTable**](jobtable.md) |

## Remarks

The **ActiveJobs** element contains all jobs that have not yet completed processing. The state of active jobs could be scanning, pending, or stopped. **ActiveJobs** is empty when there are no currently active jobs.

A client can ask for the list of active jobs through the [**GetActiveJobsRequest**](getactivejobsrequest.md) operation. The WSD Scan Service returns the list in a [**GetActiveJobsResponse**](getactivejobsresponse.md) operation element.

## See also

[**GetActiveJobsRequest**](getactivejobsrequest.md)

[**GetActiveJobsResponse**](getactivejobsresponse.md)

[**Job**](job.md)

[**JobSummary**](jobsummary.md)

[**JobTable**](jobtable.md)
