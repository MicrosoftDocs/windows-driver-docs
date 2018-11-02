---
title: minipkd.lun
description: The minipkd.lun extension displays detailed information about the specified Logical Unit Extension (LUN).
ms.assetid: f78b2c15-ecfc-4138-b595-a6e3f0f7f93c
keywords: ["minipkd.lun Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.lun
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.lun


The **!minipkd.lun** extension displays detailed information about the specified Logical Unit Extension (LUN).

```dbgcmd
!minipkd.lun LUN 
!minipkd.lun Device 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______LUN______"></span><span id="_______lun______"></span> *LUN*   
Specifies the address of the LUN.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the physical device object (PDO) for the LUN.

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

A LUN is typically referred to as a *device*. Thus, this extension displays information about a device on an adapter.

The LUN can be specified either by its address (which can be found in the **LUN** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display), or by its physical device object (which can be found in the **DevObj** field of the **!minipkd.adapters** display).

 

 





