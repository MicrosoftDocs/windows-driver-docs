---
title: driveinfo
description: The driveinfo extension displays volume information for the specified drive.
ms.assetid: cc63c07a-4556-4b79-9dff-c0ac09371651
keywords: ["driveinfo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- driveinfo
api_type:
- NA
ms.localizationpriority: medium
---

# !driveinfo


The **!driveinfo** extension displays volume information for the specified drive.

```dbgcmd
!driveinfo Drive[:] 
!driveinfo 
```dbgcmd

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Drive______"></span><span id="_______drive______"></span><span id="_______DRIVE______"></span> *Drive*   
Specifies a drive. The colon at the end of the drive name is optional.

<span id="_______No_parameters______"></span><span id="_______no_parameters______"></span><span id="_______NO_PARAMETERS______"></span> *No parameters*   
Displays some brief Help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The drive information displayed by this extension is obtained by querying the underlying file system; for example:

```dbgcmd
kd> !driveinfo c:
Drive c:, DriveObject e136cd88
    Directory Object: e1001408  Name: C:
        Target String is '\Device\HarddiskVolume1'
        Drive Letter Index is 3 (C:)
 Volume DevObj: 82254a68
    Vpb: 822549e0  DeviceObject: 82270718
 FileSystem: \FileSystem\Ntfs
    Volume has 0x229236 (free) / 0x2ee1a7 (total) clusters of size 0x1000
    8850.21 of 12001.7 MB free
```

 

 





