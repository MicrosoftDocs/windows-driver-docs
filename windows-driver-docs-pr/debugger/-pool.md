---
title: pool extension command
description: The pool extension displays information about a specific pool allocation or about the entire system-wide pool.
ms.assetid: 1c224e0c-d50c-487e-8238-9be054368ac2
keywords: ["pool", "pooltag.txt file", "pool tag", "memory, pool tag", "pool Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pool
api_type:
- NA
ms.localizationpriority: medium
---

# !pool


The **!pool** extension displays information about a specific pool allocation or about the entire system-wide pool.

```dbgcmd
!pool [Address [Flags]]
```

## <span id="ddk__pool_dbg"></span><span id="DDK__POOL_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the pool entry to be displayed. If *Address* is -1, this command displays information about all heaps in the process.

If *Address* is 0 or omitted, this command displays information about the process heap.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail to be used. This can be any combination of the following bit values; the default is zero:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to include the pool contents, not just the pool headers.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to suppress pool header information for all pools, except the one that actually contains the specified *Address*.

<span id="Bit_31__0x80000000_"></span><span id="bit_31__0x80000000_"></span><span id="BIT_31__0X80000000_"></span>Bit 31 (0x80000000)  
(Windows XP and later) Suppresses the description of the pool type and pool tag in the display.

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
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about memory pools, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

In Windows XP and later versions of Windows, the **!pool** extension displays the pool tag associated with each allocation. The owner of that pool tag is also displayed. This display is based on the contents of the pooltag.txt file. This file is located in the triage subdirectory of your Debugging Tools for Windows installation. If you want , you can edit this file to add additional pool tags relevant to your project.

**Warning**   If you install an updated version of Debugging Tools for Windows in the same directory as the current version, it overwrites all of the files in that directory, including pooltag.txt. If you modify or replace the sample pooltag.txt file, be sure to save a copy of it to a different directory. After reinstalling the debuggers, you can copy the saved pooltag.txt over the default version.

 

If the **!pool** extension reports pool corruption, you should use [**!poolval**](-poolval.md) to investigate.

Here is an example. If *Address* specifies 0xE1001050, the headers of all pools in this block are displayed, and 0xE1001050 itself is marked with an asterisk (\*).

```dbgcmd
kd> !pool e1001050 
 e1001000 size:   40 previous size:    0  (Allocated)  MmDT
 e1001040 size:   10 previous size:   40  (Free)       Mm  
*e1001050 size:   10 previous size:   10  (Allocated) *ObDi
 e1001060 size:   10 previous size:   10  (Allocated)  ObDi
 e1001070 size:   10 previous size:   10  (Allocated)  Symt
 e1001080 size:   40 previous size:   10  (Allocated)  ObDm
 e10010c0 size:   10 previous size:   40  (Allocated)  ObDi
.....
```

In this example, the right-most column shows the pool tag. The column to the left of this shows whether the pool is free or allocated.

The following command shows the pool headers and pool contents:

```dbgcmd
kd> !pool e1001050 1
 e1001000 size:   40 previous size:    0  (Allocated)  MmDT
 e1001008  ffffffff 0057005c 004e0049 004f0044
    e1001018  ffffffff 0053005c 00730079 00650074

 e1001040 size:   10 previous size:   40  (Free)       Mm  
 e1001048  ffffffff e1007ba8 e1501a58 01028101
    e1001058  ffffffff 00000000 e1000240 01028101

*e1001050 size:   10 previous size:   10  (Allocated) *ObDi
 e1001058  ffffffff 00000000 e1000240 01028101
    e1001068  ffffffff 00000000 e10009c0 01028101

 e1001060 size:   10 previous size:   10  (Allocated)  ObDi
 e1001068  ffffffff 00000000 e10009c0 01028101
    e1001078  ffffffff 00000000 00000000 04028101

......
```

 

 





