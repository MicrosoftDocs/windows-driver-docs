---
title: KSPROPERTY\_TUNER\_INPUT
description: The KSPROPERTY\_TUNER\_INPUT property describes the input of the tuner in the current tuning mode, such as selecting between cable and antenna tuner inputs. This property must be implemented.
ms.assetid: b2c92531-ad1f-4152-a98d-7cae9c2c940c
keywords: ["KSPROPERTY_TUNER_INPUT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_INPUT
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

# KSPROPERTY\_TUNER\_INPUT


The KSPROPERTY\_TUNER\_INPUT property describes the input of the tuner in the current tuning mode, such as selecting between cable and antenna tuner inputs. This property must be implemented.

## <span id="ddk_ksproperty_tuner_input_ks"></span><span id="DDK_KSPROPERTY_TUNER_INPUT_KS"></span>


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
<td><p>[<strong>KSPROPERTY_TUNER_INPUT_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565856)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the numeric index of the physical tuner inputs. This value should be in the range of 0 through (number of inputs-1).

Remarks
-------

The **InputIndex** member of the KSPROPERTY\_TUNER\_INPUT\_S structure specifies the current tuner input index.

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

[**KSPROPERTY\_TUNER\_INPUT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565856)

 

 






