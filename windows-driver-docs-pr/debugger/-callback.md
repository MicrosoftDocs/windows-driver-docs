---
title: callback
description: The callback extension displays the callback data related to the trap for the specified thread.
ms.assetid: afbd7884-d63d-4e37-a437-91bc910a3ae2
keywords: ["callback data for system traps", "callback Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- callback
api_type:
- NA
ms.localizationpriority: medium
---

# !callback


The **!callback** extension displays the callback data related to the trap for the specified thread.

```dbgsyntax
!callback Address [Number]
```

## <span id="ddk__callback_dbg"></span><span id="DDK__CALLBACK_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the thread. If this is -1 or omitted, the current thread is used.

<span id="_______Number______"></span><span id="_______number______"></span><span id="_______NUMBER______"></span> *Number*   
Specifies the number of the desired callback frame. This frame is noted in the display.

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

 

This extension command can only be used with an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about system traps, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

If the system has not experienced a system trap, this extension will not produce useful data.

 

 





