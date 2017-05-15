---
title: .remote\_exit (Exit Debugging Client)
description: The .remote\_exit command exits the debugging client but does not end the debugging session.
ms.assetid: 9e15a842-6864-4ff9-97bc-f6cc8549a422
keywords: ["Exit Debugging Client (.remote_exit) command", "remote debugging through the debugger, Exit Debugging Client (.remote_exit) command", ".remote_exit (Exit Debugging Client) Windows Debugging"]
topic_type:
- apiref
api_name:
- .remote_exit (Exit Debugging Client)
api_type:
- NA
---

# .remote\_exit (Exit Debugging Client)


The **.remote\_exit** command exits the debugging client but does not end the debugging session.

``` syntax
.remote_exit [FinalCommands]
```

## <span id="ddk_meta_exit_debugging_client_dbg"></span><span id="DDK_META_EXIT_DEBUGGING_CLIENT_DBG"></span>Parameters


<span id="_______FinalCommands______"></span><span id="_______finalcommands______"></span><span id="_______FINALCOMMANDS______"></span> *FinalCommands*   
Specifies a command string to pass to the debugging server. You should separate multiple commands by using semicolons. These commands are passed to the debugging server and the connection is then broken.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

You can use the **.remote\_exit** command only in a script file. You can use it in KD and CDB, but you cannot use it in WinDbg.

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

For more information about script files, see [Using Script Files](using-script-files.md). For more information about debugging clients and debugging servers, see [Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md).

Remarks
-------

If you are using KD or CDB directly, instead of using a script, you can exit from the debugging client by using the [**CTRL+B**](ctrl-b--quit-local-debugger-.md) key.

You cannot exit from a debugging client through a script that is executed in WinDbg.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.remote_exit%20%28Exit%20Debugging%20Client%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




