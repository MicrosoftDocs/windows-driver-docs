---
title: .sleep (Pause Debugger)
description: The .sleep command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger.
ms.assetid: bc3ee17f-e3b8-4bdb-8c80-6b1fef29000e
keywords: ["Pause Debugger (.sleep) command", "controlling the user-mode debugger from the kernel debugger, Pause Debugger (.sleep) command", ".sleep (Pause Debugger) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .sleep (Pause Debugger)
api_type:
- NA
---

# .sleep (Pause Debugger)


The **.sleep** command causes the user-mode debugger to pause and the target computer to become active. This command is only used when you are controlling the user-mode debugger from the kernel debugger.

```
.sleep milliseconds
```

## <span id="ddk_meta_pause_debugger_dbg"></span><span id="DDK_META_PAUSE_DEBUGGER_DBG"></span>Parameters


<span id="_______milliseconds______"></span><span id="_______MILLISECONDS______"></span> *milliseconds*   
Specifies the length of the pause, in milliseconds.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>controlling the user-mode debugger from the kernel debugger</p></td>
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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details and information about how to wake up a debugger in sleep mode, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

Remarks
-------

When you are controlling the user-mode debugger from the kernel debugger, and the user-mode debugger prompt is visible in the kernel debugger, this command will activate sleep mode. The kernel debugger, the user-mode debugger, and the target application will all freeze, but the rest of the target computer will become active.

If you use this command in any other scenario, it will simply freeze the debugger for a period of time.

The sleep time is in milliseconds and interpreted according to the default radix, unless a prefix such as **0n** is used. Thus, if the default radix is 16, the following command will cause about 65 seconds of sleep:

```
0:000> .sleep 10000
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.sleep%20%28Pause%20Debugger%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




