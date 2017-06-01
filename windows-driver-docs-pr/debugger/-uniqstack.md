---
title: uniqstack
description: The uniqstack extension displays all of the stacks for all of the threads in the current process, excluding stacks that appear to have duplicates.
ms.assetid: c7502106-90b7-4fec-aa6b-394967ed2cfb
keywords: ["uniqstack Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- uniqstack
api_type:
- NA
---

# !uniqstack


The **!uniqstack** extension displays all of the stacks for all of the threads in the current process, excluding stacks that appear to have duplicates.

```
!uniqstack [ -b | -v | -p ] [ -n ]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-b______"></span><span id="_______-B______"></span> **-b**   
Causes the display to include the first three parameters passed to each function.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Causes the display to include frame pointer omission (FPO) information. On x86-based processors, the calling convention information is also displayed.

<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Causes the display to include the full parameters for each function that is called in the stack trace. This listing will include each parameter's data type, name, and value. *This requires full symbol information.*

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
Causes frame numbers to be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Uext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension is similar to the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command, except that it does not display duplicate stacks.

For example:

```
0:000> !uniqstack
Processing 14 threads, please wait

.  0  Id: f0f0f0f0.15c Suspend: 1 Teb: 00000000`7fff8000 Unfrozen
      Priority: 0
Child-SP          Child-BSP         RetAddr
00000000`0006e5e0 00000000`00070420 00000000`6b009840
00000000`0006e600 00000000`000703d0 00000000`6b03db00
00000000`0006e950 00000000`000703b0 00000000`6b008520
00000000`0006e950 00000000`00070368 00000000`6b1845e0
00000000`0006e9b0 00000000`00070310 00000000`6b009980
00000000`0006e9d0 00000000`000702d0 00000000`6b009ff0
00000000`0006e9e0 00000000`00070248 00000000`77ea4a10
00000000`0006f290 00000000`000700e0 00000000`77ea5d60
00000000`0006f4c0 00000000`00070028 00000000`77ed6000
00000000`0006f550 00000000`00070000 00000000`77ed9000
00000000`0006f550 00000000`00070000 00000000`77ca78a0
00000000`0006fff0 00000000`00070000 00000000`00000000

.  1  Id: f0f0f0f0.718 Suspend: 1 Teb: 00000000`7fff4000 Unfrozen
      Priority: 0
Child-SP          Child-BSP         RetAddr
00000000`0043eb50 00000000`00440250 00000000`6b008520
00000000`0043eb80 00000000`00440208 00000000`6b1845e0
00000000`0043ebe0 00000000`004401a8 00000000`6b009980
00000000`0043ec00 00000000`00440168 00000000`6b009ff0
00000000`0043ec10 00000000`004400e0 00000000`77ea5f50
00000000`0043f4c0 00000000`00440028 00000000`77ed6000
00000000`0043f550 00000000`00440000 00000000`77ed9000
00000000`0043f550 00000000`00440000 00000000`7de05690
00000000`0043fff0 00000000`00440000 00000000`00000000

. 13  Id: f0f0f0f0.494 Suspend: 1 Teb: 00000000`7ef98000 Unfrozen
      Priority: 0
Child-SP          Child-BSP         RetAddr
00000000`00feffe0 00000000`00ff0040 00000000`77e94f30
00000000`00feffe0 00000000`00ff0040 00000000`00000000

Total threads: 14
Duplicate callstacks: 11 (windbg thread #s follow):
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!uniqstack%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




