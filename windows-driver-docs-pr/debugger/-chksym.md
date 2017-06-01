---
title: chksym
description: The chksym extension tests the validity of a module against a symbol file.
ms.assetid: 52ea75cb-44a2-4c84-a3af-b3fc027348f4
keywords: ["chksym Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- chksym
api_type:
- NA
---

# !chksym


The **!chksym** extension tests the validity of a module against a symbol file.

```
    !chksym Module [Symbol] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the name of the module by its name or base address.

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies the name of a symbol file.

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
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you do not specify a symbol filed, the loaded symbol is tested. Otherwise, if you specify a .pdb or .dbg symbol file path, the loaded symbol is tested against the loaded module.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!chksym%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




