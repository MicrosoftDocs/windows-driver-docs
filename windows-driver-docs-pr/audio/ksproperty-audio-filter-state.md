---
title: KSPROPERTY\_AUDIO\_FILTER\_STATE
description: The KSPROPERTY\_AUDIO\_FILTER\_STATE property is used to query a GFX filter for a list of the property sets that it supports. The list is retrieved in the form of an array of property-set GUIDs.
ms.assetid: e0a3bce7-d321-445c-866c-78502b5ea887
keywords: ["KSPROPERTY_AUDIO_FILTER_STATE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_FILTER_STATE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_FILTER\_STATE


The KSPROPERTY\_AUDIO\_FILTER\_STATE property is used to query a GFX filter for a list of the property sets that it supports. The list is retrieved in the form of an array of property-set GUIDs.

## <span id="ddk_ksproperty_audio_filter_state_ks"></span><span id="DDK_KSPROPERTY_AUDIO_FILTER_STATE_KS"></span>


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
<td align="left"><p>Array of GUIDs</p></td>
</tr>
</tbody>
</table>

 

The property data (operation data) is an array of GUIDs. Each GUID in the array specifies a property set that the filter supports.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_FILTER\_STATE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The size of the array of GUIDs that this property returns depends on the number of property sets that the filter supports. Before retrieving the array, a client first queries the size of the property's GUID array by sending the miniport driver's property handler a KSPROPERTY\_AUDIO\_FILTER\_STATE get-property request with a zero-length property-value buffer. The handler responds by returning the required buffer size and the status code STATUS\_BUFFER\_OVERFLOW. For more information, see [Audio Property Handlers](https://msdn.microsoft.com/library/windows/hardware/ff536214).

With the array of GUIDs from a KSPROPERTY\_AUDIO\_FILTER\_STATE get-property request, the operating system can serially interrogate the properties within each property set. This information enables the operating system to restore the state of a GFX filter object at the time that the filter is instantiated, and also to save the state of a GFX filter object at the time that the filter is destroyed. When saving or restoring the state of the GFX filter, the operating system serializes its requests for the properties in each property set, as described in [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671). The purpose for saving and restoring the GFX filter's state is to preserve any changes the user has made to the filter's settings, and to make the settings persistent across successive instantiations of the filter. .

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






