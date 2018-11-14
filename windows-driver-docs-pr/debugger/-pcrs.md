---
title: pcrs
description: The pcrs extension displays the Intel Itanium-specific processor control registers.
ms.assetid: 45a84a95-86df-4176-ba30-ac93b509f7f7
keywords: ["processor control register (PCR)", "PCR (processor control register)", "pcrs Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pcrs
api_type:
- NA
ms.localizationpriority: medium
---

# !pcrs


The **!pcrs** extension displays the Intel Itanium-specific processor control registers.

```dbgcmd
!pcrs Address
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a processor control registers file.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an Itanium-based target computer.

Remarks
-------

Do not confuse the **!pcrs** extension with the [**!pcr**](-pcr.md) extension, which displays the current status of the processor control region.

 

 





