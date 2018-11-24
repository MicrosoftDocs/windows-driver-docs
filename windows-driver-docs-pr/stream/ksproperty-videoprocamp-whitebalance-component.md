---
title: KSPROPERTY\_VIDEOPROCAMP\_WHITEBALANCE\_COMPONENT
description: The KSPROPERTY\_VIDEOPROCAMP\_WHITEBALANCE\_COMPONENT property specifies the white balance setting in blue and red values for video formats.
ms.assetid: ed5faffa-7e31-47ac-bf11-2201d616c6aa
keywords: ["KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOPROCAMP\_WHITEBALANCE\_COMPONENT


The KSPROPERTY\_VIDEOPROCAMP\_WHITEBALANCE\_COMPONENT property specifies the white balance setting in blue and red values for video formats.

## <span id="ddk_ksproperty_videoprocamp_whitebalance_component_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE_COMPONENT_KS"></span>


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
<td><p>Yes</p></td>
<td><p>node</p></td>
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff566082" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_NODE_S2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566082)"><strong>KSPROPERTY_VIDEOPROCAMP_NODE_S2</strong></a></td>
<td><p>Pair of LONG integers</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a pair of LONG integers that specify the red and blue components of a camera's white balance setting. The values indicate the current red and blue component values of the camera.

Remarks
-------

The supported range and default values for white balance components are implementation-dependent.

When making a set request, the client should supply the red component value in the **Value1** member and the blue component value in the **Value2** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2 structure.

To determine the range of white balance values supported by the device, an application can issue a KSPROPERTY\_TYPE\_BASICSUPPORT request. You can specify KSPROPERTY\_TYPE\_BASICSUPPORT in the **Flags** member of the [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) structure.

When making a get request, the client receives the red value in the **Value1** member and the blue component value in the **Value2** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2 structure.

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

[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S2**](https://msdn.microsoft.com/library/windows/hardware/ff566082)

 

 






