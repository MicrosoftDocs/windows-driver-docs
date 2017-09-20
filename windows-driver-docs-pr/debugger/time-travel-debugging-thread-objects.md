---
title: TTD Thread Objects
description: This section describes the thread model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Thread Objects
## Description
*TTD Thread* objects are used to give information about threads and their lifetime during a time travel trace.

## Properties
| Property | Description |
| --- | --- |
| UniqueId | A unique ID for the thread across the trace. |
| Id | The TID of the thread. |


## Children
| Object | Description |
| --- | --- |
| LifeTime | A [TTD range object](time-travel-debugging-range-object.md) that describes the lifetime of the thread. |
| ActiveTime | A [TTD range object](time-travel-debugging-range-object.md) that describes the time the thread was active. |

## Example Usage
`TODO`

## See Also
`TODO`