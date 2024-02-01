---
title: wudfext.wudfusbinterface
description: The wudfext.wudfusbinterface extension displays information about a USB interface object.
keywords: ["wudfext.wudfusbinterface Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfusbinterface
api_type:
- NA
---

# !wudfext.wudfusbinterface


The **!wudfext.wudfusbinterface** extension displays information about a USB interface object.

```dbgcmd
!wudfext.wudfusbinterface pWDFUSBInterface TypeName
```

## Parameters


<span id="_______pWDFUSBInterface______"></span><span id="_______pwdfusbinterface______"></span><span id="_______PWDFUSBINTERFACE______"></span> *pWDFUSBInterface*   
Specifies the address of the **IWDFUsbInterface** interface to display information about. The [**!wudfext.wudfobject**](-wudfext-wudfobject.md) extension command determines the address of **IWDFUsbInterface**.

<span id="_______TypeName______"></span><span id="_______typename______"></span><span id="_______TYPENAME______"></span> *TypeName*   
Optional. Specifies the type of the interface (for example, **IWDFDevice**). If a value for *TypeName* is supplied, the extension uses the value as the type of the interface. If an asterisk (\*) is supplied as *TypeName*, or if *TypeName* is omitted, the extension attempts to automatically determine the type of the supplied interface.

## DLL

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

 

### Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

 

 





