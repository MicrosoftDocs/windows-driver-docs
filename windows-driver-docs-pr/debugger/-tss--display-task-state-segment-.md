---
title: .tss (Display Task State Segment)
description: The .tss command displays a formatted view of the saved Task State Segment (TSS) information for the current processor.
ms.assetid: 3f73b7cf-56a8-434a-bc4d-2e8ab3af9f94
keywords: ["Display Task State Segment (.tss) command", "task state segment (TSS)", "TSS (task state segment)", ".tss (Display Task State Segment) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .tss (Display Task State Segment)
api_type:
- NA
---

# .tss (Display Task State Segment)


The **.tss** command displays a formatted view of the saved Task State Segment (TSS) information for the current processor.

```
.tss [Address]
```

## <span id="ddk_meta_display_task_state_segment_dbg"></span><span id="DDK_META_DISPLAY_TASK_STATE_SEGMENT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Address of the TSS.

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

The address of the TSS can be found by examining the output of the [**!pcr**](-pcr.md) extension.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.tss%20%28Display%20Task%20State%20Segment%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




