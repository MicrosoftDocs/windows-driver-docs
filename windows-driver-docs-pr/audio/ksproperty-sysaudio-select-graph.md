---
title: KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH
description: The KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property is used to explicitly include an optional node in the graph that SysAudio builds for a pin instance on a virtual audio device.
ms.assetid: 1107e20e-9ba8-4fda-8457-c357426a9cda
keywords: ["KSPROPERTY_SYSAUDIO_SELECT_GRAPH Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_SELECT_GRAPH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH


The KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property is used to explicitly include an optional node in the graph that SysAudio builds for a pin instance on a virtual audio device.

## <span id="ddk_ksproperty_sysaudio_select_graph_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_SELECT_GRAPH_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p>[<strong>SYSAUDIO_SELECT_GRAPH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff538500)</p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a structure of type SYSAUDIO\_SELECT\_GRAPH that specifies the property, pin ID, and node ID. The property is specified by an embedded structure of type [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262). The pin ID is an index identifying a pin factory in the KS filter that wraps the virtual audio device. The node ID is an index identifying an optional node in the specified pin's data path. For more information, see the following Remarks section.

No property value (operation data) is defined for this property. Specify the property value's buffer pointer as **NULL** and its size as zero.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is typically used to force an AEC node into the graph for a pin instance.

When instantiating a rendering pin on the filter for a virtual audio device, SysAudio starts at the pin and by default selects the graph that represents the simplest path through the filter. This graph excludes any optional nodes such as AEC controls.

You can override SysAudio's default behavior by first sending SysAudio a KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH set-property request that specifies the optional node that is to be included in the graph. When SysAudio subsequently creates the pin instance, the pin's graph will include the optional node that was specified in the request.

A KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH set-property request affects only pin instances that are created after the request. The request has no effect on any previously instantiated pins.

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


[**SYSAUDIO\_SELECT\_GRAPH**](https://msdn.microsoft.com/library/windows/hardware/ff538500)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_SYSAUDIO_SELECT_GRAPH%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





