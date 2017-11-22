---
title: KSPROPERTY\_TUNER\_INPUT
description: The KSPROPERTY\_TUNER\_INPUT property describes the input of the tuner in the current tuning mode, such as selecting between cable and antenna tuner inputs. This property must be implemented.
MS-HAID:
- 'vidcapprop\_97bfae42-a9df-4f88-b197-4cbe1504bba9.xml'
- 'stream.ksproperty\_tuner\_input'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_TUNER_INPUT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





