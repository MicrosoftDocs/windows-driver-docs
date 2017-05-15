---
title: .lines (Toggle Source Line Support)
description: The .lines command enables or disables support for source-line information.
ms.assetid: 5d923592-7aba-42a0-893b-2c6621e4b87f
keywords: [".lines (Toggle Source Line Support) Windows Debugging"]
topic_type:
- apiref
api_name:
- .lines (Toggle Source Line Support)
api_type:
- NA
---

# .lines (Toggle Source Line Support)


The **.lines** command enables or disables support for source-line information.

``` syntax
    .lines [-e|-d|-t]
```

## <span id="ddk_meta_toggle_source_line_support_dbg"></span><span id="DDK_META_TOGGLE_SOURCE_LINE_SUPPORT_DBG"></span>Parameters


<span id="_______-e______"></span><span id="_______-E______"></span> **-e**   
Enables source line support.

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Disables source line support.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
Turns source line support on or off. If you do not specify parameters for **.lines**, the default behavior of the **.lines** command is this switching of source line support.

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

For more information about source debugging and related commands, see [Debugging in Source Mode](debugging-in-source-mode.md).

Remarks
-------

You must enable source line support before you can perform source-level debugging. This support enables the debugger to load source line symbols.

You can enable source line support by using the **.lines** command or the [-lines command-line option](command-line-options.md). If source line support is already enabled, using the **.lines** command disables this support.

By default, if you do not use the **.lines** command, WinDbg turns on source line support, and console debuggers (KD, CDB, NTSD) turn off the support. For more information about how to change this setting, see [Setting Symbol Options](symbol-options.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.lines%20%28Toggle%20Source%20Line%20Support%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




