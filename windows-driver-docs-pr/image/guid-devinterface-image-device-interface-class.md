---
title: GUID\_DEVINTERFACE\_IMAGE Device Interface Class
description: GUID\_DEVINTERFACE\_IMAGE Device Interface Class
ms.assetid: 2bf0bb35-c047-481e-a0f3-b8a8c06e259b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20GUID_DEVINTERFACE_IMAGE%20Device%20Interface%20Class%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




