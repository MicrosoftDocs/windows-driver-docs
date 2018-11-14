---
title: minipkd.srb
description: The minipkd.srb extension displays the specified SCSI request block (SRB) data structure.
ms.assetid: d742a900-f8a8-43a8-b00a-12bb82ca1460
keywords: ["minipkd.srb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.srb
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.srb


The **!minipkd.srb** extension displays the specified SCSI request block (SRB) data structure.

```dbgcmd
!minipkd.srb SRB 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______SRB______"></span><span id="_______srb______"></span> *SRB*   
Specifies the address of an SRB.

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
<td align="left"><p>Minipkd.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [SCSI Miniport Debugging](scsi-miniport-debugging.md).

Remarks
-------

The addresses of all currently active requests can be found in the *SRB* fields of the output from the [**!minipkd.req**](-minipkd-req.md) command.

This extension displays the status of the SRB, the driver it is addressed to, the SCSI that issued the SRB and its address, and a hexadecimal flag value. If 0x10000 is set in the flag value, this request is currently in the miniport.

 

 





