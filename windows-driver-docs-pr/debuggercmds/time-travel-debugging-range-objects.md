---
title: TTD Range Objects
description: This section describes the range model objects associated with time travel debugging.
keywords: ["TTD Range Objects", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 09/22/2017
---

# TTD Range Objects

## Description

*TTD Range* objects are used to give information about a range of time in a trace. These are generally used to describe the lifetime of a [TTD thread object](time-travel-debugging-thread-objects.md) during a TTD session.

## Children

| Object | Description |
| --- | --- |
| MinPosition | A [position object](time-travel-debugging-position-objects.md) that describes the earliest position relevant to the range. |
| MaxPosition | A [position object](time-travel-debugging-position-objects.md) that describes the latest position relevant to the range. |


## Example Usage

*Information pending*

## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

