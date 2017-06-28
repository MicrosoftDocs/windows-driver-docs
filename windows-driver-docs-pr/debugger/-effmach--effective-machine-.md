---
title: .effmach (Effective Machine)
description: The .effmach command displays or changes the processor mode that the debugger uses.
ms.assetid: bf4dfdc0-2f0b-416a-8bf2-0e7d81339905
keywords: ["Effective Machine (.effmach) command", ".effmach (Effective Machine) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .effmach (Effective Machine)
api_type:
- NA
---

# .effmach (Effective Machine)


The **.effmach** command displays or changes the processor mode that the debugger uses.

```
.effmach [MachineType]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______MachineType______"></span><span id="_______machinetype______"></span><span id="_______MACHINETYPE______"></span> *MachineType*   
Specifies the processor type that the debugger uses for this session. If you omit this parameter, the debugger displays the current machine type.

You can enter one of the following machine types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Machine type</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.</strong></p></td>
<td align="left"><p>Use the processor mode of the target computer's native processor mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>#</strong></p></td>
<td align="left"><p>Use the processor mode of the code that is executing for the most recent event.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>x86</strong></p></td>
<td align="left"><p>Use an x86-based processor mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>amd64</strong></p></td>
<td align="left"><p>Use an x64-based processor mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ebc</strong></p></td>
<td align="left"><p>Use an EFI byte code processor mode.</p></td>
</tr>
</tbody>
</table>

 

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

The processor mode influences many debugger features:

-   Which processor is used for stack tracing.

-   Whether the process uses 32-bit or 64-bit pointers.

-   Which processor's register set is active.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.effmach%20%28Effective%20Machine%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




