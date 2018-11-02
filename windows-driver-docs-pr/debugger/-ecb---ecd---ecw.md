---
title: ecb, ecd, ecw
description: The ecb, ecd, and ecw extensions write to the PCI configuration space.
ms.assetid: ab5f5164-7666-48ac-aeba-5f238c2625f6
keywords: ["ecb, ecd, ecw Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ecb, ecd, ecw
api_type:
- NA
ms.localizationpriority: medium
---

# !ecb, !ecd, !ecw


The **!ecb**, **!ecd**, and **!ecw** extensions write to the PCI configuration space.

```dbgcmd
!ec Bus.Device.Function Offset Data 
```

## <span id="ddk__ec__dbg"></span><span id="DDK__EC__DBG"></span>Parameters


<span id="_______Bus______"></span><span id="_______bus______"></span><span id="_______BUS______"></span> *Bus*   
Specifies the bus. *Bus* can range from 0 to 0xFF.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the slot device number for the device.

<span id="_______Function______"></span><span id="_______function______"></span><span id="_______FUNCTION______"></span> *Function*   
Specifies the slot function number for the device.

<span id="_______Offset______"></span><span id="_______offset______"></span><span id="_______OFFSET______"></span> *Offset*   
Specifies the address at which to write.

<span id="_______Data______"></span><span id="_______data______"></span><span id="_______DATA______"></span> *Data*   
Specifies the value to be written. For the **!ecb** extension, *Data* must be 1 byte (two hexadecimal digits). For the **!ecw** extension, *Data* must be one WORD (four hexadecimal digits). For the **!ecd** extension, *Data* must be one DWORD (eight hexadecimal digits).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>

 

These extension commands can only be used with an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command, and some additional examples. For information about PCI buses, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

You cannot use these extension commands to write a sequence of *Data* values. This can only be done by repeated use of this extension.

To display the PCI configuration space, use [**!pci 100**](-pci.md)*Bus Device Function*.

 

 





