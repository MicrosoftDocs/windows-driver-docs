---
title: TTD Memory Objects
description: This section describes the memory model objects associated with time travel debugging.
ms.author: windowsdriverdev
ms.date: 01/11/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Memory Objects
## Description
*TTD Memory* objects TBD.

## Parameters
| Property | Description |
| --- | --- |
| beginAddress | The beginning address of the memory object prefaced with 0x.|
| endAddress| The ending address of the memory object prefaced with 0x.|
| dataAccessMask |The data access mask contained in double quotes. This can be r for read, w for write, e for execute and c for change. |


## Children
| Object      | Description |
| ----------- | ----------- |
| EventType  |	The type of event such as "MemoryAccess". |
| ThreadId   |	The OS thread ID of thread that made the request. |
| UniqueThreadId  |	 The Unique Thread Id of the ____________. |
| TimeStart | A [position object](time-travel-debugging-position-objects.md) that describes the position at the start of the call. |
| TimeEnd | A [position object](time-travel-debugging-position-objects.md) that describes the position at the end of the call. |
TimeStart	A position object that describes the position at the time memory access was made.
TimeEnd	A position object that describes the position at at the time memory access was made. This will always be the same as the TimeStart for TTD.Memory objects.

| AccessType |	The access type - Read, Write, Change or Execute |
| IP         |  The instruction pointer of the code that made the memory access |
| Address    |	The Address of the TTD.Memory object |
| Size       |	The size the size of the read/write/execute in bytes. This will typically be 8 bytes or less. In the event of code execution, it is the number of bytes in the instruction that was executed. |
| Value   |	The value that was read, written or executed. In the case of execution it contains the code bytes for the instruction. Note the instruction bytes are listed in MSB order by the disassembler but will be stored in the value in LSB order. |


## Remarks

The following access types are allowed in TTD.Memory queries:

-	r - read
-	w - write
-	rw - read / write
-	e - execute
-	ec - execute /change




## Example Usage

In this example all of the positions in the trace where the four bytes of memory starting at 0x1bf7d0 were read/write accessed are listed. Click on any entry to drill down on each occurrence of memory access.

```
0:000> dx @$cursession.TTD.Memory(0x1bf7d0,0x1bf7d4, "rw")
@$cursession.TTD.Memory(0x1bf7d0,0x1bf7d4, "rw")                
    [0x0]           
    [0x1]           
    [0x2]           
    [0x3]           
     ...
```

In this example all of the postions in the trace where the four bytes of memory starting at 0x13a1710 were execute/change accessed are listed. Click on any occurance to drill down on for addtional information on each occurance of memory access.

```
0:000> dx -r1 @$cursession.TTD.Memory(0x13a1710,0x13a1714, "ec")[0]
@$cursession.TTD.Memory(0x13a1710,0x13a1714, "ec")[0]                
    EventType        : MemoryAccess
    ThreadId         : 0x1278
    UniqueThreadId   : 0x2
    TimeStart        : 5B:4D [Time Travel]
    TimeEnd          : 5B:4D [Time Travel]
    AccessType       : Execute
    IP               : 0x13a1710
    Address          : 0x13a1710
    Size             : 0x1
    Value            : 0x55
```



## See Also

[Time Travel Debugging - Introduction to Time Travel Debugging objects](time-travel-debugging-object-model.md)

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")