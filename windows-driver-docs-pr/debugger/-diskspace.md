---
title: diskspace
description: The diskspace extension displays the amount of free space on a hard disk of the target computer.
ms.assetid: 9153cdc0-addf-4804-a898-1e4280ac60ea
keywords: ["diskspace Windows Debugging"]
topic_type:
- apiref
api_name:
- diskspace
api_type:
- NA
---

# !diskspace


The **!diskspace** extension displays the amount of free space on a hard disk of the target computer.

``` syntax
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

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!diskspace%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




