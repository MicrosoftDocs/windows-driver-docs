---
title: poolfind
description: The poolfind extension finds all instances of a specific pool tag in either nonpaged or paged memory pools.
ms.assetid: 01783b6b-0117-49ca-87ca-bbe3c1b0e730
keywords: ["poolfind Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- poolfind
api_type:
- NA
ms.localizationpriority: medium
---

# !poolfind


The **!poolfind** extension finds all instances of a specific pool tag in either nonpaged or paged memory pools.

```dbgcmd
!poolfind TagString [PoolType] 
!poolfind TagValue [PoolType] 
```

## <span id="ddk__poolfind_dbg"></span><span id="DDK__POOLFIND_DBG"></span>Parameters


<span id="_______TagString______"></span><span id="_______tagstring______"></span><span id="_______TAGSTRING______"></span> *TagString*   
Specifies the pool tag. *TagString* is a case-sensitive ASCII string. The asterisk (\*) can be used to represent any number of characters; the question mark (?) can be used to represent exactly one character. Unless an asterisk is used, *TagString* must be exactly four characters in length.

<span id="_______TagValue______"></span><span id="_______tagvalue______"></span><span id="_______TAGVALUE______"></span> *TagValue*   
Specifies the pool tag. *TagValue* must begin with "0x", even if the default radix is 16. If this parameter begins with any other value (including "0X") it will be interpreted as an ASCII tag string.

<span id="_______PoolType______"></span><span id="_______pooltype______"></span><span id="_______POOLTYPE______"></span> *PoolType*   
Specifies the type of pool to be searched. The following values are permitted:

<span id="0"></span>0  
Specifies nonpaged memory pool. This is the default.

<span id="1"></span>1  
Specifies paged memory pool.

<span id="2"></span>2  
Specifies the special pool.

<span id="4"></span>4  
(Windows XP and later) Specifies the session pool.

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

For information about memory pools and pool tags, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

This command can take a significant amount of time to execute, depending on the size of pool memory that must be searched. To speed up this execution, increase the COM port speed with the [**CTRL+A (Toggle Baud Rate)**](ctrl-a--toggle-baud-rate-.md) key, or use the [**.cache (Set Cache Size)**](-cache--set-cache-size-.md) command to increase the cache size (to approximately 10 MB).

The pool tag is the same tag passed to the **ExAllocate***Xxx* family of routines.

Here is an example. The entire nonpaged pool is searched and then the paged pool is searched, but the command is terminated before completion (after an hour of operation):

```dbgcmd
kd> !poolfind SeSd 0

Scanning large pool allocation table for Tag: SeSd (827d1000 : 827e9000)

Searching NonPaged pool (823b1000 : 82800000) for Tag: SeSd

826fa130 size:   c0 previous size:   40  (Allocated) SeSd
82712000 size:   c0 previous size:    0  (Allocated) SeSd
82715940 size:   a0 previous size:   60  (Allocated) SeSd
8271da30 size:   c0 previous size:   10  (Allocated) SeSd
82721c00 size:   10 previous size:   30  (Free)      SeSd
8272b3f0 size:   60 previous size:   30  (Allocated) SeSd
8272d770 size:   60 previous size:   40  (Allocated) SeSd
8272d7d0 size:   a0 previous size:   60  (Allocated) SeSd
8272d960 size:   a0 previous size:   70  (Allocated) SeSd
82736f30 size:   a0 previous size:   10  (Allocated) SeSd
82763840 size:   a0 previous size:   10  (Allocated) SeSd
8278b730 size:  100 previous size:  290  (Allocated) SeSd
8278b830 size:   10 previous size:  100  (Free)      SeSd
82790130 size:   a0 previous size:   20  (Allocated) SeSd
82799180 size:   a0 previous size:   10  (Allocated) SeSd
827c00e0 size:   a0 previous size:   30  (Allocated) SeSd
827c8320 size:   a0 previous size:   60  (Allocated) SeSd
827ca180 size:   a0 previous size:   50  (Allocated) SeSd
827ec140 size:   a0 previous size:   10  (Allocated) SeSd

Searching NonPaged pool (fe7c3000 : ffbe0000) for Tag: SeSd

kd> !poolfind SeSd 1

Scanning large pool allocation table for Tag: SeSd (827d1000 : 827e9000)

Searching Paged pool (e1000000 : e4400000) for Tag: SeSd

e10000b0 size:   d0 previous size:   20  (Allocated) SeSd
e1000260 size:   d0 previous size:   60  (Allocated) SeSd
......
e1221dc0 size:   a0 previous size:   60  (Allocated) SeSd
e1224250 size:   a0 previous size:   30  (Allocated) SeSd

...terminating - searched pool to e1224000
kd> 
```

 

 





