---
title: .echocpunum (Show CPU Number)
description: The .echocpunum command turns on or turns off the display of the processor number when you are debugging a multiprocessor target computer.
ms.assetid: a238b291-8c6e-4a4c-adc3-3be5a9916a29
keywords: ["Show CPU Number (.echocpunum) command", "multiprocessor computer, Show CPU Number (.echocpunum) command", ".echocpunum (Show CPU Number) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .echocpunum (Show CPU Number)
api_type:
- NA
---

# .echocpunum (Show CPU Number)


The **.echocpunum** command turns on or turns off the display of the processor number when you are debugging a multiprocessor target computer.

```
.echocpunum 0 
.echocpunum 1 
.echocpunum 
```

## <span id="ddk_meta_show_cpu_number_dbg"></span><span id="DDK_META_SHOW_CPU_NUMBER_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Turns off the display of the processor number.

<span id="_______1______"></span> **1**   
Turns on the display of the processor number.

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

Remarks
-------

If you use the **.echocpunum** command without any arguments, the display of processor numbers is turned on or off, and the new state is displayed.

By default, the display is turned off.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.echocpunum%20%28Show%20CPU%20Number%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




