---
title: minipkd.req
description: The minipkd.req extension displays information about all of the currently active requests on the specified adapter or device.
ms.assetid: 5edc00dd-9a0b-4576-a3ec-11ce22163e95
keywords: ["minipkd.req Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.req
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.req


The **!minipkd.req** extension displays information about all of the currently active requests on the specified adapter or device.

```dbgcmd
!minipkd.req Adapter 
!minipkd.req Device 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Adapter______"></span><span id="_______adapter______"></span><span id="_______ADAPTER______"></span> *Adapter*   
Specifies the address of the adapter.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the physical device object (PDO) for the Logical Unit Extension (LUN) device.

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

The PDO for a LUN can be found in the **DevObj** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display.

 

 





