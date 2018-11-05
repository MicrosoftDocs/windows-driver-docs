---
title: wudfext.wudffile
description: The wudfext.wudffile extension displays information about a framework file.
ms.assetid: f655703d-0e61-4e9c-a033-834a89ef6d05
keywords: ["wudfext.wudffile Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wudfext.wudffile
api_type:
- NA
ms.localizationpriority: medium
---

# !wudfext.wudffile


The **!wudfext.wudffile** extension displays information about a framework file.

```dbgcmd
!wudfext.wudffile pWDFFile [TypeName] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______pWDFFile______"></span><span id="_______pwdffile______"></span><span id="_______PWDFFILE______"></span> *pWDFFile*   
Specifies the address of the **IWDFFile** interface to display information about.

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

 

 





