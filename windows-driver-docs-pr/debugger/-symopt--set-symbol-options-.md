---
title: .symopt (Set Symbol Options)
description: The .symopt command sets or displays the symbol options.
ms.assetid: 0793baa3-14f7-48df-8773-736b6a5470e6
keywords: [".symopt (Set Symbol Options) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .symopt (Set Symbol Options)
api_type:
- NA
---

# .symopt (Set Symbol Options)


The **.symopt** command sets or displays the symbol options.

```
.symopt+ Flags 
.symopt- Flags 
.symopt 
```

## <span id="ddk_meta_set_symbol_options_dbg"></span><span id="DDK_META_SET_SYMBOL_OPTIONS_DBG"></span>Parameters


<span id="______________"></span> **+**   
Causes the symbol options specified by *Flags* to be set. If **.symopt** is used with *Flags* but no plus or minus sign, a plus sign is assumed.

<span id="_______-______"></span> **-**   
Causes the symbol options specified by *Flags* to be cleared.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the symbol options to be changed. *Flags* must be the sum of the bit flags of these symbol options.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a list and description of each symbol option, its bit flag, and other methods of setting and clearing these options, see [Setting Symbol Options](symbol-options.md).

Remarks
-------

Without any arguments, **.symopt** displays the current symbol options.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.symopt%20%28Set%20Symbol%20Options%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




