---
title: ready
description: The ready extension displays summary information about each thread in the system in a READY state.
ms.assetid: 1dc94ceb-7d06-4874-999c-059c86f51ea0
keywords: ["thread, ready threads", "ready Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ready
api_type:
- NA
ms.localizationpriority: medium
---

# !ready


The **!ready** extension displays summary information about each thread in the system in a READY state.

```dbgcmd
!ready [Flags]
```

## <span id="ddk__ready_dbg"></span><span id="DDK__READY_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail to display. *Flags* can be any combination of the following bits. If *Flags* is 0, only a minimal amount of information is displayed. The default is 0x6.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the thread's wait states.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
If this is included without Bit 1 (0x2), this has no effect. If this is included along with Bit 1, the thread is displayed with a stack trace.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
(Windows XP and later) Causes the display of each function to include the return address, the stack pointer, and (on Itanium systems) the **bsp** register value. The display of function arguments is suppressed.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
(Windows XP and later) Causes the display of each function to include only the return address; arguments and stack pointers are suppressed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about thread scheduling and the READY state, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The output from this extension is similar to that of [**!thread**](-thread.md), except that only ready threads are displayed, and they are sorted in order of decreasing priority.

 

 





