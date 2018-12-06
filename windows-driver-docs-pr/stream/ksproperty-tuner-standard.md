---
title: KSPROPERTY\_TUNER\_STANDARD
description: The KSPROPERTY\_TUNER\_STANDARD property retrieves the current analog video standard. This property must be implemented.
ms.assetid: b20dd01c-bd6b-4908-a3c4-eb2914eb54d0
keywords: ["KSPROPERTY_TUNER_STANDARD Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_STANDARD
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_STANDARD


The KSPROPERTY\_TUNER\_STANDARD property retrieves the current analog video standard. This property must be implemented.

## <span id="ddk_ksproperty_tuner_standard_ks"></span><span id="DDK_KSPROPERTY_TUNER_STANDARD_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565918" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_STANDARD_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565918)"><strong>KSPROPERTY_TUNER_STANDARD_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the tuning standard of the tuner.

Remarks
-------

The **Standard** member of the KSPROPERTY\_TUNER\_STANDARD\_S structure specifies the current analog video standard.

This property is used only when the current mode is KSPROPERTY\_TUNER\_MODE\_TV.

Analog TV signals can be broadcast in accordance with several different analog TV standards such as NTSC, PAL, or SECAM. Clients use the KSPROPERTY\_TUNER\_MODE\_CAPS property to query the supported standards, and use KSPROPERTY\_TUNER\_STANDARD to get or set the current standard for a TV tuner device.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_TUNER\_STANDARD\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565918)

[**KSPROPERTY\_TUNER\_MODE**](ksproperty-tuner-mode.md)

 

 






