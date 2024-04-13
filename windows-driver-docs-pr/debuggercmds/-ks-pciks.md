---
title: "!ks.pciks (WinDbg)"
description: "The !ks.pciks extension lists functional devices for kernel streaming devices that are attached to the PCI bus. Optionally, it can display information about active streams on those functional devices."
keywords: ["!ks.pciks Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ks.pciks
api_type:
- NA
---

# !ks.pciks


The **!ks.pciks** extension lists functional devices for kernel streaming devices that are attached to the PCI bus. Optionally, it can display information about active streams on those functional devices.

```dbgcmd
!ks.pciks [Flags] [Level] 
```

## Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to be displayed. *Flags* can be any combination of the following bits.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
List all currently running streams.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Recurse graphs to find non-PCI devices.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Display a list of proxy instances.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Display currently queued Irps.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Display information about all streams.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
Display active stream formats.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional, and applicable only to flag combinations that cause data to be displayed. Levels are the same as those for [**!ks.dump**](-ks-dump.md).

## DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information, see [Kernel Streaming Debugging](../debugger/kernel-streaming-debugging.md).

## Remarks

This command may take time to execute, especially if the ACPI filter driver is loaded, or if Driver Verifier is enabled and driver names are paged out.

Here is an example of the **!ks.pciks** display:

```dbgcmd
kd> !pciks
1 Kernel Streaming FDOs found:
    Functional Device 82a17690 [\Driver\smwdm]
```

