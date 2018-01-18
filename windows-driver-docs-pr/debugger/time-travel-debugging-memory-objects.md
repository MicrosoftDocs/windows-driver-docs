---
title: TTD Memory Objects
description: This section describes the memory model objects associated with time travel debugging.
ms.author: domars
ms.date: 01/16/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# TTD Memory Objects
## Description
*TTD Memory* is a method that takes beginAddress, endAddress and dataAccessMask parameters and returns a collection of memory objects that contain memory access information.

## Parameters
| Property | Description |
| --- | --- |
| beginAddress | The beginning address of the memory object prefaced with 0x.|
| endAddress| The ending address of the memory object prefaced with 0x.|
| dataAccessMask |The data access mask contained in double quotes. This can be r for read, w for write, e for execute and c for change. |


## Children
| Object      | Description |
| ----------- | ----------- |
| EventType  |	The type of event. This is "MemoryAccess" for all TTD.Memory objects. |
| ThreadId   |	The OS thread ID of thread that made the request. |
| UniqueThreadId |	 A unique ID for the thread across the trace. Regular thread IDs can get reused over the lifetime of a process but UniqueThreadIds cannot. |
| TimeStart | A [position object](time-travel-debugging-position-objects.md) that describes the position when memory access was made. |
| TimeEnd | A [position object](time-travel-debugging-position-objects.md) that describes the position when memory access was made. This will always be the same as the TimeStart for TTD.Memory objects.
| AccessType |	The access type - Read, Write or Execute. |
| IP         |  The instruction pointer of the code that made the memory access. |
| Address    |	The Address that was read / written to / executed and will be in the range of [beginAddress, endAddress) from the parameters to .Memory().  Note that the interval is half-open.  That is, none of the returned events will have an address matching endAddress but there could be events matching endAddress – 1.|
| Size       |	The size of the read/write/execute in bytes. This will typically be 8 bytes or less. In the event of code execution, it is the number of bytes in the instruction that was executed. |
| Value   |	The value that was read, written or executed. In the case of execution, it contains the code bytes for the instruction. Note the instruction bytes are listed in MSB order by the disassembler but will be stored in value in LSB order. |


## Remarks

The following access types are allowed in TTD.Memory queries:

-	r - read
-	w - write
-	rw - read / write
-	e - execute
-	rwe - read / write / execute
-	ec - execute /change

Note that this is a function that does computation, so it takes a while to run. 


## Example Usage

This example shows a grid display of all the positions in the trace where the four bytes of memory starting at 0x00a4fca0 were read access occurred. Click on any entry to drill down on each occurrence of memory access.

```
dx -g @$cursession.TTD.Memory(0x00a4fca0,0x00a4fca4, "r")
```

![memory object dx example grid output](images/ttd-time-travel-memory-object-dx-output.png) 

You can click on the TimeStart fields in any of the events in the grid display, to display information for that event. 

```
0:000> dx -r1 @$cursession.TTD.Memory(0x00a4fca0,0x00a4fca4, "r")[16].TimeStart
@$cursession.TTD.Memory(0x00a4fca0,0x00a4fca4, "r")[16].TimeStart                 : 5D:113 [Time Travel]
    Sequence         : 0x5d
    Steps            : 0x113
```

To move to the position in the trace that the event occurred, click on [Time Travel].

```
0:000> dx @$cursession.TTD.Memory(0x00a4fca0,0x00a4fca4, "r")[16].TimeStart.SeekTo()
@$cursession.TTD.Memory(0x00a4fca0,0x00a4fca4, "r")[16].TimeStart.SeekTo()
(27b8.3168): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 5D:113

eax=0000004c ebx=00dd0000 ecx=00a4f89c edx=00a4f85c esi=00a4f89c edi=00b61046
eip=690795e5 esp=00a4f808 ebp=00a4f818 iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000206
690795e5 ffb604040000    push    dword ptr [esi+404h] ds:002b:00a4fca0=00000000
```

In this example, all of the positions in the trace where the four bytes of memory starting at 0x1bf7d0 were read/write accessed are listed. Click on any entry to drill down on each occurrence of memory access.

```
0:000> dx @$cursession.TTD.Memory(0x1bf7d0,0x1bf7d4, "rw")
@$cursession.TTD.Memory(0x1bf7d0,0x1bf7d4, "rw")                
    [0x0]           
    [0x1]           
    [0x2]           
    [0x3]           
     ...
```

In this last example, the positions in the trace where the four bytes of memory starting at 0x13a1710 were execute/change accessed were listed. And then the first [0] occurrence was clicked on to display additional information.

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