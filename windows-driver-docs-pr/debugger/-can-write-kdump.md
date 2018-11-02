---
title: can_write_kdump
description: The can_write_kdump extension verifies that there is enough disk space on the target computer to write a kernel dump file of the specified type.
ms.assetid: e9fdf8a4-3294-4625-a854-5e42a69374a6
keywords: ["kernel dump", "can_write_kdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- can_write_kdump
api_type:
- NA
ms.localizationpriority: medium
---

# !can\_write\_kdump


The **!can\_write\_kdump** extension verifies that there is enough disk space on the target computer to write a kernel dump file of the specified type.

```dbgsyntax
!can_write_kdump [-dn] [Options]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-dn______"></span><span id="_______-DN______"></span> **-dn**   
Specifies that the file system on the target computer is an NTFS file system. If this parameter is omitted, then the amount of disk free space cannot be determined, and a warning will be shown. However, the amount of space required will still be displayed.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
The following options are valid:

<span id="-t"></span><span id="-T"></span>**-t**  
Specifies that the extension should determine if there is enough space for a minidump.

<span id="-s"></span><span id="-S"></span>**-s**  
Specifies that the extension should determine if there is enough space for a summary kernel dump. This is the default value.

<span id="-f"></span><span id="-F"></span>**-f**  
Specifies that the extension should determine if there is enough space for a full kernel dump.

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

If no *Option* is specified, then the extension will determine if there is enough space for a summary kernel dump.

In the following example, the file system is not specified:

```dbgcmd
kd> !can_write_kdump
Checking kernel summary dump...
WARNING: Can't predict how many pages will be used, assuming worst-case.
Physical memory: 285560 KB
Page file size: 1572864 KB
NO: Page file too small
```

 

 





