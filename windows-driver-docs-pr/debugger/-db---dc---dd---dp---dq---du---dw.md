---
title: db, dc, dd, dp, dq, du, dw
description: The db, dc, dd, dp, dq, du, and dw extensions display data at the specified physical address on the target computer.
ms.assetid: d34eebb7-bc91-4bff-9787-d92f74195ee1
keywords: ["db extension", "dc extension", "dd extension", "dp extension", "dq extension", "du extension", "dw extension", "memory, Display Physical ( d ) extensions", "db, dc, dd, dp, dq, du, dw Windows Debugging"]
ms.author: domars
ms.date: 01/18/2017
topic_type:
- apiref
api_name:
- db, dc, dd, dp, dq, du, dw
api_type:
- NA
ms.localizationpriority: medium
---

# !db, !dc, !dd, !dp, !dq, !du, !dw


The **!db**, **!dc**, **!dd**, **!dp**, **!dq**, **!du**, and **!dw** extensions display data at the specified physical address on the target computer.

These extension commands should not be confused with the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command, or with the [**!ntsdexts.dp**](-dp---ntsdexts-dp-.md) extension command.

```dbgcmd
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

### <span id="DLL"></span><span id="dll"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Mode</strong></p></td>
<td align="left"><p>Kernel Mode</p></td>
</tr>
</tbody>
</table>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To write to physical memory, use the [**!e\\***](-eb---ed.md) extensions. For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](reading-and-writing-memory.md).

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

```dbgcmd
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

 

 





