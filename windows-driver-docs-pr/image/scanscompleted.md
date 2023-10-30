---
title: ScansCompleted element
description: The required ScansCompleted element specifies the number of images that are scanned.
keywords: ["ScansCompleted element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScansCompleted
api_type:
- Schema
ms.date: 05/02/2023
---

# ScansCompleted element

The required **ScansCompleted** element specifies the number of images that are scanned.

## Usage

```xml
<wscn:ScansCompleted>
  text
</wscn:ScansCompleted>
```

## Attributes

There are no attributes.

## Text value

Required. An integer value from 1 through 2147483648.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobEndState**](jobendstate.md) |
| [**JobStatus**](jobstatus.md) |
| [**JobSummary**](jobsummary.md) |

## Remarks

If a sheet of media is scanned multiple times, the WSD Scan Service must increment the **ScansCompleted** count every time. Each side of a media sheet is scanned in duplex mode, generating two scans in the **ScansCompleted** count.

The **ScansCompleted** count might not be known until the scanner has completed processing the job. The WSD Scan Service must update the **ScansCompleted** element when more exact information is available.

## See also

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)
