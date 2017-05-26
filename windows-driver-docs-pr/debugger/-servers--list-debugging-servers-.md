---
title: .servers (List Debugging Servers)
description: The .servers command lists all debugging servers that have been established by this debugger.
ms.assetid: bf65c6f7-9c59-4756-a667-8b896bd7ea2a
keywords: ["List Debugging Servers (.servers) command", "remote debugging through the debugger, List Debugging Servers (.servers) command", ".servers (List Debugging Servers) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .servers (List Debugging Servers)
api_type:
- NA
---

# .servers (List Debugging Servers)


The **.servers** command lists all debugging servers that have been established by this debugger.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.servers%20%28List%20Debugging%20Servers%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




