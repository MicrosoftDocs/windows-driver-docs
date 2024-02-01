---
title: JobCompletedState Element
description: The required JobCompletedState element specifies a job's final job state.
keywords: ["JobCompletedState element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobCompletedState
api_type:
- Schema
ms.date: 04/28/2023
---

# JobCompletedState element

The required **JobCompletedState** element specifies a job's final job state.

## Usage

```xml
<wscn:JobCompletedState>
  text
</wscn:JobCompletedState>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values from the [**JobState**](jobstate.md) element:

- Aborted
- Canceled
- Completed
- Terminating

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobEndState**](jobendstate.md) |

## Remarks

The WSD Scan Service sends a **JobCompletedState** element to the client within the [**JobEndStateEvent**](jobendstateevent.md) event element.

## See also

[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobState**](jobstate.md)
