---
title: eb, ed
description: The eb and ed extensions write a sequence of values into a specified physical address. These extension commands should not be confused with the e\\ (Enter Values) command.
ms.assetid: 368937e4-0989-4dca-983a-65bc63142108
keywords: ["eb extension", "ed extension", "memory, Write Physical ( e ) extensions", "eb, ed Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- eb, ed
api_type:
- NA
ms.localizationpriority: medium
---

# !eb, !ed


The **!eb** and **!ed** extensions write a sequence of values into a specified physical address.

These extension commands should not be confused with the [**e\* (Enter Values)**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) command.

```dbgcmd
!eb [Flag] PhysicalAddress Data [ ... ] 
!ed [Flag] PhysicalAddress Data [ ... ]
```

## <span id="ddk__e__dbg"></span><span id="DDK__E__DBG"></span>Parameters


<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Can be any one of the following values. The *Flag* value must be surrounded by square brackets:

<span id="_c_"></span><span id="_C_"></span>**\[c\]**  
Writes to cached memory.

<span id="_uc_"></span><span id="_UC_"></span>**\[uc\]**  
Writes to uncached memory.

<span id="_wc_"></span><span id="_WC_"></span>**\[wc\]**  
Writes to write-combined memory.

<span id="_______PhysicalAddress______"></span><span id="_______physicaladdress______"></span><span id="_______PHYSICALADDRESS______"></span> *PhysicalAddress*   
Specifies the first physical address on the target computer to which the data will be written, in hexadecimal.

<span id="_______Data______"></span><span id="_______data______"></span><span id="_______DATA______"></span> *Data*   
Specifies one or more values to be written sequentially into physical memory. Enter these values in hexadecimal format. For the **!eb** extension, each value must be 1 byte (two hexadecimal digits). For the **!ed** extension, each value must be one DWORD (eight hexadecimal digits). You can include any number of *Data* values on one line. To separate multiple values, use commas or spaces.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Kext.dll
Kdextx86.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To read physical memory, use the [**!d\\***](-db---dc---dd---dp---dq---du---dw.md) extensions. For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

 

 





