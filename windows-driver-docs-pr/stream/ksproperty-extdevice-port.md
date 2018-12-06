---
title: KSPROPERTY\_EXTDEVICE\_PORT
description: The KSPROPERTY\_EXTDEVICE\_PORT property retrieves an external device's port type.
ms.assetid: 7513c37f-0c93-4078-ba85-cbc98304880f
keywords: ["KSPROPERTY_EXTDEVICE_PORT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTDEVICE_PORT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_EXTDEVICE\_PORT


The KSPROPERTY\_EXTDEVICE\_PORT property retrieves an external device's port type.

## <span id="ddk_ksproperty_extdevice_port_ks"></span><span id="DDK_KSPROPERTY_EXTDEVICE_PORT_KS"></span>


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
<td><p>Device</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565156" data-raw-source="[&lt;strong&gt;KSPROPERTY_EXTDEVICE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565156)"><strong>KSPROPERTY_EXTDEVICE_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the external device's connection port. For example 1394 or USB.

Remarks
-------

The **DevPort** member of the KSPROPERTY\_EXTDEVICE\_S structure specifies the external device's port type. The **DevPort** member may be set to equal DEV\_PORT\_1394, DEV\_PORT\_USB, etc. These tokens are defined in the *xprtdefs.h* file in the Microsoft DirectX SDK.

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

[**KSPROPERTY\_EXTDEVICE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565156)

 

 






