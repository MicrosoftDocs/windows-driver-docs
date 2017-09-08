---
title: Time Travel Debugging - Playback
description: This section describes how to record time travel traces.
ms.author: windowsdriverdev
ms.date: 09/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Recording 

TBD TBD TBD

This section describes how to playback time travel traces and navigate in time.

## Command time travel navigation

Use a trailing minus sign with the following version of these commands to travel back in time.

| Command  |  For more information |
|----|-------------------------------------------------------------------------------------------|
| t- | [t (Trace)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/t--trace-) |
| p- | [p (Step)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/p--step-)   |
| g- | [g (Go)](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/g--go-)       |


## Ribbon button time travel navigation

Alternatively use the ribbon buttons to navigate in the trace.

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-ribbon-buttons.png)

## Use the !tt extension to travel in time

Provide a time postion in any of the following formats to travel to that point in time.

!tt <position> - Time travel to the given position in the trace.
           
- If <position> is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !tt 0                   - Time travel to the beginning of the trace
    - !tt 50                  - Time travel to halfway through the trace
    - !tt 100                 - Time travel to the end of the trace
 

- If <position> is #:#, where # are a hexadecimal numbers,it travels to that position. If the number after : is omitted, it's defaulted to zero.
    - !tt 1A0:                - Time travel to position 1A0:0
    - !tt 1A0:0               - Time travel to position 1A0:0
    - !tt 1A0:12F             - Time travel to position 1A0:12F

- If the : is omitted, then the second number must have precisely 16 hexadecimal digits, with zeros for left-padding.
    - !tt 1A0000000000000012F - Time travel to position 1A0:12F


## Example TTD Playback

This outputs shows... TBD 

```
0:000> !tt
Setting position to the beginning of the trace
Setting position: 10:0
(4604.21dc): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 10:0
ntdll!ZwTestAlert+0x14:
00007ffc`61f789d4 c3              ret
```



> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




