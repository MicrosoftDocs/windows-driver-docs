---
title: KSPROPERTY\_ONESHOT\_RECONNECT
description: The KSPROPERTY\_ONESHOT\_RECONNECT property is used to prompt the audio driver to attempt to connect to the Bluetooth audio device.
ms.assetid: 54122a02-87e9-4953-aa78-4b9b31447a26
keywords: ["KSPROPERTY_ONESHOT_RECONNECT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ONESHOT_RECONNECT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_ONESHOT\_RECONNECT


The **KSPROPERTY\_ONESHOT\_RECONNECT** property is used to prompt the audio driver to attempt to connect to the Bluetooth audio device.

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
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>NULL</p></td>
</tr>
</tbody>
</table>

 

No property value is sent with this property request.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The **KSPROPERTY\_ONESHOT\_RECONNECT** property returns STATUS\_SUCCESS if the request is successful.

&gt; \[!Note\]
&gt;   A successful request means that the driver made an attempt to connect to the Bluetooth audio device, but does not necessarily mean that the attempt was successful.

 

Remarks
-------

You can implement the [**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md) pin property in your driver. This implementation allows you to check the connection status of the endpoint after you make a **KSPROPERTY\_ONESHOT\_RECONNECT** property request.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md)

 

 






