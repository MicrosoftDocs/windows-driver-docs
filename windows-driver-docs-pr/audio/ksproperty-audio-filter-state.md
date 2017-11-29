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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_AUDIO\_FILTER\_STATE


The KSPROPERTY\_AUDIO\_FILTER\_STATE property is used to query a [GFX filter](https://msdn.microsoft.com/library/windows/hardware/ff536403) for a list of the property sets that it supports. The list is retrieved in the form of an array of property-set GUIDs.

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
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
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

With the array of GUIDs from a KSPROPERTY\_AUDIO\_FILTER\_STATE get-property request, the operating system can serially interrogate the properties within each property set. This information enables the operating system to restore the state of a GFX filter object at the time that the filter is instantiated, and also to save the state of a GFX filter object at the time that the filter is destroyed. When saving or restoring the state of the GFX filter, the operating system serializes its requests for the properties in each property set, as described in [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671). The purpose for saving and restoring the GFX filter's state is to preserve any changes the user has made to the filter's settings, and to make the settings persistent across successive instantiations of the filter. For additional information, see [Persistence of GFX Settings](https://msdn.microsoft.com/library/windows/hardware/ff537741).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_FILTER_STATE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





