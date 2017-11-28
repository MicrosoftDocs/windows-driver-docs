---
title: KSPROPERTY\_ITD3D\_PARAMS
description: The KSPROPERTY\_ITD3D\_PARAMS property is used to set the parameters used by a 3D node's ITD algorithm.
ms.assetid: c6f87087-3c91-46a4-b40e-078d0a015c4c
keywords: ["KSPROPERTY_ITD3D_PARAMS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ITD3D_PARAMS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_ITD3D\_PARAMS


The KSPROPERTY\_ITD3D\_PARAMS property is used to set the parameters used by a 3D node's ITD algorithm.

## <span id="ddk_ksproperty_itd3d_params_ks"></span><span id="DDK_KSPROPERTY_ITD3D_PARAMS_KS"></span>


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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSNODEPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537143)</p></td>
<td align="left"><p>[<strong>KSDS3D_ITD_PARAMS_MSG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537114)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSDS3D\_ITD\_PARAMS\_MSG that specifies the parameters for the ITD algorithm.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_ITD3D\_PARAMS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSDS3D\_ITD\_PARAMS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff537114)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_ITD3D_PARAMS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





