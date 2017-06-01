---
title: .write\_cmd\_hist (Write Command History)
description: The .write\_cmd\_hist command writes the entire history of the Debugger Command window to a file.
ms.assetid: 7d512f0c-56cd-48e5-b618-d5615113f065
keywords: [".write_cmd_hist (Write Command History) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .write_cmd_hist (Write Command History)
api_type:
- NA
---

# .write\_cmd\_hist (Write Command History)


The **.write\_cmd\_hist** command writes the entire history of the Debugger Command window to a file.

```
.write_cmd_hist Filename 
```

## <span id="ddk_meta_cmd_hist_write_command_history_dbg"></span><span id="DDK_META_CMD_HIST_WRITE_COMMAND_HISTORY_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies the path and filename of the file that will be created.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is available only in WinDbg and cannot be used in script files.

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.write_cmd_hist%20%28Write%20Command%20History%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




