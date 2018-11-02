---
title: locks ntsdexts.locks
description: The locks extension in Ntsdexts.dll displays a list of critical sections associated with the current process.This extension command should not be confused with the kdext*.locks extension command.
ms.assetid: f33a68e8-1ddc-4d49-bb22-8f8b097c8ada
keywords: ["locks ( ntsdexts.locks) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- locks ( ntsdexts.locks)
api_type:
- NA
ms.localizationpriority: medium
---

# !locks (!ntsdexts.locks)


The **!locks** extension in Ntsdexts.dll displays a list of critical sections associated with the current process.

This extension command should not be confused with the [**!kdext\*.locks**](-locks---kdext--locks-.md) extension command.

```dbgcmd
    !locks [Options] 
```

## <span id="ddk__ntsdexts_locks_dbg"></span><span id="DDK__NTSDEXTS_LOCKS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies the amount of information to be displayed. Any combination of the following options can be used:

<span id="-v"></span><span id="-V"></span>**-v**  
Causes the display to include all critical sections, even those that are not currently owned.

<span id="-o"></span><span id="-O"></span>**-o**  
(Windows XP and later) Causes the display to only include orphaned information (pointers that do not actually point to valid critical sections).

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

This extension command shows all critical sections that have been initialized by calling **RtlInitializeCriticalSection**. If there are no critical sections, then no output will result.

Here is an example:

```dbgcmd
0:000> !locks

CritSec w3svc!g_pWamDictator+a0 at 68C2C298
LockCount          0
RecursionCount     1
OwningThread       d1
EntryCount         1
ContentionCount    0
*** Locked

CritSec SMTPSVC+66a30 at 67906A30
LockCount          0
RecursionCount     1
OwningThread       d0
EntryCount         1
ContentionCount    0
*** Locked
```

 

 





