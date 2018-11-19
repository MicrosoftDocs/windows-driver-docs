---
title: KSPROPERTY\_VIDEOPROCAMP\_POWERLINE\_FREQUENCY
description: The KSPROPERTY\_VIDEOPROCAMP\_POWERLINE\_FREQUENCY property specifies the local power line frequency. The frequency might be necessary if the device supports anti-flicker processing for fluorescent lighting environments.
ms.assetid: 560bb16d-2a95-408f-b32c-fa2db1c94902
keywords: ["KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VIDEOPROCAMP\_POWERLINE\_FREQUENCY


The KSPROPERTY\_VIDEOPROCAMP\_POWERLINE\_FREQUENCY property specifies the local power line frequency. The frequency might be necessary if the device supports anti-flicker processing for fluorescent lighting environments.

## <span id="ddk_ksproperty_videoprocamp_powerline_frequency_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_POWERLINE_FREQUENCY_KS"></span>


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

 

The property value (operation data) is a LONG that specifies the local power line frequency. The value indicates the current power-line setting of the camera.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>The power-line frequency control is disabled.</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>The power-line frequency is 50 Hz.</p></td>
</tr>
<tr class="odd">
<td><p>2</p></td>
<td><p>The power-line frequency is 60 Hz.</p></td>
</tr>
<tr class="even">
<td><p>3</p></td>
<td><p>The power-line frequency is determined automatically by the system.</p>
<div class="alert">
<strong>Note</strong>  The auto property value (3) is not available on all cameras (UVC 1.1 specifically).
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

Remarks
-------

When making a set request, the client should supply one of the values in the preceding table in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

When making a get request, the client receives one of the values in the preceding table in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

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

[**PowerlineFrequency enumeration**](https://msdn.microsoft.com/library/windows/apps/br226651)

 

 






