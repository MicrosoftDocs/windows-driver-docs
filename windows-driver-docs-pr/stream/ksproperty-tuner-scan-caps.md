---
title: KSPROPERTY\_TUNER\_SCAN\_CAPS
description: The KSPROPERTY\_TUNER\_SCAN\_CAPS property describes the scanning capabilities of the tuning device, including the network types that the device supports.
ms.assetid: 339d5f6b-81ac-419e-9821-a7f1642e1aa8
keywords: ["KSPROPERTY_TUNER_SCAN_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_SCAN_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_SCAN\_CAPS


The KSPROPERTY\_TUNER\_SCAN\_CAPS property describes the scanning capabilities of the tuning device, including the network types that the device supports. This property must be implemented for an AVStream tuning minidriver that runs on Windows Vista and later.

### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565892" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_CAPS_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565892)"><strong>KSPROPERTY_TUNER_SCAN_CAPS_S</strong></a></p></td>
<td><p>KSPROPERTY_TUNER_SCAN_CAPS_S</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_TUNER\_SCAN\_CAPS\_S structure that specifies the supported network types and whether the driver or firmware for the tuning device can support hardware-assisted scanning operations.

Remarks
-------

The driver should return at least one of the following GUIDs for the network types that it supports. These GUIDs are defined in *Bdamedia.h* and should be referenced from *Bdamedia.h*. For more information about these GUIDs, see [Broadcast Network Type GUIDs](broadcast-network-type-guids.md).

-   DIGITAL\_CABLE\_NETWORK\_TYPE

-   ANALOG\_TV\_NETWORK\_TYPE

-   ANALOG\_AUXIN\_NETWORK\_TYPE

-   ANALOG\_FM\_NETWORK\_TYPE

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565892)

 

 






