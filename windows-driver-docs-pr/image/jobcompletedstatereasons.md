---
title: JobCompletedStateReasons Element
description: The required JobCompletedStateReasons element is a collection of all additional information about how and why a scan job completed.
keywords: ["JobCompletedStateReasons element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobCompletedStateReasons
api_type:
- Schema
ms.date: 04/28/2023
---

# JobCompletedStateReasons element

The required **JobCompletedStateReasons** element is a collection of all additional information about how and why a scan job completed.

## Usage

```xml
<wscn:JobCompletedStateReasons>
  child elements
</wscn:JobCompletedStateReasons>
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
| [**JobEndState**](jobendstate.md) |

## Remarks

The **JobCompletedStateReasons** element contains zero or more [**JobStateReason**](jobstatereason.md) elements, each of which contains a reason for how or why the scan job completed. The WSD Scan Service sends the **JobCompletedStateReasons** element to the client through the [**JobEndStateEvent**](jobendstateevent.md) event element.

## See also

[**JobEndState**](jobendstate.md)

[**JobEndStateEvent**](jobendstateevent.md)

[**JobStateReason**](jobstatereason.md)
