---
title: .servers (List Debugging Servers)
description: The .servers command lists all debugging servers that have been established by this debugger.
ms.assetid: bf65c6f7-9c59-4756-a667-8b896bd7ea2a
keywords: ["List Debugging Servers (.servers) command", "remote debugging through the debugger, List Debugging Servers (.servers) command", ".servers (List Debugging Servers) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .servers (List Debugging Servers)
api_type:
- NA
ms.localizationpriority: medium
---

# .servers (List Debugging Servers)


The **.servers** command lists all debugging servers that have been established by this debugger.

```dbgcmd
.servers 
```

## <span id="ddk_meta_list_debugging_servers_dbg"></span><span id="DDK_META_LIST_DEBUGGING_SERVERS_DBG"></span>


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

For full details on debugging servers, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

Remarks
-------

The output of the **.servers** command lists all the debugging servers started by the debugger on which this command is issued. The output is formatted so that it can be used literally as the argument for the -remote command-line option or pasted into the WinDbg dialog box.

Each debugging server is identified by a unique ID. This ID can be used as the argument for the [**.endsrv (End Debugging Server)**](-endsrv--end-debugging-server-.md) command, if you wish to terminate the debugging server.

The **.servers** command does not list debugging servers started on this computer by different instances of the debugger, nor does it list process servers or KD connection servers.

 

 





