---
title: TTD Exception Objects
description: This section describes the exception model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

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
Coming soon.

## See Also
Coming soon.