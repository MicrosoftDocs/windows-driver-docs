---
title: wudfext.wudfusbpipe
description: The wudfext.wudfusbpipe extension displays information about a USB pipe object.
ms.assetid: a80f01e1-9c2c-4674-a067-0ff7e006713a
keywords: ["wudfext.wudfusbpipe Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfusbpipe
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfusbpipe


The **!wudfext.wudfusbpipe** extension displays information about a USB pipe object.

```dbgcmd
!wudfext.wudfusbpipe pWDFUSBPipe TypeName
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pWDFUSBPipe______"></span><span id="_______pwdfusbpipe______"></span><span id="_______PWDFUSBPIPE______"></span> *pWDFUSBPipe*   
Specifies the address of the **IWDFUsbTargetPipe** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFUsbTargetPipe**.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

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
<td align="left"><p><strong>Windows XP with UMDF version 1.7 and later</strong></p></td>
<td align="left"><p>Wudfext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [User-Mode Driver Framework Debugging](user-mode-driver-framework-debugging.md).

 

 





