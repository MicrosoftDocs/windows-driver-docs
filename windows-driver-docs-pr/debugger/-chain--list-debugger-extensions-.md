---
title: .chain (List Debugger Extensions)
description: The .chain command lists all loaded debugger extensions in their default search order.
ms.assetid: 73139b02-265a-424d-9de8-f4f3736e62db
keywords: [".chain (List Debugger Extensions) Windows Debugging"]
topic_type:
- apiref
api_name:
- .chain (List Debugger Extensions)
api_type:
- NA
---

# .chain (List Debugger Extensions)


The **.chain** command lists all loaded debugger extensions in their default search order.

``` syntax
.chain
.chain /D
```

## <span id="ddk_meta_close_handle_dbg"></span><span id="DDK_META_CLOSE_HANDLE_DBG"></span>Parameters


<span id="________D______"></span><span id="________d______"></span> **/D**   
Displays the output using [Debugger Markup Language](debugger-markup-language-commands.md). In the output, each listed module is a link that you can click to get information about the extensions that are implemented by the module.

## <span id="ddk_meta_list_debugger_extensions_dbg"></span><span id="DDK_META_LIST_DEBUGGER_EXTENSIONS_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md). For details on executing extension commands and an explanation of the default search order, see [Using Debugger Extension Commands](using-debugger-extension-commands.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.chain%20%28List%20Debugger%20Extensions%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




