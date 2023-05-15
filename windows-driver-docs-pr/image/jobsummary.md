---
title: JobSummary element
description: The optional JobSummary element contains a summary about a scan job.
keywords: ["JobSummary element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobSummary
api_type:
- Schema
ms.date: 04/28/2023
---

# JobSummary element

The optional **JobSummary** element contains a summary about a scan job.

## Usage

```xml
<wscn:JobSummary>
  child elements
</wscn:JobSummary>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobId**](jobid.md) |
| [**JobName**](jobname.md) |
| [**JobOriginatingUserName**](joboriginatingusername.md) |
| [**JobState**](jobstate.md) |
| [**JobStateReasons**](jobstatereasons.md) |
| [**ScansCompleted**](scanscompleted.md) |

## Parent elements

| Element |
|--|
| [**ActiveJobs**](activejobs.md) |
| [**JobHistory**](jobhistory.md) |

## Remarks

If the parent element of the **JobSummary** element is [**ActiveJobs**](activejobs.md), **JobSummary** contains a summary of information about one job that is currently active within the scan device.

If the parent element is [**JobHistory**](jobhistory.md), **JobSummary** contains a summary of information about a single, recently completed job within the scan device.

## See also

[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**JobState**](jobstate.md)

[**JobStateReasons**](jobstatereasons.md)

[**ScansCompleted**](scanscompleted.md)
