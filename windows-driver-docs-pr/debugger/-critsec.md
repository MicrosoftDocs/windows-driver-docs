---
title: critsec
description: The critsec extension displays a critical section.
ms.assetid: 7e30efd5-2bdc-420c-b3ed-504280ddd8f7
keywords: ["critsec Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- critsec
api_type:
- NA
ms.localizationpriority: medium
---

# !critsec


The **!critsec** extension displays a critical section.

```dbgsyntax
!critsec Address 
```

## <span id="ddk__critsec_dbg"></span><span id="DDK__CRITSEC_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the critical section.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other commands and extensions that can display critical section information, see [Displaying a Critical Section](displaying-a-critical-section.md). For information about critical sections, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

If you do not know the address of the critical section, you should use the [**!ntsdexts.locks**](-locks---ntsdexts-locks-.md) extension. This displays all critical sections that have been initialized by calling **RtlInitializeCriticalSection**.

Here is an example:

```dbgcmd
0:000> !critsec 3a8c0e9c

CritSec +3a8c0e9c at 3A8C0E9C
LockCount          1
RecursionCount     1
OwningThread       99
EntryCount         472
ContentionCount    1
*** Locked
```

 

 





