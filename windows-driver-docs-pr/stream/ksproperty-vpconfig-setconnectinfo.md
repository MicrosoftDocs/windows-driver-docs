---
title: KSPROPERTY\_VPCONFIG\_SETCONNECTINFO
description: The KSPROPERTY\_VPCONFIG\_SETCONNECTINFO property sets the video port configuration with user-defined connection information. It is a pointer to an array of DDVIDEOPORTCONNECT structures as returned by the KSPROPERTY\_VPCONFIG\_GETCONNECTINFO property.
ms.assetid: 120f6889-cd67-4c05-b4b8-adab3efd7f2c
keywords: ["KSPROPERTY_VPCONFIG_SETCONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SETCONNECTINFO
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_SETCONNECTINFO


The KSPROPERTY\_VPCONFIG\_SETCONNECTINFO property sets the video port configuration with user-defined connection information. It is a pointer to an array of [**DDVIDEOPORTCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff550388) structures as returned by the KSPROPERTY\_VPCONFIG\_GETCONNECTINFO property.

## <span id="ddk_ksproperty_vpconfig_setconnectinfo_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SETCONNECTINFO_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550388" data-raw-source="[&lt;strong&gt;DDVIDEOPORTCONNECT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550388)"><strong>DDVIDEOPORTCONNECT</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a DDVIDEOPORTCONNECT structure that describes the configuration of a video port connection.

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


[**DDVIDEOPORTCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff550388)

[**KSPROPERTY\_VPCONFIG\_GETCONNECTINFO**](ksproperty-vpconfig-getconnectinfo.md)

 

 






