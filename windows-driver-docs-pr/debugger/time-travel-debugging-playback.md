---
title: Time Travel Debugging - Playback
description: This section describes how to record time travel traces.
ms.author: windowsdriverdev
ms.date: 09/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Playback 


This section describes how to playback time travel traces and navigate in time.

## Command time travel navigation

Use a trailing minus sign with the following version of these commands to travel back in time.

| Command  |  For more information |
|----|-------------------------------------------------------------------------------------------|
| t- | [t (Trace)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/t--trace-) |
| p- | [p (Step)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/p--step-)   |
| g- | [g (Go)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/g--go-)       |

## Ribbon button time travel navigation

Alternatively, use the ribbon buttons to navigate in the trace.

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-ribbon-buttons.png)


## Trace Segment Terminology

This table summarizes the major elements of a TTD Trace.
| Term  |  Description|
|----|-------------------------------------------------------------------------------------------|
| Keyframe | A location in a trace where replay can start with no previous data​. Keyframes are generated automatically. Larger traces will contain more keyframes. When the trace is indexed, the number of keyframes is displayed. |
| Trace segment​ | Part of a recorded thread between two key frames​.  |
| Instruction Position Reference |A specific position reference in the trace, for example 12:0. |
| Position | The current position in the trace.  |
| Sequencing point​ | Orderable event in the trace.​ |

TBD - Create elements of trace file diagram.


## Example TTD Playback

This outputs shows using the !tt 0 command to reset the time postion to the begining of the trace. 

```
0:000> !tt 0
Setting position to the beginning of the trace
Setting position: 10:0
(4604.21dc): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 10:0
ntdll!ZwTestAlert+0x14:
00007ffc`61f789d4 c3              ret
```

This outputs shows using the p command to travel forward in a TTD trace. 

```
0:000> p
Time Travel Position: E:1
ntdll!TpAdjustBindingCount+0x49:
00007ff9`31e887ed ebd4            jmp     ntdll!TpAdjustBindingCount+0x1f (00007ff9`31e887c3)
0:000> p
Time Travel Position: E:2
ntdll!TpAdjustBindingCount+0x1f:
00007ff9`31e887c3 4883c428        add     rsp,28h
0:000> p
Time Travel Position: E:4
    could step in/over inline function frames ...
01 000000e4`d1c8f110 00007ff9`31e8668a ntdll!TppInitializeTimer+0x54 [minkernel\threadpool\ntdll\timer.c @ 1411] 
ntdll!TppInitializeTimer+0x54:
00007ff9`31e8875c 4883a3f000000000 and     qword ptr [rbx+0F0h],0 ds:0000027c`e87065f0=0000000000000000
```

This outputs shows using the p- command to travel backwards in a TTD trace. 

```
0:000> p-
Time Travel Position: E:3
ntdll!TpAdjustBindingCount+0x23:
00007ff9`31e887c7 c3              ret
0:000> p-
Time Travel Position: E:1
ntdll!TpAdjustBindingCount+0x49:
00007ff9`31e887ed ebd4            jmp     ntdll!TpAdjustBindingCount+0x1f (00007ff9`31e887c3)
0:000> p-
TTD: Start of trace reached.
(1a04.3bd0): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: E:0
ntdll!ZwSetInformationWorkerFactory+0x14:
00007ff9`31ed0894 c3              ret
```

TBD- Why did we skip over E:2 in the example above?

## !tt navigation commands

Provide a time position in any of the following formats to travel to that point in time.

!tt <position> - Time travel to the given position in the trace.
           
- If <position> is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !tt 0                   - Time travel to the beginning of the trace
    - !tt 50                  - Time travel to halfway through the trace
    - !tt 100                 - Time travel to the end of the trace
 

- If <position> is #:#, where # are a hexadecimal numbers, it travels to that position. If the number after : is omitted, it's defaulted to zero.
    - !tt 1A0:                - Time travel to position 1A0:0
    - !tt 1A0:0               - Time travel to position 1A0:0
    - !tt 1A0:12F             - Time travel to position 1A0:12F

- If the : is omitted, then the second number must have precisely 16 hexadecimal digits, with zeros for left-padding.
    - !tt 1A0000000000000012F - Time travel to position 1A0:12F


## !tt.positions

Use !tt.*positions* to display all the active threads, including their current positions.

```
0:000> !tt.positions
>Thread ID=0x4164 - Position: 97:4
 Thread ID=0x4C8C - Position: F2:0
 Thread ID=0x1E08 - Position: F3:0
```
In this example three threads each ran until they finished, one after another.  (TBD - Confirm)


## !tt Extension utility commands

Use the following !tt extension commands to work with TTD traces.

You can change threads and navigate in time in each ??? TBD

--- TEST ---

(See echo lab)

### !tt.index

Use !tt.*index* to run an indexing pass over the current trace. If the current trace is already indexed, this does nothing.

```
0:000> !tt.index
Successfully created the index in 0ms.
```

### !tt.index status

Use !tt.index status to report the status of the trace index.

```
0:000> !tt.index status
Index file loaded.
```




> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




