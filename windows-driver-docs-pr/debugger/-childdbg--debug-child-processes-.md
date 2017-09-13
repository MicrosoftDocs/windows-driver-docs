---
title: .childdbg (Debug Child Processes)
description: The .childdbg command controls the debugging of child processes.
ms.assetid: 87d70d3b-d9d5-4a37-b8a7-1616ba78b2f3
keywords: [".childdbg (Debug Child Processes) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .childdbg (Debug Child Processes)
api_type:
- NA
---

# .childdbg (Debug Child Processes)


The **.childdbg** command controls the debugging of child processes.

```
.childdbg 0 
.childdbg 1 
.childdbg 
```

## <span id="ddk_meta_debug_child_processes_dbg"></span><span id="DDK_META_DEBUG_CHILD_PROCESSES_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Prevents the debugger from debugging child processes.

<span id="_______1______"></span> **1**   
Causes the debugger to debug child processes.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is only supported in Windows XP and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86, x64, and Itanium only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

**Child processes** are additional processes launched by the original target application.

With no parameters, **.childdbg** will display the current status of child-process debugging.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.childdbg%20%28Debug%20Child%20Processes%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




