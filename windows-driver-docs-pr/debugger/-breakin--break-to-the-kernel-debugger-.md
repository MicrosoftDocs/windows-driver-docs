---
title: .breakin (Break to the Kernel Debugger)
description: The .breakin command switches from user-mode debugging to kernel-mode debugging. This command is particularly useful when you are controlling the user-mode debugger from the kernel debugger.
ms.assetid: f0dab2c2-60f4-4a85-91bd-6379b247ceaf
keywords: [".breakin (Break to the Kernel Debugger) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .breakin (Break to the Kernel Debugger)
api_type:
- NA
ms.localizationpriority: medium
---

# .breakin (Break to the Kernel Debugger)


The **.breakin** command switches from user-mode debugging to kernel-mode debugging. This command is particularly useful when you are controlling the user-mode debugger from the kernel debugger.

```dbgcmd
    .breakin 
```

## <span id="ddk_meta_break_to_the_kernel_debugger_dbg"></span><span id="DDK_META_BREAK_TO_THE_KERNEL_DEBUGGER_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If kernel-mode debugging was enabled during the boot process and you are running a user-mode debugger, you can use the **.breakin** command to halt the operating system and transfer control to a kernel debugger.

The **.breakin** command causes a kernel-mode break in the debugger's process context. If a kernel debugger is attached, it will become active. The kernel debugger's [process context](changing-contexts.md) will automatically be set to the process of the user-mode debugger, not the user-mode debugger's target process.

This command is primarily useful when debugging a user-mode problem requires retrieving information about the kernel state of the system. Resuming execution in the kernel debugger is necessary before the user-mode debugging session can continue.

When you are [controlling the user-mode debugger from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) and the user-mode debugger prompt is visible in the kernel debugger, this command will pause the user-mode debugger and make the kernel-mode debugging prompt appear.

If the system is unable to break into the kernel debugger, an error message is displayed.

This command is also useful if you use the kernel debugger to set a breakpoint in user space and that breakpoint is caught by a user-mode debugger instead of the kernel debugger. Issuing this command in the user-mode debugger will transfer control to the kernel debugger.

If the **.breakin** command is used on a system that was not booted with debugging enabled, it has no effect.

 

 





