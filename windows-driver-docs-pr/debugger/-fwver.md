---
title: fwver
description: The fwver extension displays the Itanium firmware version.
ms.assetid: 0b1a2fb2-9df6-45b4-bd5b-cbcdde38ddad
keywords: ["fwver Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- fwver
api_type:
- NA
ms.localizationpriority: medium
---

# !fwver


The **!fwver** extension displays the Itanium firmware version.

```dbgcmd
!fwver 
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## <span id="ddk__fwver_dbg"></span><span id="DDK__FWVER_DBG"></span>


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

 

This extension command can only be used with an Itanium target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, consult an Intel architecture manual.

Remarks
-------

Here is an example of the output from this extension:

```dbgcmd
kd> !fwver

Firmware Version

   Sal Revision:        0
   SAL_A_VERSION:       0
   SAL_B_VERSION:       0
   PAL_A_VERSION:       6623
   PAL_B_VERSION:       6625
   smbiosString:        W460GXBS2.86E.0117A.P08.200107261041
```

 

 





