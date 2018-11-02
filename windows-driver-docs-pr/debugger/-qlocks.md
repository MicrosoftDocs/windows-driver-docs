---
title: qlocks
description: The qlocks extension displays the state of all queued spin locks.
ms.assetid: fdeefedb-c840-410a-94e4-ae42923e82e7
keywords: ["qlocks Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- qlocks
api_type:
- NA
ms.localizationpriority: medium
---

# !qlocks


The **!qlocks** extension displays the state of all queued spin locks.

```dbgcmd
!qlocks 
```

## <span id="ddk__qlocks_dbg"></span><span id="DDK__QLOCKS_DBG"></span>


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

For information about spin locks, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

This command is useful only on a multiprocessor system.

Here is an example:

```dbgcmd
0: kd> !qlocks
Key: O = Owner, 1-n = Wait order, blank = not owned/waiting, C = Corrupt

                       Processor Number
    Lock Name         0  1  2  3

KE   - Dispatcher               
KE   - Unused Spare             
MM   - PFN                      
MM   - System Space             
CC   - Vacb                     
CC   - Master                   
EX   - NonPagedPool             
IO   - Cancel                   
EX   - WorkQueue                
IO   - Vpb                      
IO   - Database                 
IO   - Completion               
NTFS - Struct                   
AFD  - WorkQueue                
CC   - Bcb                      
MM   - MM NonPagedPool             
```

 

 





