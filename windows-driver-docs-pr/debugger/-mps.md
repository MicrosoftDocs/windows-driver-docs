---
title: mps
description: The mps extension displays BIOS information for the Intel Multiprocessor Specification (MPS) of the target computer.
ms.assetid: b6ee2eac-ef3c-403a-83ca-fe45506a8c4e
keywords: ["mps Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- mps
api_type:
- NA
ms.localizationpriority: medium
---

# !mps


The **!mps** extension displays BIOS information for the Intel Multiprocessor Specification (MPS) of the target computer.

```dbgcmd
!mps [Address] 
```

## <span id="ddk__mps_dbg"></span><span id="DDK__MPS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the MPS table in the BIOS. If this is omitted, the information is obtained from the HAL. This will require HAL symbols.

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

For more information about BIOS debugging, see [Debugging BIOS Code](debugging-bios-code.md). For more information about the MPS, refer to the appropriate version of the Intel MultiProcessor Specification.

 

 





