---
title: External Device Properties
description: External Device Properties
ms.assetid: 633b24c7-a1da-4748-aaa2-864a01a3fd98
keywords:
- external device properties WDK video capture
- PROPSETID_EXT_DEVICE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# External Device Properties


The [PROPSETID\_EXT\_DEVICE](https://msdn.microsoft.com/library/windows/hardware/ff567795) property set contains properties related to the control or operation of external devices, such as camcorders or digital tape decks. The following table describes the properties that are part of the PROPSETID\_EXT\_DEVICE property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_EXT_DEVICE KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565153" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_ID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565153)"><strong>KSPROPERTY_EXTDEVICE_ID</strong></a></p></td>
<td><p>Returns an external device&#39;s generalized system-wide ID.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565157" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_VERSION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565157)"><strong>KSPROPERTY_EXTDEVICE_VERSION</strong></a></p></td>
<td><p>Returns the version of an external device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565155" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_POWER_STATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565155)"><strong>KSPROPERTY_EXTDEVICE_POWER_STATE</strong></a></p></td>
<td><p>Controls the power state of an external device, such as On, Standby, or Off.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565154" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_PORT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565154)"><strong>KSPROPERTY_EXTDEVICE_PORT</strong></a></p></td>
<td><p>Returns the external device&#39;s connection port type, such as 1394 or USB.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565152" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565152)"><strong>KSPROPERTY_EXTDEVICE_CAPABILITIES</strong></a></p></td>
<td><p>Returns the capabilities of the external device, such as whether the device can record, possesses video capabilities, and/or the device uses files.</p></td>
</tr>
</tbody>
</table>

 

 

 




