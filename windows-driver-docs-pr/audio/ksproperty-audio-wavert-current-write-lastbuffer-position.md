---
title: KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION
description: The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION property is used for indicating the last valid byte in the audio buffer.
ms.assetid: 01EC2F29-D30A-4017-841F-8443D7C4BCF6
keywords: ["KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_LASTBUFFER_POSITION Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_LASTBUFFER_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION


The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION property is used for indicating the last valid byte in the audio buffer.

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
<td align="left"><p>Node via Pin instance</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value is of type ULONG and represents the last valid byte in the WaveRT audio buffer.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

If a client app uses the KSPROPERTY\_TYPE\_BASICSUPPORT flag when it sends a KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION property request to the audio driver and STATUS\_SUCCESS is returned, it confirms that the driver supports the newly added KSPROPERTY\_AUDIO\_WAVERT\_CURRENT\_WRITE\_LASTBUFFER\_POSITION property.

When a client app performs the very last write operation to the audio buffer to be processed by the audio driver of an offloaded stream, the audio driver calls the [**SetStreamCurrentWritePositionForLastBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn338128) method. The **SetStreamCurrentWritePositionForLastBuffer** method indicates the “write position” of the very last buffer in a stream. Note that this last buffer could be only partially filled.

If you develop an audio driver that was not designed to work with the audio port class driver (Portcls), then you have to implement your own property handler for the this new KS property.

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
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**SetStreamCurrentWritePositionForLastBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn338128)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_WAVERT_CURRENT_WRITE_LASTBUFFER_POSITION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





