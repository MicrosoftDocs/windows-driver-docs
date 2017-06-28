---
title: .crash (Force System Crash)
description: The .crash command causes the target computer to issue a bug check.
ms.assetid: 625d174d-7011-4b15-aad7-1b39aa3742a4
keywords: [".crash (Force System Crash) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .crash (Force System Crash)
api_type:
- NA
---

# .crash (Force System Crash)


The **.crash** command causes the target computer to issue a bug check.

```
.crash
```

## <span id="ddk_meta_force_system_crash_dbg"></span><span id="DDK_META_FORCE_SYSTEM_CRASH_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
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

For an overview of related commands and a description of the options available after a system crash, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

Remarks
-------

This command will immediately cause the target computer to crash.

If you are already in a bug check handler, do not use **.crash**. Use [**g (Go)**](g--go-.md) instead to continue execution of the handler, which will generate a crash dump.

A kernel-mode dump file will be written if crash dumps have been enabled. See [Creating a Kernel-Mode Dump File](creating-a-kernel-mode-dump-file.md) for details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.crash%20%28Force%20System%20Crash%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




