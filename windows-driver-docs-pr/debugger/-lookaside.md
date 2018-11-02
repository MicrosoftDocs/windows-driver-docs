---
title: lookaside
description: The lookaside extension displays information about look-aside lists, resets the counters of look-aside lists, or modifies the depth of a look-aside list.
ms.assetid: ec343563-f293-4ddf-96c8-69fc7b9b4377
keywords: ["lookaside list", "lookaside Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- lookaside
api_location:
- Kdexts.dll
api_type:
- DllExport
ms.localizationpriority: medium
---

# !lookaside


The **!lookaside** extension displays information about look-aside lists, resets the counters of look-aside lists, or modifies the depth of a look-aside list.

```dbgcmd
!lookaside [Address [Options [Depth]]]
!lookaside [-all]
!lookaside 0 [-all]
```

## <span id="ddk__lookaside_dbg"></span><span id="DDK__LOOKASIDE_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of a look-aside list to be displayed or modified.

If *Address* is omitted (or 0) and the **-all** option is not specified, a set of well-known, standard system look-aside lists is displayed. The set of lists is not exhaustive; that is, it does not include all system look-aside lists. Also, the set does not include custom look-aside lists that were created by calls to [**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309) or [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301).

If *Address* is omitted (or 0) and the **-all** option is specified, all look-aside lists are displayed.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Controls what operation will be taken. The following possible *Options* are supported. The default is zero:

<span id="0"></span>0  
Displays information about the specified look-aside list or lists.

<span id="1"></span>1  
Resets the counters of the specified look-aside list.

<span id="2"></span>2  
Modifies the depth of the specified look-aside list. This option can only be used if *Address* is nonzero.

<span id="_______Depth______"></span><span id="_______depth______"></span><span id="_______DEPTH______"></span> *Depth*   
Specifies the new maximum depth of the specified look-aside list. This parameter is permitted only if *Address* is nonzero and *Options* is equal to 2.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about look-aside lists, see the [Windows Driver Kit (WDK) documentation](https://go.microsoft.com/fwlink/p/?linkid=201141) and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Look-aside lists are multiprocessor-safe mechanisms for managing pools of fixed-size entries from either paged or nonpaged memory.

Look-aside lists are efficient, because the routines do not use spin locks on most platforms.

Note that if the current depth of a look-aside list exceeds the maximum depth of that list, then freeing a structure associated with that list will result in freeing it into pool memory, rather than list memory.

Here is an example of the output from this extension:

```dbgcmd
!lookaside 0xfffff88001294f80

Lookaside "" @ 0xfffff88001294f80  Tag(hex): 0x7366744e "Ntfs"
    Type           =       0011  PagedPool RaiseIfAllocationFailure
    Current Depth  =          0  Max Depth  =          4
    Size           =        496  Max Alloc  =       1984
    AllocateMisses =          8  FreeMisses =          0
    TotalAllocates =     272492  TotalFrees =     272488
    Hit Rate       =         99% Hit Rate   =        100%
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">Kdexts.dll</td>
</tr>
</tbody>
</table>

 

 





