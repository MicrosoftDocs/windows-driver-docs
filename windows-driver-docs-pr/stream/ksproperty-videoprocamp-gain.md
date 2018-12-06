---
title: KSPROPERTY\_VIDEOPROCAMP\_GAIN
description: The KSPROPERTY\_VIDEOPROCAMP\_GAIN property sets or gets the camera gain. This property is optional.
ms.assetid: 46ed6ba1-1413-4466-9125-2d0a3fd51def
keywords: ["KSPROPERTY_VIDEOPROCAMP_GAIN Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_GAIN
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOPROCAMP\_GAIN


The KSPROPERTY\_VIDEOPROCAMP\_GAIN property sets or gets the camera gain. This property is optional.

## <span id="ddk_ksproperty_videoprocamp_gain_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_GAIN_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566089" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566089)"><strong>KSPROPERTY_VIDEOPROCAMP_S</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff566080" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEOPROCAMP_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566080)"><strong>KSPROPERTY_VIDEOPROCAMP_NODE_S</strong></a></p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's gain setting.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_S structure specifies the requested or current gain, depending on whether this is a *get* or *Set* request.

The range for gain is vendor-defined; the default resolution is 1.

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

[**KSPROPERTY\_VIDEOPROCAMP\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566089)

[**KSPROPERTY\_VIDEOPROCAMP\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566080)

 

 






