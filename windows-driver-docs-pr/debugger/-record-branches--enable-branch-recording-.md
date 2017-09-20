---
title: .record_branches (Enable Branch Recording)
description: The .record_branches command enables the recording of branches that the target's code executed.
ms.assetid: 522eeba5-b6c5-473c-9c8e-8ef4c941079f
keywords: ["Enable Branch Recording (.record_branches) command", ".record_branches (Enable Branch Recording) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .record_branches (Enable Branch Recording)
api_type:
- NA
---

# .record\_branches (Enable Branch Recording)


The **.record\_branches** command enables the recording of branches that the target's code executed.

```
.record_branches {1|0} 
.record_branches
```

## <span id="ddk_meta_enable_branch_recording_dbg"></span><span id="DDK_META_ENABLE_BRANCH_RECORDING_DBG"></span>


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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x64-based only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **.record\_branches 1** command enables the recording of branches in the target's code. The **.record\_branches 0** command disables this recording.

Without parameters, **.record\_branches** displays the current status of this setting.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.record_branches%20%28Enable%20Branch%20Recording%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




