---
title: .ttime (Display Thread Times)
description: The .ttime command displays the running times for a thread.
ms.assetid: ff48310f-3eb9-4112-b5ab-b7c16878ac8f
keywords: [".ttime (Display Thread Times) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .ttime (Display Thread Times)
api_type:
- NA
---

# .ttime (Display Thread Times)


The **.ttime** command displays the running times for a thread.

```
    .ttime 
```

## <span id="ddk_meta_display_thread_times_dbg"></span><span id="DDK_META_DISPLAY_THREAD_TIMES_DBG"></span>


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
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86 only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This command only works in user mode. In kernel mode you should use [**!thread**](-thread.md) instead. This command works with user-mode minidumps as long as they were created with the **/mt** or **/ma** options; see [Minidumps](minidumps.md) for details.

The **.ttime** command shows the creation time of the thread, as well as the amount of time it has been running in kernel mode and in user mode.

Here is an example:

```
0:000> .ttime
Created: Sat Jun 28 17:58:42 2003
Kernel:  0 days 0:00:00.131
User:    0 days 0:00:02.109
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.ttime%20%28Display%20Thread%20Times%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




