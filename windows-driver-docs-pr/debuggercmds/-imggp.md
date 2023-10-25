---
title: imggp (WinDbg)
description: The imggp extension displays the global pointer (GP) directory entry value for a 64-bit image.
keywords: ["global pointer (GP)", "GP (global pointer)", "imggp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- imggp
api_type:
- NA
---

# !imggp


The **!imggp** extension displays the global pointer (GP) directory entry value for a 64-bit image.

```dbgcmd
!imggp Address 
```

## <span id="ddk__imggp_dbg"></span><span id="DDK__IMGGP_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the base address of the image.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

 

 





