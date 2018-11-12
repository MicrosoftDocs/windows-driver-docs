---
title: minipkd.portconfig
description: The minipkd.portconfig extension displays information about the specified PORT_CONFIGURATION_INFORMATION data structure.
ms.assetid: efc527c4-0340-4976-9126-d3e32286fc64
keywords: ["minipkd.portconfig Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- minipkd.portconfig
api_type:
- NA
ms.localizationpriority: medium
---

# !minipkd.portconfig


The **!minipkd.portconfig** extension displays information about the specified PORT\_CONFIGURATION\_INFORMATION data structure.

```dbgcmd
!minipkd.portconfig PortConfig 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______PortConfig______"></span><span id="_______portconfig______"></span><span id="_______PORTCONFIG______"></span> *PortConfig*   
Specifies the address of a PORT\_CONFIGURATION\_INFORMATION data structure.

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

The *PortConfig* address can be found in the **Port Config Info** field of the [**!minipkd.adapter**](-minipkd-adapter.md) display.

 

 





