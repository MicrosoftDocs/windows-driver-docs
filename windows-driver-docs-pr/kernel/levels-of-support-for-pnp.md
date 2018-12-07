---
title: Levels of Support for PnP
description: Levels of Support for PnP
ms.assetid: 33e0b4c6-858c-4822-ba49-38eb87a5923d
keywords: ["PnP WDK kernel , device support", "Plug and Play WDK kernel , device support", "full PnP WDK kernel", "partial PnP WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Levels of Support for PnP





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

 

 




