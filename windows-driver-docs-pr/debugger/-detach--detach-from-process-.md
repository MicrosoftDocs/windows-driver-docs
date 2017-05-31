---
title: .detach (Detach from Process)
description: The .detach command ends the debugging session, but leaves any user-mode target application running.
ms.assetid: 4f0fbd8b-3037-4549-99da-be40a091a363
keywords: [".detach (Detach from Process) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .detach (Detach from Process)
api_type:
- NA
---

# .detach (Detach from Process)


The **.detach** command ends the debugging session, but leaves any user-mode target application running.

```
.detach [ /h | /n ]
```

## <span id="ddk_meta_detach_from_process_dbg"></span><span id="DDK_META_DETACH_FROM_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
Any outstanding debug event will be continued without being marked as handled.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

For live user-mode debugging, this command is only supported in Windows XP and later versions of Windows.

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

 

Remarks
-------

This command will end the debugging session in any of the following scenarios:

-   When you are debugging a user-mode or kernel-mode dump file.

-   (Windows XP and later) When you are debugging a live user-mode target.

-   When you are noninvasively debugging a user-mode target.

If you are only debugging a single target, the debugger will return to dormant mode after it detaches.

If you are [debugging multiple targets](debugging-multiple-targets.md), the debugging session will continue with the remaining targets.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.detach%20%28Detach%20from%20Process%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




