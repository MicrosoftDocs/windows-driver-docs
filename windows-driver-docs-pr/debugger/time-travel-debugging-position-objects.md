---
title: TTD Position Objects
description: This section describes the position model objects associated with time travel debugging.
ms.author: domars
ms.date: 12/19/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

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


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
