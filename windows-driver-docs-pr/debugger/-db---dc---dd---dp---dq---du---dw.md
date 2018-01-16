---
title: db, dc, dd, dp, dq, du, dw
description: The db, dc, dd, dp, dq, du, and dw extensions display data at the specified physical address on the target computer.
ms.assetid: d34eebb7-bc91-4bff-9787-d92f74195ee1
keywords: ["db extension", "dc extension", "dd extension", "dp extension", "dq extension", "du extension", "dw extension", "memory, Display Physical ( d ) extensions", "db, dc, dd, dp, dq, du, dw Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- db, dc, dd, dp, dq, du, dw
api_type:
- NA
---

# !db, !dc, !dd, !dp, !dq, !du, !dw


The **!db**, **!dc**, **!dd**, **!dp**, **!dq**, **!du**, and **!dw** extensions display data at the specified physical address on the target computer.

These extension commands should not be confused with the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command, or with the [**!ntsdexts.dp**](-dp---ntsdexts-dp-.md) extension command.

```
!db [Caching] [-m] [PhysicalAddress] [L Size] 
!dc [Caching] [-m] [PhysicalAddress] [L Size] 
!dd [Caching] [-m] [PhysicalAddress] [L Size] 
!dp [Caching] [-m] [PhysicalAddress] [L Size] 
!dq [Caching] [-m] [PhysicalAddress] [L Size] 
!du [Caching] [-m] [PhysicalAddress] [L Size] 
!dw [Caching] [-m] [PhysicalAddress] [L Size] 
```

## <span id="ddk__d__dbg"></span><span id="DDK__D__DBG"></span>Parameters


<span id="_______Caching______"></span><span id="_______caching______"></span><span id="_______CACHING______"></span> *Caching*   
Can be any one of the following values. The *Caching* value must be surrounded by square brackets:

<span id="_c_"></span><span id="_C_"></span>**\[c\]**  
Causes this extension to read from cached memory.

<span id="_uc_"></span><span id="_UC_"></span>**\[uc\]**  
Causes this extension to read from uncached memory.

<span id="_wc_"></span><span id="_WC_"></span>**\[wc\]**  
Causes this extension to read from write-combined memory.

<span id="_______-m______"></span><span id="_______-M______"></span> **-m**   
Causes memory to be read one unit at a time. For example, **!db -m** reads memory in 8-bit chunks and **!dw -m** reads memory in 16-bit chunks. If your hardware does not support 32-bit physical memory reads, it may be necessary to use the **-m** option. This option does not affect the length or appearance of the display -- it only affects how the memory is accessed.

<span id="_______PhysicalAddress______"></span><span id="_______physicaladdress______"></span><span id="_______PHYSICALADDRESS______"></span> *PhysicalAddress*   
Specifies the first physical address to be displayed, in hexadecimal format. If this is omitted the first time this command is used, the address defaults to zero. If this is omitted on a subsequent use, the display will begin where the last display ended.

<span id="_______L_______Size______"></span><span id="_______l_______size______"></span><span id="_______L_______SIZE______"></span> **L** **** *Size*   
Specifies the number of chunks of memory to display. The size of a chunk is determined by the precise extension used.

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

To write to physical memory, use the [**!e\***](-eb---ed.md) extensions. For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

Remarks
-------

These extensions each display physical memory, but their display formats and default length differ:

-   The **!db** extension displays hexadecimal bytes and their ASCII character equivalents. The default length is 128 bytes.

-   The **!dc** extension displays DWORD values and their ASCII character equivalents. The default length is 32 DWORDs (128 total bytes).

-   The **!dd** extension displays DWORD values. The default length is 32 DWORDs (128 total bytes).

-   The **!dp** extension displays ULONG\_PTR values. These are either 32-bit or 64-bit words, depending on the instruction size. The default length is 128 total bytes.

-   The **!dq** extension displays ULONG64\_PTR values. These are 32-bit words. The default length is 128 total bytes.

-   The **!du** extension displays UNICODE characters. The default length is 16 characters (32 total bytes), or until a NULL character is encountered.

-   The **!dw** extension displays WORD values. The default length is 64 DWORDs (128 total bytes).

Consequently, using two of these extensions that are distinct with the same value of *Size* will most likely result in a difference in the total amount of memory displayed. For example, using the command **!db L 32** results in 32 bytes being displayed (as hexadecimal bytes), whereas the command **!dd L 32** results in 128 bytes being displayed (as DWORD values).

Here is an example in which the caching attribute flag is needed:

```
kd> !dc e9000
physical memory read at e9000 failed
If you know the caching attributes used for the memory,
try specifying [c], [uc] or [wc], as in !dd [c] <params>.
WARNING: Incorrect use of these flags will cause unpredictable
processor corruption. This may immediately (or at any time in
the future until reboot) result in a system hang, incorrect data
being displayed or other strange crashes and corruption.

kd> !dc [c] e9000
#   e9000 000ea002 000ea002 000ea002 000ea002 ................
#   e9010 000ea002 000ea002 000ea002 000ea002 ................
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!db,%20!dc,%20!dd,%20!dp,%20!dq,%20!du,%20!dw%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




