---
title: wudfext.wudfdriverinfo
description: The wudfext.wudfdriverinfo extension displays information about a UMDF driver within the current host process.
ms.assetid: 6204df00-2de5-41b6-80c1-ba576699fb20
keywords: ["wudfext.wudfdriverinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfdriverinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfdriverinfo


The **!wudfext.wudfdriverinfo** extension displays information about a UMDF driver within the current host process.

```dbgcmd
!wudfext.wudfdriverinfo Name
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Name______"></span><span id="_______name______"></span><span id="_______NAME______"></span> *Name*   
Specifies the name of the UMDF driver to display information about.

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
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

Remarks
-------

The **!wudfext.wudfdriverinfo** extension iterates through each level in each device stack and displays the driver and device information for each entry that matches the driver whose name is specified in the *Name* parameter.

You can use **!wudfext.wudfdriverinfo** to quickly find the device object for your driver.

The following is an example of the **!wudfext.wudfdriverinfo** display:

```dbgcmd
kd> !wudfdriverinfo wudfechodriver 
IWDFDriver: 0xf2db8
  !WDFDEVICE 0xf2f80
    !devstack 0x34e4e0 @ level 0
```

 

 





