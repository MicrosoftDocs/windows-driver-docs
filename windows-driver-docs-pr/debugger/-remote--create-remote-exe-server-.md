---
title: .remote (Create Remote.exe Server)
description: The .remote command starts a Remote.exe Server, enabling a remote connection to the current debugging session.
ms.assetid: fa3de33c-ba8c-4e9c-9899-b9a43f3195bf
keywords: ["Create Remote.exe Server (.remote) command", "remote debugging through remote.exe, Create Remote.exe Server (.remote) command", ".remote (Create Remote.exe Server) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .remote (Create Remote.exe Server)
api_type:
- NA
ms.localizationpriority: medium
---

# .remote (Create Remote.exe Server)


The **.remote** command starts a [Remote.exe Server](starting-a-remote-exe-session.md), enabling a remote connection to the current debugging session.

```dbgcmd
.remote session
```

## <span id="ddk_meta_create_remote_exe_server_dbg"></span><span id="DDK_META_CREATE_REMOTE_EXE_SERVER_DBG"></span>Parameters


<span id="_______session______"></span><span id="_______SESSION______"></span> *session*   
Specifies a name that you give to the debugging session.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use the **.remote** command in KD and CDB, but you cannot use it in WinDbg.

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

For more information about how to use Remote.exe Servers and Remote.exe Clients, see [Remote Debugging Through Remote.exe](remote-debugging-through-remote-exe.md).

Remarks
-------

The **.remote** command creates a Remote.exe process and turns the current debugger into a Remote.exe Server. This server enables a Remote.exe Client to connect to the current debugging session.

 

 





