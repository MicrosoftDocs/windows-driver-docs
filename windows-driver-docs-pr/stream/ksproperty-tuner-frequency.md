---
title: KSPROPERTY\_TUNER\_FREQUENCY
description: The KSPROPERTY\_TUNER\_FREQUENCY property sets or gets the current frequency or channel of the tuner. This property must be implemented.
ms.assetid: ba6caf67-63c1-4a31-b93f-3b06b61244bf
keywords: ["KSPROPERTY_TUNER_FREQUENCY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_FREQUENCY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_FREQUENCY


The KSPROPERTY\_TUNER\_FREQUENCY property sets or gets the current frequency or channel of the tuner. This property must be implemented.

## <span id="ddk_ksproperty_tuner_frequency_ks"></span><span id="DDK_KSPROPERTY_TUNER_FREQUENCY_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_FREQUENCY_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565839)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the current frequency of the tuner. This value is specified in hertz (Hz).

Remarks
-------

The **Frequency** member of the KSPROPERTY\_TUNER\_FREQUENCY\_S structure specifies the current tuner frequency.

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_TUNER\_FREQUENCY\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565839)

 

 






