---
title: pciir
description: The pciir extension displays the contents of the hardware routing of peripheral component interconnect (PCI) devices to interrupt controller inputs.
ms.assetid: 83d1b716-adfe-4712-bdbb-25960c38fff0
keywords: ["PCI IRQ routing table", "peripheral component interconnect (PCI)", "pciir Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pciir
api_type:
- NA
ms.localizationpriority: medium
---

# !pciir


The **!pciir** extension displays the contents of the hardware routing of peripheral component interconnect (PCI) devices to interrupt controller inputs.

```dbgcmd
!pciir
```

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP</strong></p>
<p><strong>Windows Server 2003</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

This extension command can only be used with an x86-based target computer that does not have the Advanced Configuration and Power Interface (ACPI) enabled.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For similar information on any ACPI-enabled computer, use the [**!acpiirqarb**](-acpiirqarb.md) extension.

For information about PCI buses, see the Windows Driver Kit (WDK) documentation.

 

 





