---
title: GUID\_DEVINTERFACE\_IMAGE Device Interface Class
description: GUID\_DEVINTERFACE\_IMAGE Device Interface Class
ms.assetid: 2bf0bb35-c047-481e-a0f3-b8a8c06e259b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# GUID\_DEVINTERFACE\_IMAGE Device Interface Class


The image [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [still image devices](https://msdn.microsoft.com/library/windows/hardware/ff542729), including digital cameras and scanners.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Manifest constant</p></td>
<td><p>GUID_DEVINTERFACE_IMAGE</p></td>
</tr>
<tr class="even">
<td><p>Class GUID</p></td>
<td><p>{0x6bdd1fc6L, 0x810f, 0x11d0, 0xbe, 0xc7, 0x08, 0x00, 0x2b, 0xe2, 0x09, 0x2f}</p></td>
</tr>
</tbody>
</table>

 

### <span id="headers"></span><span id="HEADERS"></span>Headers

Defined in *Wiaintfc.h*. Include *Wiaintfc.h.*

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The system-supplied kernel-mode drivers for still image devices register an instance of this device interface class for still image devices. You can access an instance of this device interface class by using the I/O interface that still image drivers support. For more information about still image devices and drivers, see [Windows Image Acquisition Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553346).

This interface is applicable to both still image drivers and WIA drivers and is available for Microsoft Windows XP and later versions of Windows.

 

 





