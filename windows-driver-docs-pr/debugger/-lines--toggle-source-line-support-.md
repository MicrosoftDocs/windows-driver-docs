---
title: .lines (Toggle Source Line Support)
description: The .lines command enables or disables support for source-line information.
ms.assetid: 5d923592-7aba-42a0-893b-2c6621e4b87f
keywords: [".lines (Toggle Source Line Support) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .lines (Toggle Source Line Support)
api_type:
- NA
ms.localizationpriority: medium
---

# .lines (Toggle Source Line Support)


The **.lines** command enables or disables support for source-line information.

```dbgcmd
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

 

 





