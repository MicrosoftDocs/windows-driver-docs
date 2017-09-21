---
title: TTD Event Objects
description: This section describes the event model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Event Objects
## Description
*TTD Event* objects are used to give information about important events that happened during a time travel trace.

## Properties
| Property | Description |
| --- | --- |
| Type | Describes the type of event that happened. Possible values are: ThreadCreated, ThreadTerminated, ModuleLoaded, ModuleUnloaded, Exception |

## Children
| Object | Description |
| --- | --- |
| Position | A [position object](time-travel-debugging-position-objects.md) that describes the position the event occurred. |
| Module* | A [module object](time-travel-debugging-module-objects.md) containing information about the module that was loaded or unloaded. |
| Thread* | A [thread object](time-travel-debugging-thread-objects.md) containing information about the thread that was created or terminated. |
| Exception* | An [exception object](time-travel-debugging-exception-objects.md) containing information about the exception that was hit. |

\* - Existence of these child objects depends on the type of event

## Example Usage
`TODO`

## See Also
`TODO`