---
title: ss (Set Symbol Suffix)
description: The ss command sets or displays the current suffix value that is used for symbol matching in numeric expressions.
ms.assetid: acf4cf2e-5b09-4d46-aa42-e539ee968685
keywords: ["ss (Set Symbol Suffix) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ss (Set Symbol Suffix)
api_type:
- NA
---

# ss (Set Symbol Suffix)


The **ss** command sets or displays the current suffix value that is used for symbol matching in numeric expressions.

```
    ss [a|w|n] 
```

## <span id="ddk_cmd_set_symbol_suffix_dbg"></span><span id="DDK_CMD_SET_SYMBOL_SUFFIX_DBG"></span>Parameters


<span id="_______a______"></span><span id="_______A______"></span> **a**   
Specifies that the symbol suffix should be "A", matching many ASCII symbols.

<span id="_______w______"></span><span id="_______W______"></span> **w**   
Specifies that the symbol suffix should be "W", matching many Unicode symbols.

<span id="_______n______"></span><span id="_______N______"></span> **n**   
Specifies that the debugger should not use a symbol suffix. (This parameter is the default behavior.)

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about symbol matching, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

Remarks
-------

If you specify the **ss** command together with no parameters, the current state of the suffix value is displayed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ss%20%28Set%20Symbol%20Suffix%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




