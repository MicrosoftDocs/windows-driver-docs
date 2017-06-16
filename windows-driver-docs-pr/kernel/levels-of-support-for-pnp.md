---
title: Levels of Support for PnP
author: windows-driver-content
description: Levels of Support for PnP
ms.assetid: 33e0b4c6-858c-4822-ba49-38eb87a5923d
keywords: ["PnP WDK kernel , device support", "Plug and Play WDK kernel , device support", "full PnP WDK kernel", "partial PnP WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Levels of Support for PnP


## <a href="" id="ddk-levels-of-support-for-pnp-kg"></a>


The extent to which a device supports PnP depends on the PnP support in both the device hardware and the device drivers (see the following table).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>PnP driver</th>
<th>Non-PnP driver</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>PnP Device</strong></p></td>
<td><p>Full PnP</p></td>
<td><p>No PnP</p></td>
</tr>
<tr class="even">
<td><p><strong>Non-PnP Device</strong></p></td>
<td><p>Possible partial PnP</p></td>
<td><p>No PnP</p></td>
</tr>
</tbody>
</table>

 

Any device that supports PnP should have PnP support in its drivers.

A non-PnP device can have some PnP capability if it is driven by a PnP driver. For example, an ISA sound card or an EISA network card can be manually installed and then a PnP driver can treat the card like a PnP device.

If a driver does not support PnP, its devices behave as non-PnP devices regardless of any hardware PnP support. A non-PnP driver can constrain the PnP and power management capabilities of the whole system.

*Legacy drivers* (that is, drivers written before the operating system supported PnP) continue to work as they did previously, without any PnP capability. New drivers should include PnP support.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Levels%20of%20Support%20for%20PnP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


