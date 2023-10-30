---
title: JobTable element
description: The required JobTable element contains current and historical information about scan jobs.
keywords: ["JobTable element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobTable
api_type:
- Schema
ms.date: 05/01/2023
---

# JobTable element

The required **JobTable** element contains current and historical information about scan jobs.

## Usage

```xml
<wscn:JobTable>
  child elements
</wscn:JobTable>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ActiveJobs**](activejobs.md) |
| [**JobHistory**](jobhistory2.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service uses a **JobTable** element to track all current and finished scan jobs that are submitted to the WSD Scan Service. Current jobs are tracked in the [**ActiveJobs**](activejobs.md) child element; finished jobs are optionally tracked in the [**JobHistory**](jobhistory2.md) child element.

## See also

[**ActiveJobs**](activejobs.md)

[**JobHistory**](jobhistory2.md)
