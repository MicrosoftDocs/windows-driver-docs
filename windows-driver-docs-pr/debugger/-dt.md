---
title: dt
description: The dt extension displays information about a CSR thread.This extension command should not be confused with the dt (Display Type) command.
ms.assetid: 7fbca028-8d11-42b5-b64e-41eb3edc56cc
keywords: ["dt Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dt
api_type:
- NA
ms.localizationpriority: medium
---

# !dt


The **!dt** extension displays information about a CSR thread.

This extension command should not be confused with the [**dt (Display Type)**](dt--display-type-.md) command.

```dbgcmd
!dt [v] CSR-Thread 
```

## <span id="ddk__dt_dbg"></span><span id="DDK__DT_DBG"></span>Parameters


<span id="_______v______"></span><span id="_______V______"></span> **v**   
Verbose mode.

<span id="_______CSR-Thread______"></span><span id="_______csr-thread______"></span><span id="_______CSR-THREAD______"></span> *CSR-Thread*   
Specifies the hexadecimal address of the CSR thread.

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

 

Remarks
-------

This extension displays the thread, process, client ID, flags, and reference count associated with the CSR thread. If verbose mode is selected, the display will also include list pointers, thread handle, and the wait block.

## <span id="see_also"></span>See also


[**!dp (!ntsdexts.dp)**](-dp---ntsdexts-dp-.md)

 

 






