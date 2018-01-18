---
title: .endpsrv (End Process Server)
description: The .endpsrv command causes the current process server or KD connection server to close.
ms.assetid: 3f8d0a85-f0f4-4c13-ab52-e4d99ba3599c
keywords: [".endpsrv (End Process Server) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .endpsrv (End Process Server)
api_type:
- NA
---

# .endpsrv (End Process Server)


The **.endpsrv** command causes the current process server or KD connection server to close.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.endpsrv%20%28End%20Process%20Server%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




