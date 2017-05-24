---
title: .abandon (Abandon Process)
description: The .abandon command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.
ms.assetid: e44ae9b8-b6a2-4648-911d-61ff3c94527c
keywords: [".abandon (Abandon Process) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .abandon (Abandon Process)
api_type:
- NA
---

# .abandon (Abandon Process)


The **.abandon** command ends the debugging session, but leaves the target application in a debugging state. This returns the debugger to dormant mode.

``` syntax
    .abandon [/h|/n] 
```

## <span id="ddk_meta_abandon_process_dbg"></span><span id="DDK_META_ABANDON_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Any outstanding debug event will be continued unhandled.

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
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

If the target is left in a debugging state, a new debugger can be attached to it. See [Re-attaching to the Target Application](reattaching-to-the-target-application.md) for details. However, after a process has been abandoned once, it can never be restored to a running state without a debugger attached.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.abandon%20%28Abandon%20Process%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




