---
title: .endpsrv (End Process Server)
description: The .endpsrv command causes the current process server or KD connection server to close.
ms.assetid: 3f8d0a85-f0f4-4c13-ab52-e4d99ba3599c
keywords: [".endpsrv (End Process Server) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .endpsrv (End Process Server)
api_type:
- NA
ms.localizationpriority: medium
---

# .endpsrv (End Process Server)


The **.endpsrv** command causes the current process server or KD connection server to close.

```dbgcmd
.endpsrv 
```

## <span id="ddk_meta_end_process_server_dbg"></span><span id="DDK_META_END_PROCESS_SERVER_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use this command only when you are performing remote debugging through a process server or KD connection server.

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

For more information about these servers, see [Process Servers (User Mode)](process-servers--user-mode-.md) or [KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md)

Remarks
-------

The **.endpsrv** command terminates the process server or KD connection server currently connected to your smart client.

If you wish to terminate a process server or KD connection server from the computer on which it is running, use Task Manager to end the process (dbgsrv.exe or kdsrv.exe).

The **.endpsrv** command can terminate a process server or KD connection server, but it cannot terminate a debugging server. For information on how to do that, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

 

 





