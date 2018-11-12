---
title: wudfext.wudfiotarget
description: The wudfext.wudfiotarget extension displays information about an I/O target including the target's state and list of sent requests.
ms.assetid: ccd241d6-c9c8-4518-902c-f119cf5b73fe
keywords: ["wudfext.wudfiotarget Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudfiotarget
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudfiotarget


The **!wudfext.wudfiotarget** extension displays information about an I/O target including the target's state and list of sent requests.

```dbgcmd
!wudfext.wudfiotarget pWDFTarget TypeName
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pWDFTarget______"></span><span id="_______pwdftarget______"></span><span id="_______PWDFTARGET______"></span> *pWDFTarget*   
Specifies the address of the **IWDFIoTarget** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFIoTarget**.

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

 

 





