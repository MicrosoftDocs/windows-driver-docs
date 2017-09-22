---
title: Time Travel Debugging - Replay a trace
description: This section describes how to replay time travel traces.
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Replay a trace 

This section describes how to replay time travel traces, navigating forwards and backwards in time.

## Command time travel navigation

Use a trailing minus sign with the following commands to travel back in time.

| Command  |  For more information |
|----|-------------------------------------------------------------------------------------------|
| t- | [t (Trace)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/t--trace-) |
| p- | [p (Step)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/p--step-)   |
| g- | [g (Go)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/g--go-)       |

## Ribbon button time travel navigation

Alternatively, use the ribbon buttons to navigate in the trace.

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-ribbon-buttons.png)


## Example TTD Trace Replay

Use the g- command to reset the time position to the beginning of the TTD trace. 

```
0:000> g-
TTD: Start of trace reached.
(3f78.4274): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 29:0
ntdll!ZwTestAlert+0x14:
00007ffc`61f789d4 c3              ret
```

Use the [p (Step)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/p--step-) command to step forward in a TTD trace. 

```
0:000> p
Time Travel Position: 29:1
ntdll!_LdrpInitialize+0x96:
00007ffc`61f49bc6 4c8d5c2450      lea     r11,[rsp+50h]
0:000> p
Time Travel Position: 29:B
ntdll!LdrpInitialize+0x3b:
00007ffc`61f49b1b 488b5c2430      mov     rbx,qword ptr [rsp+30h] ss:000000a3`e827f360=000000a3e827f3b0
0:000> p
Time Travel Position: 29:F
ntdll!LdrInitializeThunk+0xe:
00007ffc`61f49ace b201            mov     dl,1
```

You an also use the [t (Trace)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/t--trace-) command to navigate in the trace.

```
0:000> t
Time Travel Position: 29:12
ntdll!ZwContinue:
00007ffc`61f75bf0 4c8bd1          mov     r10,rcx
0:000> t
Time Travel Position: 2B:0
ntdll!RtlUserThreadStart:
00007ffc`61f40d30 4883ec48        sub     rsp,48h
```


Use the the p- command to step backwards in a TTD trace. 

```
0:000> p-
Time Travel Position: 2A:0
ntdll!ZwContinue+0x12:
00007ffc`61f75c02 0f05            syscall
0:000> p-
Time Travel Position: 29:11
ntdll!LdrInitializeThunk+0x13:
00007ffc`61f49ad3 e818c10200      call    ntdll!ZwContinue (00007ffc`61f75bf0)
0:000> p-
TTD: Start of trace reached.
(3f78.4274): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 29:0
ntdll!ZwTestAlert+0x14:
00007ffc`61f789d4 c3              ret
```

You can also use the t- command to navigate backwards in time.


## !tt navigation commands

Use the !tt command to navigate forward or backwards in time, by skiping to a given position in the trace. 

!tt {position}

Provide a time position in any of the following formats to travel to that point in time.
           
- If {position} is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:


     - !tt 0                   - Time travel to the beginning of the trace
     - !tt 50                  - Time travel to halfway through the trace
     - !tt 100                 - Time travel to the end of the trace

- If {position} is #:#, where # are a hexadecimal numbers, it travels to that position. If the number after : is omitted, it defaults to zero.
    - !tt 1A0:                - Time travel to position 1A0:0
    - !tt 1A0:0               - Time travel to position 1A0:0
    - !tt 1A0:12F             - Time travel to position 1A0:12F


   > [!NOTE]
   > Traces use a two part instruction position that references a specific position reference in the trace, for example 12:0. or 15:7. The two elements are hexadecimal numbers defined as described here.
   >
   > xx:yy
   > 
   > xx- the first element is the sequencing number, which corresponds to a sequencing event.
   >
   > yy - the second element is a step count, which corresponds roughly to the instruction count since the sequencing event.


## !positions

Use ```!positions``` to display all the active threads, including their position in the trace.

```
1:0:000> !positions
>Thread ID=0x3604 - Position: 20:0
 Thread ID=0x0A94 - Position: 612:0
 Thread ID=0x1D78 - Position: A89:0
 Thread ID=0x38F8 - Position: 1695:0
 Thread ID=0x0AC4 - Position: 172C:0
 Thread ID=0x1D8C - Position: 17B5:0
 Thread ID=0x35FC - Position: 743D:0
 Thread ID=0x3200 - Position: 7D56:0
```
This example shows that there are eight threads at the current position. The current thread is 3604, marked with '>'.  

> [!TIP] 
> Another way to display the current list of threads with positions is to use the a data model command for example:
>
> ```dx -g @$curprocess.Threads.Select(t => new { IsCurrent = t.Id == @$curthread.Id, ThreadId = t.Id, Position = t.TTD.Position })```
>

Use the user mode [~ (Thread Status)](---thread-status-.md) command shows the same eight threads, and marks the current thread with '.':

```
1:0:000> ~
.  0  Id: 3f4.3604 Suspend: 4096 Teb: 00000061`79804000 Unfrozen
   1  Id: 3f4.a94 Suspend: 4096 Teb: 00000061`79806000 Unfrozen
   2  Id: 3f4.1d78 Suspend: 4096 Teb: 00000061`7980a000 Unfrozen
   3  Id: 3f4.38f8 Suspend: 4096 Teb: 00000061`7980e000 Unfrozen
   4  Id: 3f4.ac4 Suspend: 4096 Teb: 00000061`79810000 Unfrozen
   5  Id: 3f4.1d8c Suspend: 4096 Teb: 00000061`79812000 Unfrozen
   6  Id: 3f4.35fc Suspend: 4096 Teb: 00000061`79814000 Unfrozen
   7  Id: 3f4.3200 Suspend: 4096 Teb: 00000061`79808000 Unfrozen
```

Click on the link next to the third thread (1D78) in the !positions output, to time travel to that position in the trace, A89:0.

```
1:0:001> !tt A89:0
Setting position: A89:0
ModLoad: 00007ff8`3cd00000 00007ff8`3ce45000   C:\WINDOWS\System32\ole32.dll
(3f4.1d78): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: A89:0
ntdll!ZwWaitForWorkViaWorkerFactory+0x14:
00007ff8`3ed88c34 c3              ret
```

Use the [~ (Thread Status)](---thread-status-.md) command to confirm that we are now positioned at the third thread, 1D78.

```
1:0:002> ~
   0  Id: 3f4.3604 Suspend: 4096 Teb: 00000061`79804000 Unfrozen
   1  Id: 3f4.a94 Suspend: 4096 Teb: 00000061`79806000 Unfrozen
.  2  Id: 3f4.1d78 Suspend: 4096 Teb: 00000061`7980a000 Unfrozen
   3  Id: 3f4.38f8 Suspend: 4096 Teb: 00000061`7980e000 Unfrozen
   4  Id: 3f4.ac4 Suspend: 4096 Teb: 00000061`79810000 Unfrozen
   5  Id: 3f4.1d8c Suspend: 4096 Teb: 00000061`79812000 Unfrozen
   6  Id: 3f4.35fc Suspend: 4096 Teb: 00000061`79814000 Unfrozen
   7  Id: 3f4.3200 Suspend: 4096 Teb: 00000061`79808000 Unfrozen
```

## Time travel debugging extension utility commands

Use the following travel debugging extension utility commands to work with TTD traces.


### !index

Use ```!index``` to run an indexing pass over the current trace and to display the status of the index. For more information, see [Time Travel Debugging - !index (time travel)](time-travel-debugging-extension-index.md).

 
## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

[Time Travel Debugging - Record a trace](time-travel-debugging-recording.md)

[Time Travel Debugging - Working with trace files](time-travel-debugging-trace-files.md)

[Time Travel Debugging - Sample App Walkthrough](time-travel-debugging-walkthrough.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




