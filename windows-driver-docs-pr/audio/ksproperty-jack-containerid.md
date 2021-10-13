---
title: KSPROPERTY\_JACK\_CONTAINERID
description: The KSPROPERTY\_JACK\_CONTAINERID property is implemented as a pin-wise property that is accessed by using the filter handle.
keywords: ["KSPROPERTY_JACK_CONTAINERID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_JACK_CONTAINERID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_JACK\_CONTAINERID


The KSPROPERTY\_JACK\_CONTAINERID property is implemented as a pin-wise property that is accessed by using the filter handle.

This property can be supported on any bridge pin that is associated with one or more physical jacks, or other wired or wireless connection.

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
<td align="left"><p>Pin factory (via filter handle)</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></p></td>
<td align="left"><p><strong>GUID</strong></p></td>
</tr>
</tbody>
</table>

 

The property value (instance data) is a GUID.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

KSPROPERTY\_JACK\_CONTAINERID property request returns a GUID that has the container ID of the device that is associated with the physical jack, or other wired or wireless connection.

## Remarks

The audio driver should support this property if and only if the following are true:

-   The container ID of the associated audio device is different from the container ID of the device node for which the audio driver is loaded.

-   The driver can obtain the correct container ID through other means.

The KSPROPERTY\_JACK\_CONTAINERID property only needs to be populated if the audio endpoint is in a different piece of plastic from the audio adapter. By default the audio endpoint will inherit the container ID of its parent.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**BTHHFP\_DESCRIPTOR**](/windows-hardware/drivers/ddi/bthhfpddi/ns-bthhfpddi-_bthhfp_descriptor)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CONTAINERID**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_containerid)

