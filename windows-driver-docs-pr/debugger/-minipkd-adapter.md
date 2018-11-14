---
title: minipkd.adapter
description: The minipkd.adapter extension displays information about the specified adapter.
ms.assetid: 86cde6f0-9690-41b6-8e81-b9d25d7d6de5
keywords: ["minipkd.adapter Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.adapter
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.adapter


The **!minipkd.adapter** extension displays information about the specified adapter.

```dbgcmd
!minipkd.adapter Address 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of an adapter.

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

The address of an adapter can be found in the **DevExt** field of the [**!minipkd.adapters**](-minipkd-adapters.md) display.

 

 





