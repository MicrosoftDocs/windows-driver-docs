---
title: TTD Exception Objects
description: This section describes the exception model objects associated with time travel debugging.
ms.author: domars
ms.date: 09/24/2017
ms.localizationpriority: medium
---


# TTD Exception Objects
## Description
*TTD Exception* objects are used to give information about exceptions that happened during a trace session.


## Properties

| Property | Description |
| --- | --- |
| Type | Describes the type of exception. Possible values are "Software" and "Hardware". |
| ProgramCounter | The instruction where the exception was thrown.  |
| Code | The code of the exception.  |
| Flags | The exception flags. |
| RecordAddress | Where in memory you can find the record of the exception.  |

## Children

| Object | Description |
| --- | --- |
| Position | A [position object](time-travel-debugging-position-objects.md) that describes the position the exception occurred. |

## Example Usage

*Information pending*



## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


