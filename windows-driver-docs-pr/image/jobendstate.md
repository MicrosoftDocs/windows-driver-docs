---
title: JobEndState Element
description: The required JobEndState element describes the final state of the current scan job.
keywords: ["JobEndState element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobEndState
api_type:
- Schema
ms.date: 04/28/2023
---

# JobEndState element

The required **JobEndState** element describes the final state of the current scan job.

## Usage

```xml
<wscn:JobEndState>
  child elements
</wscn:JobEndState>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobCompletedState**](jobcompletedstate.md) |
| [**JobCompletedStateReasons**](jobcompletedstatereasons.md) |
| [**JobCompletedTime**](jobcompletedtime.md) |
| [**JobId**](jobid.md) |
| [**JobName**](jobname.md) |
| [**JobOriginatingUserName**](joboriginatingusername.md) |
| [**ScansCompleted**](scanscompleted.md) |

## Parent elements

| Element |
|--|
| [**JobEndStateEvent**](jobendstateevent.md) |

## Remarks

The **JobEndState** element contains child elements that describe various aspects about the end state of a scan job. The WSD Scan Service sends a **JobEndState** element to a client through the [**JobEndStateEvent**](jobendstateevent.md) element.

## See also

[**JobCompletedState**](jobcompletedstate.md)

[**JobCompletedStateReasons**](jobcompletedstatereasons.md)

[**JobCompletedTime**](jobcompletedtime.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobId**](jobid.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**ScansCompleted**](scanscompleted.md)
