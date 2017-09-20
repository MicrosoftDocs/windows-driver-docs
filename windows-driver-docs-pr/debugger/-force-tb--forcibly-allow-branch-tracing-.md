---
title: .force_tb (Forcibly Allow Branch Tracing)
description: The .force_tb command forces the processor to trace branches early in the boot process.
ms.assetid: ac4aabfa-6d00-4478-9c13-213bf89f613a
keywords: [".force_tb (Forcibly Allow Branch Tracing) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .force_tb (Forcibly Allow Branch Tracing)
api_type:
- NA
---

# .force\_tb (Forcibly Allow Branch Tracing)


The **.force\_tb** command forces the processor to trace branches early in the boot process.

```
.force_tb 
```

## <span id="ddk_meta_forcibly_allow_branch_tracing_dbg"></span><span id="DDK_META_FORCIBLY_ALLOW_BRANCH_TRACING_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

 

Remarks
-------

Typically, branch tracing is enabled after the debugger initializes the processor control block (PRCB). This initialization occurs early in the boot process.

However, if you have to use the [**tb (Trace to Next Branch)**](tb--trace-to-next-branch-.md) command before this initialization, you can use the **.force\_tb** command to enable branch tracing earlier. Use this command carefully because it can corrupt your processor state.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.force_tb%20%28Forcibly%20Allow%20Branch%20Tracing%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




