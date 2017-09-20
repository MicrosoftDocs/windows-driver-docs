---
title: TTD Position Objects
description: This section describes the position model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Position Objects
## Description
*Position* objects are used to describe a position in a time travel trace. A position object is normally described by two hexadecimal numbers separated by a colon. The first of the hexadecimal numbers is the *Steps* and the second is the *Sequence*.

## Properties
| Property | Description |
| --- | --- |
| Sequence | The sequencing point relevant to the position. |
| Steps | The number of steps from the sequence point to get to this posiiton. |

## Methods
| Method | Description |
| --- | --- |
| SeekTo() | Time travels the trace to the position. |

## Example Usage
`TODO`

## See Also
`TODO`