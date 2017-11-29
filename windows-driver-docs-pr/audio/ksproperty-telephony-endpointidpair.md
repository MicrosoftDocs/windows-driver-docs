---
title: KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR
description: The KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR property contains the render and capture endpoints for cellular audio routing.
ms.assetid: 4F163A65-5572-41D0-80B2-493285E2B87B
keywords: ["KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR


The **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property contains the render and capture endpoints for cellular audio routing.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>[<strong>KSTOPOLOGY_ENDPOINTIDPAIR</strong>](https://msdn.microsoft.com/library/windows/hardware/mt169887)</p></td>
</tr>
</tbody>
</table>

 

The property value is of type [**KSTOPOLOGY\_ENDPOINTIDPAIR**](https://msdn.microsoft.com/library/windows/hardware/mt169887), which specifies the render and capture endpoints.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property request returns the render and capture endpoints for cellular audio routing.

Remarks
-------

Cellular routing is controlled by **KSPROPERTY\_TELEPHONY\_ENDPOINTIDPAIR** property on the topology filter. This property takes a pair of [**KSTOPOLOGY\_ENDPOINTID**](https://msdn.microsoft.com/library/windows/hardware/mt169886) structures for the requested endpoint combination. **KSTOPOLOGY\_ENDPOINTID** contains a reference string for the topology filter of an endpoint and a topology filter pin ID to which the endpoint is connected. The driver provides basic support for this property and returns all of the valid pairs of render and capture endpoints that can be used for cellular audio routing. It is the driver’s responsibility to handle moving both render and capture cellular audio to this new endpoint combination, meeting whatever constraints are necessary for the hardware. This property must be settable even when there is no active phone call in the system.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Client</p></td>
<td align="left"><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_TELEPHONY_ENDPOINTIDPAIR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




