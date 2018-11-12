---
title: defwrites
description: The defwrites extension displays the values of the kernel variables used by the cache manager.
ms.assetid: da576e05-3d9f-4599-bf8e-b1fa05093d77
keywords: ["cache manager", "defwrites Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- defwrites
api_type:
- NA
ms.localizationpriority: medium
---

# !defwrites


The **!defwrites** extension displays the values of the kernel variables used by the cache manager.

```dbgcmd
!defwrites
```dbgcmd

## <span id="ddk__defwrites_dbg"></span><span id="DDK__DEFWRITES_DBG"></span>


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

For information about write throttling, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

For information about other cache management extensions, use the [**!cchelp**](-cchelp.md) extension.

Remarks
-------

When the number of deferred writes ("dirty pages") becomes too large, page writing will be throttled. This extension allows you to see whether your system has reached this point.

Here is an example:

```dbgcmd
kd> !defwrites 
*** Cache Write Throttle Analysis ***

        CcTotalDirtyPages:                   0 (       0 Kb)
        CcDirtyPageThreshold:             1538 (    6152 Kb)
        MmAvailablePages:                 2598 (   10392 Kb)
        MmThrottleTop:                     250 (    1000 Kb)
        MmThrottleBottom:                   30 (     120 Kb)
        MmModifiedPageListHead.Total:      699 (    2796 Kb)

Write throttles not engaged
```

In this case, there are no dirty pages. If **CcTotalDirtyPages** reaches 1538 (the value of **CcDirtyPageThreshold**), writing will be delayed until the number of dirty pages is reduced.

 

 





