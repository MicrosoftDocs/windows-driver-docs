---
title: JobState element
description: The required JobState element specifies the current state of the job.
keywords: ["JobState element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobState
api_type:
- Schema
ms.date: 09/27/2021
---

# JobState element

The required **JobState** element specifies the current state of the job.

## Usage

```xml
<wscn:JobState>
  text
</wscn:JobState>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| Aborted | The system aborted the job. |
| Canceled | The job was canceled by a client that is using the CancelJobRequest operation or by means outside the scope of the WSD Scan Service. |
| Completed | The job is finished processing and all of the image data has been sent to the client. |
| Creating | The job is being initialized. |
| Held | The job is waiting to be processed but is unavailable for scheduling. The job can reach this state only by methods outside the scope of the WSD Scan Service. |
| Pending | The job has been initialized and is waiting to be processed. |
| Processing | The job data is being digitized, transformed, or transferred. |
| Started | The scan device has started processing the job. This state is a transient state and will typically be seen only with a JobStatusEvent event. |
| Terminating | The job was canceled by either a client-initiated CancelJobRequest operation or aborted by means outside the scope of the WSD Scan Service. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobStatus**](jobstatus.md) |
| [**JobSummary**](jobsummary.md) |

## Remarks

When the **JobState** element is contained in a [**JobEndStateEvent**](jobendstateevent.md) event or [**JobHistory**](jobhistory2.md) element, **JobState** represents the completed state of a job. Otherwise, **JobState** specifies the current state of the job.

You can both extend and subset the allowed values for this element.

## See also

[**CancelJobRequest**](canceljobrequest.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobHistory**](jobhistory2.md)

[**JobStatus**](jobstatus.md)

[**JobStatusEvent**](jobstatusevent.md)

[**JobSummary**](jobsummary.md)
