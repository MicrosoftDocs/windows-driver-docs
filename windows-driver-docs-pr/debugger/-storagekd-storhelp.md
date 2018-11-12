---
title: storagekd.storhelp
description: The storagekd.storhelp extension displays help text for Storagekd.dll extension commands.
ms.assetid: 17FFB5CC-1FA3-4D13-AA30-6D48D2435CDC
keywords: ["storagekd.storhelp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- storagekd.storhelp
api_type:
- NA
ms.localizationpriority: medium
---

# !storagekd.storhelp


The **!storagekd.storhelp** extension displays help text for Storagekd.dll extension commands.

```dbgcmd
!storagekd.storhelp 
```

## <span id="DLL"></span><span id="dll"></span>DLL


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 8 and later</strong></p></td>
<td align="left"><p>Storagekd.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example of the **!storagekd.storhelp** display:

**0: kd&gt; !storagekd.storhelp**

```dbgcmd
# Storage Debugger Extension
===============================================
## General Commands
----------------
!storhelp    - Displays complete help of the commands provided in this KD extension
!storclass   - Dumps all class devices managed by classpnp
!storadapter - Dumps all adapters managed by Storport
!storunit    - Dumps all disks managed by Storport

## STORPORT specific commands
--------------------------
!storlogirp <args>     - displays internal log entries that reference the specified IRP.
                         See '!storhelp storlogirp' for details.
!storloglist <args>    - displays internal log entries. See '!storhelp storloglist' for details.
!storlogsrb <args>     - displays internal log entries that reference the specified SRB.
                         See '!storhelp storlogsrb' for details.
!storsrb <address>     - display details for the specified SCSI or STORAGE request block
```

 

 





