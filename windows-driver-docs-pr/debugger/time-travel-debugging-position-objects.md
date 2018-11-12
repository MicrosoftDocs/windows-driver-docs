---
title: TTD Position Objects
description: This section describes the position model objects associated with time travel debugging.
ms.author: domars
ms.date: 12/19/2017
ms.localizationpriority: medium
---

# TTD Position Objects
## Description
*Position* objects are used to describe a position in a time travel trace. A position object is normally described by two hexadecimal numbers separated by a colon. The first of the hexadecimal numbers is the *Sequence* and the second is the *Steps*.

A position of FFFFFFFFFFFFFFFE:0 indicates the end of the trace.

## Properties

| Property | Description |
| --- | --- |
| Sequence | The sequencing point relevant to the position. |
| Steps | The number of steps from the sequence point in this thread to get to this position. |

## Methods

| Method | Description |
| --- | --- |
| SeekTo() | Time travels to this position in the trace. |

## Example Usage
*Information pending*



## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


