---
title: storagekd.storhelp
description: The storagekd.storhelp extension displays help text for Storagekd.dll extension commands.
ms.assetid: 17FFB5CC-1FA3-4D13-AA30-6D48D2435CDC
keywords: ["storagekd.storhelp Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- storagekd.storhelp
api_type:
- NA
---

# !storagekd.storhelp


The **!storagekd.storhelp** extension displays help text for Storagekd.dll extension commands.

``` syntax
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

```
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
                         See &#39;!storhelp storlogirp&#39; for details.
!storloglist <args>    - displays internal log entries. See &#39;!storhelp storloglist&#39; for details.
!storlogsrb <args>     - displays internal log entries that reference the specified SRB.
                         See &#39;!storhelp storlogsrb&#39; for details.
!storsrb <address>     - display details for the specified SCSI or STORAGE request block
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!storagekd.storhelp%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




