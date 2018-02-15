---
title: so (Set Kernel Debugging Options)
description: The so command sets or displays the kernel debugging options.
ms.assetid: b40260c7-6e60-4198-988f-bcafecb165bc
keywords: ["so (Set Kernel Debugging Options) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- so (Set Kernel Debugging Options)
api_type:
- NA
---

# so (Set Kernel Debugging Options)


The **so** command sets or displays the kernel debugging options.

```
so [Options] 
```

## <span id="ddk_cmd_set_kernel_debugging_options_dbg"></span><span id="DDK_CMD_SET_KERNEL_DEBUGGING_OPTIONS_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
One or more of the following options:

<span id="NOEXTWARNING"></span><span id="noextwarning"></span>**NOEXTWARNING**  
Does not issue a warning when the debugger cannot find an extension command.

<span id="NOVERSIONCHECK"></span><span id="noversioncheck"></span>**NOVERSIONCHECK**  
Does not check the version of debugger extension DLLs.

If you omit *Options*, the current options are displayed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
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

 

Remarks
-------

You can also set kernel debugging options using the \_NT\_DEBUG\_OPTIONS [environment variable](kernel-mode-environment-variables.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20so%20%28Set%20Kernel%20Debugging%20Options%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




