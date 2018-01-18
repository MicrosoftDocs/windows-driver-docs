---
title: cpuid
description: The cpuid extension displays information about the processors on the system.
ms.assetid: 3dbd1079-d129-4e17-8d06-18b25fdd17c9
keywords: ["cpuid Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- cpuid
api_type:
- NA
---

# !cpuid


The **!cpuid** extension displays information about the processors on the system.

```
!cpuid [Processor]
```

## <span id="ddk__cpuid_dbg"></span><span id="DDK__CPUID_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor whose information will be displayed. If you omit this parameter, all processors are displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

Remarks
-------

The **!cpuid** extension works during live user-mode or kernel-mode debugging, local kernel debugging, and debugging of dump files. However, user-mode minidump files contain only information about the active processor.

If you are debugging in user mode, the **!cpuid** extension describes the computer that the target application is running on. In kernel mode, it describes the target computer.

The following example shows this extension.

```
kd> !cpuid 
CP  F/M/S  Manufacturer        MHz 
 0  6,5,1  GenuineIntel        700 
 1  8,1,5  AuthenticAMD        700 
```

The **CP** column gives the processor number. (These numbers are always sequential, starting with zero). The **Manufacturer** column specifies the processor manufacturer. The **MHz** column specifies the processor speed, if it is available.

For an x86-based processor or an x64-based processor, the **F** column displays the processor family number, the **M** column displays the processor model number, and the **S** column displays the stepping size.

For an Itanium-based processor, the **M** column displays the processor model number, the R column displays the processor revision number, the **F** column displays the processor family number, and the **A** column displays the architecture revision number.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!cpuid%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




