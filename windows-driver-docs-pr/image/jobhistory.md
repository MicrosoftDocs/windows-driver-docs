---
title: JobHistory element (required)
description: The required JobHistory element contains a list of JobSummary elements that describe the most recently completed jobs in the scan device.
keywords: ["JobHistory element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobHistory
api_type:
- Schema
ms.date: 07/06/2020
ms.localizationpriority: medium
---

# JobHistory element (required)

The required **JobHistory** element contains a list of [**JobSummary**](jobsummary.md) elements that describe the most recently completed jobs in the scan device.

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
| [**JobSummary**](jobsummary.md) |

## Parent elements

| Element |
|--|
| [**GetJobHistoryResponse**](getjobhistoryresponse.md) |

## Remarks

The **JobHistory** element contains a [**JobSummary**](jobsummary.md) element for every job that the scanner recently completes. **JobHistory** is empty if the WSD Scan Service has no record of recently completed jobs. The Scan Service returns this list from [**GetJobHistoryResponse**](getjobhistoryresponse.md).

The amount of job history that the WSD Scan Service stores and returns is implementation-specific.

## See also

[**GetJobHistoryResponse**](getjobhistoryresponse.md)

[**JobSummary**](jobsummary.md)
