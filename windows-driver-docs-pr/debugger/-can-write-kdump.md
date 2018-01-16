---
title: can_write_kdump
description: The can_write_kdump extension verifies that there is enough disk space on the target computer to write a kernel dump file of the specified type.
ms.assetid: e9fdf8a4-3294-4625-a854-5e42a69374a6
keywords: ["kernel dump", "can_write_kdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- can_write_kdump
api_type:
- NA
---

# !can\_write\_kdump


The **!can\_write\_kdump** extension verifies that there is enough disk space on the target computer to write a kernel dump file of the specified type.

```
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

```
kd> !can_write_kdump
Checking kernel summary dump...
WARNING: Can't predict how many pages will be used, assuming worst-case.
Physical memory: 285560 KB
Page file size: 1572864 KB
NO: Page file too small
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!can_write_kdump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




