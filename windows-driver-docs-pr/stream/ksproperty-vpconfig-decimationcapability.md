---
title: KSPROPERTY\_VPCONFIG\_DECIMATIONCAPABILITY
description: The KSPROPERTY\_VPCONFIG\_DECIMATIONCAPABILITY property indicates if the size of the video image can be reduced by the hardware.
ms.assetid: a929b154-165e-4075-9295-d34fecc8e18d
keywords: ["KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_DECIMATIONCAPABILITY


The KSPROPERTY\_VPCONFIG\_DECIMATIONCAPABILITY property indicates if the size of the video image can be reduced by the hardware.

## <span id="ddk_ksproperty_vpconfig_decimationcapability_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_DECIMATIONCAPABILITY_KS"></span>


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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p>Boolean</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a Boolean. Specify **TRUE** if the hardware can reduce the video image dimensions, or specify **FALSE** if the hardware cannot reduce the dimensions.

Remarks
-------

A property value of **TRUE** specifies that the video image can be reduced in size. **FALSE** specifies that the image can still be resized, but would also be clipped to the rectangle instead of scaled.

KSPROPERTY\_VPCONFIG\_DECIMATION\_CAPABILITY property requests return STATUS\_SUCCESS to indicate successful completion. Otherwise, requests return an appropriate error status code.

When this property is used by KSPROPSETID\_VPVBIConfig, all property requests must return STATUS\_NOT\_IMPLEMENTED.

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

 

 






