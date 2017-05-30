---
title: ur (Unassemble Real Mode BIOS)
description: The ur command displays an assembly translation of the specified 16-bit real-mode code.
ms.assetid: 7ea3421a-3841-47ea-ab40-99d10516bb14
keywords: ["ur (Unassemble Real Mode BIOS) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ur (Unassemble Real Mode BIOS)
api_type:
- NA
---

# ur (Unassemble Real Mode BIOS)


The **ur** command displays an assembly translation of the specified 16-bit real-mode code.

```
ur Range 
ur Address
ur 
```

## <span id="ddk_cmd_unassemble_real_mode_bios_dbg"></span><span id="DDK_CMD_UNASSEMBLE_REAL_MODE_BIOS_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range that contains the instructions to disassemble. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the beginning of the memory range to disassemble. Eight instructions (on an x86-based processor) or nine instructions (on an Itanium-based processor) are unassembled. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug BIOS code, see [Debugging BIOS Code](debugging-bios-code.md).

Remarks
-------

If you do not specify *Range* or *Address*, the disassembly begins at the current address and extends eight instructions (on an x86-based processor) or nine instructions (on an Itanium-based processor).

If you are examining 16-bit real-mode code on an x86-based processor, both the **ur** command and the [**u (Unassemble)**](u--unassemble-.md) command give correct results.

However, if real-mode code exists in a location where the debugger is not expecting it (for example, a non-x86 computer that is running or emulating x86-based BIOS code from a plug-in card), you must use **ur** to correctly disassemble this code.

If you use **ur** on 32-bit or 64-bit code, the command tries to disassemble the code as if it were 16-bit code. This situation produces meaningless results.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ur%20%28Unassemble%20Real%20Mode%20BIOS%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




