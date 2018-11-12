---
title: diskspace
description: The diskspace extension displays the amount of free space on a hard disk of the target computer.
ms.assetid: 9153cdc0-addf-4804-a898-1e4280ac60ea
keywords: ["diskspace Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- diskspace
api_type:
- NA
ms.localizationpriority: medium
---

# !diskspace


The **!diskspace** extension displays the amount of free space on a hard disk of the target computer.

```dbgcmd
!diskspace Drive[:]
```

## <span id="ddk__diskspace_dbg"></span><span id="DDK__DISKSPACE_DBG"></span>Parameters


<span id="_______Drive______"></span><span id="_______drive______"></span><span id="_______DRIVE______"></span> *Drive*   
Specifies the drive letter of the disk. The colon (:) after *Drive* is optional.

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

 

Remarks
-------

Here is an example:

```dbgcmd
kd> !diskspace c:
Checking Free Space for c: ..........
   Cluster Size 0 KB
 Total Clusters 4192901 KB
  Free Clusters 1350795 KB
    Total Space 1 GB (2096450 KB)
     Free Space 659.567871 MB (675397 KB)

kd> !diskspace f:
Checking Free Space for f: 
f: is a CDROM drive. This function is not supported!
```

 

 





