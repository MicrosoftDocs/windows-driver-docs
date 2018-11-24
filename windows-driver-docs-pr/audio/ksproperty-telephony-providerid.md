---
title: KSPROPERTY\_TELEPHONY\_PROVIDERID
description: The KSPROPERTY\_TELEPHONY\_PROVIDERID property is used by the audio driver to associate a provider identifier to a wave filter.
ms.assetid: A2BE85E3-068B-41C1-9791-69A929ECEC5C
keywords: ["KSPROPERTY_TELEPHONY_PROVIDERID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_PROVIDERID
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TELEPHONY\_PROVIDERID


The **KSPROPERTY\_TELEPHONY\_PROVIDERID** property is used by the audio driver to associate a provider identifier to a wave filter.

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
<td align="left"><p>UINT</p></td>
</tr>
</tbody>
</table>

 

The property value is of type UINT and specifies the provider ID.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_PROVIDERID** property request returns a UINT value that represents the provider ID that the audio driver associates to the wave filter.

Remarks
-------

The radio stack has a concept of provider ID (executor ID) and call type (packet or circuit-switched) to connect the phone call instance to a specific hardware path. This concept will continue to be used to communicate to the audio driver which path in hardware to use.

This hardware path will be controlled by sending properties on a wave filter for each provider. The audio driver will associate a provider ID to the wave filter. This provider ID will also be set on the associated cellular streaming endpoints. The provider ID for the wave filter must not change at runtime. The audio stack will query the provider ID from the driver by using the **KSPROPERTY\_TELEPHONY\_PROVIDERID** property . After this provider ID is discovered, all the calls for that provider ID will be sent to the particular wave filter.

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

 

 





