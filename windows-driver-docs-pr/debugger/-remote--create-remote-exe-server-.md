---
title: .remote (Create Remote.exe Server)
description: The .remote command starts a Remote.exe Server, enabling a remote connection to the current debugging session.
ms.assetid: fa3de33c-ba8c-4e9c-9899-b9a43f3195bf
keywords: ["Create Remote.exe Server (.remote) command", "remote debugging through remote.exe, Create Remote.exe Server (.remote) command", ".remote (Create Remote.exe Server) Windows Debugging"]
topic_type:
- apiref
api_name:
- .remote (Create Remote.exe Server)
api_type:
- NA
---

# .remote (Create Remote.exe Server)


The **.remote** command starts a [Remote.exe Server](starting-a-remote-exe-session.md), enabling a remote connection to the current debugging session.

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.remote%20%28Create%20Remote.exe%20Server%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




