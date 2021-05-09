---
title: KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS
description: The KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS property describes the scanning capabilities of a particular broadcast network type that the tuning device supports. This property can be implemented optionally.
keywords: ["KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS


The KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS property describes the scanning capabilities of a particular broadcast network type that the tuning device supports. This property can be implemented optionally.

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
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_networktype_scan_caps_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_networktype_scan_caps_s)"><strong>KSPROPERTY_TUNER_NETWORKTYPE_SCAN_CAPS_S</strong></a></p></td>
<td><p>KSPROPERTY_TUNER_NETWORKTYPE</p>
<p>_SCAN_CAPS_S</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S structure that specifies the scanning capabilities for a network type.

## Remarks

## Requirements

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


[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_networktype_scan_caps_s)

