---
title: KSPROPERTY\_TUNER\_STATUS
description: The KSPROPERTY\_TUNER\_STATUS property retrieves information about the tuning process including the current frequency, phase locked loop (PLL) offset, and signal strength. This property must be implemented.
ms.assetid: 8613cda2-f39b-4363-a1c7-ac91162b9fca
keywords: ["KSPROPERTY_TUNER_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_STATUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_TUNER\_STATUS


The KSPROPERTY\_TUNER\_STATUS property retrieves information about the tuning process including the current frequency, phase locked loop (PLL) offset, and signal strength. This property must be implemented.

## <span id="ddk_ksproperty_tuner_status_ks"></span><span id="DDK_KSPROPERTY_TUNER_STATUS_KS"></span>


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
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_STATUS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565925)</p></td>
<td><p>[<strong>KSPROPERTY_TUNER_STATUS_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565925)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_TUNER\_STATUS\_S structure that specifies the current frequency, PLL offset, and signal strength.

Remarks
-------

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

[**KSPROPERTY\_TUNER\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565925)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_TUNER_STATUS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





