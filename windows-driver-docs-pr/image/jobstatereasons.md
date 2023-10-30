---
title: JobStateReasons element
description: The required JobStateReasons element contains all additional information about why a job is in its current state.
keywords: ["JobStateReasons element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobStateReasons
api_type:
- Schema
ms.date: 04/28/2023
---

# JobStateReasons element

The required **JobStateReasons** element contains all additional information about why a job is in its current state.

## Usage

```xml
<wscn:JobStateReasons>
  child elements
</wscn:JobStateReasons>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobStateReason**](jobstatereason.md) |

## Parent elements

| Element |
|--|
| [**JobStatus**](jobstatus.md) |
| [**JobSummary**](jobsummary.md) |

## Remarks

The **JobStateReasons** element contains a list of [**JobStateReason**](jobstatereason.md) elements, each of which specifies one reason why a job is in its current state.

## See also

[**JobStateReason**](jobstatereason.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)
