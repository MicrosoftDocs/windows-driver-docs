---
title: ld (Load Symbols)
description: The ld command loads symbols for the specified module and updates all module information.
ms.assetid: 1dae519f-8dd1-4f30-98f4-fe904454c84c
keywords: ["ld (Load Symbols) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ld (Load Symbols)
api_type:
- NA
---

# ld (Load Symbols)


The **ld** command loads symbols for the specified module and updates all module information.

```
ld ModuleName [/f FileName]
```

## <span id="ddk_cmd_load_symbols_dbg"></span><span id="DDK_CMD_LOAD_SYMBOLS_DBG"></span>Parameters


<span id="_______ModuleName______"></span><span id="_______modulename______"></span><span id="_______MODULENAME______"></span> *ModuleName*   
Specifies the name of the module whose symbols are to be loaded. *ModuleName* can contain a variety of wildcard characters and specifiers.

<span id="________f_______FileName______"></span><span id="________f_______filename______"></span><span id="________F_______FILENAME______"></span> **/f** *FileName*   
Changes the name selected for the match. By default the module name is matched, but when **/f** is used the file name is matched instead of the module name. *FileName* can contain a variety of wildcard characters and specifiers. For more information on the syntax of wildcard characters and specifiers, see [String Wildcard Syntax](string-wildcard-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The debugger's default behavior is to use *lazy symbol loading* (also known as [deferred symbol loading](deferred-symbol-loading.md)). This means that symbols are not actually loaded until they are needed.

The **ld** command, on the other hand, forces all symbols for the specified module to be loaded.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about deferred (lazy) symbol loading, see [Deferred Symbol Loading](deferred-symbol-loading.md). For more information about other symbol options, see [Setting Symbol Options](symbol-options.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ld%20%28Load%20Symbols%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




