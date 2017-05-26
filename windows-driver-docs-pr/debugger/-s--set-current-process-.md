---
title: s (Set Current Process)
description: The s command sets or displays the current process number.
ms.assetid: 6b4d8e00-426c-496b-9c52-c60faeb0c975
keywords: ["s (Set Current Process) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- s (Set Current Process)
api_type:
- NA
---

# |s (Set Current Process)


The **|s** command sets or displays the current process number.

Do not confuse this command with the [**s (Search Memory)**](s--search-memory-.md), [**~s (Change Current Processor)**](-s--change-current-processor-.md), [**~s (Set Current Thread)**](-s--set-current-thread-.md), or [**||s (Set Current System)**](--s--set-current-system-.md) command.

``` syntax
|Process s 
| s 
```

## <span id="ddk_cmd_set_current_process_dbg"></span><span id="DDK_CMD_SET_CURRENT_PROCESS_DBG"></span>Parameters


<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the process to set or display. For more information about the syntax, see [Process Syntax](process-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
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

For more information about other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify processes only in user mode.

If you use the **|s** syntax, the debugger displays information about the current process.

This command also disassembles the current instruction for the current system, process, and thread.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20|s%20%28Set%20Current%20Process%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




