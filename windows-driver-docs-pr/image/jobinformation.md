---
title: JobInformation element
description: The optional JobInformation element describes the intended use of the job.
keywords: ["JobInformation element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobInformation
api_type:
- Schema
ms.date: 04/28/2023
---

# JobInformation element

The optional **JobInformation** element describes the intended use of the job.

## Usage

```xml
<wscn:JobInformation>
  text
</wscn:JobInformation>
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

## Remarks

The **JobInformation** value is useful when the client will reuse the scan ticket that is used to create the job.

## See also

[**JobDescription**](jobdescription.md)
