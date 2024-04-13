---
title: JobStatus Element
description: The required JobStatus element contains all information about the status of the current scan job.
keywords: ["JobStatus element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobStatus
api_type:
- Schema
ms.date: 04/28/2023
---

# JobStatus element

The required **JobStatus** element contains all information about the status of the current scan job.

## Usage

```xml
<wscn:JobStatus>
  child elements
</wscn:JobStatus>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobCompletedTime**](jobcompletedtime.md) |
| [**JobCreatedTime**](jobcreatedtime.md) |
| [**JobId**](jobid.md) |
| [**JobState**](jobstate.md) |
| [**JobStateReasons**](jobstatereasons.md) |
| [**ScansCompleted**](scanscompleted.md) |

## Parent elements

| [**Job**](job.md) |

## Remarks

**JobStatus** child elements are maintained through automata. The WSD Scan Service should update **JobStatus** elements accordingly as it processes a job. A client operation, such as [**CancelJobRequest**](canceljobrequest.md), can indirectly affect job status.

The WSD Scan Service notifies a client about changes to a job's status through a [**JobStatusEvent**](jobstatusevent.md) event element. The WSD Scan Service should generate a **JobStatusEvent** element for every change to all **JobStatus** child elements.

A client can query for job status through the [**GetJobElementsRequest**](getjobelementsrequest.md) operation.

## See also

[**CancelJobRequest**](canceljobrequest.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**Job**](job.md)

[**JobCompletedTime**](jobcompletedtime.md)

[**JobCreatedTime**](jobcreatedtime.md)

[**JobId**](jobid.md)

[**JobState**](jobstate.md)

[**JobStateReasons**](jobstatereasons.md)

[**JobStatusEvent**](jobstatusevent.md)

[**ScansCompleted**](scanscompleted.md)
