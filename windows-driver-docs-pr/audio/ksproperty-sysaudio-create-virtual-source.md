---
title: KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE
description: The KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE property creates a new virtual source.
ms.assetid: 771c4084-8007-4280-8451-946a26182740
keywords: ["KSPROPERTY_SYSAUDIO_CREATE_VIRTUAL_SOURCE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_CREATE_VIRTUAL_SOURCE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE


The KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE property creates a new virtual source.

## <span id="ddk_ksproperty_sysaudio_create_virtual_source_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_CREATE_VIRTUAL_SOURCE_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538485" data-raw-source="[&lt;strong&gt;SYSAUDIO_CREATE_VIRTUAL_SOURCE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538485)"><strong>SYSAUDIO_CREATE_VIRTUAL_SOURCE</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a structure of type SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE that specifies the pin-category and pin-name GUIDs for the virtual source.

The property value (operation data) is a ULONG variable containing the virtual source index. SysAudio generates this index to identify the new virtual source.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is used to create a mixer-line virtual source such as a volume or mute control.

If SysAudio has already created a virtual source with the same pin-category and pin-name GUIDs, a KSPROPERTY\_SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE get-property request retrieves the index for the existing virtual source. Otherwise, the request generates a new virtual source index and outputs that value.

After SysAudio has assigned an index to a virtual source, a [**KSPROPERTY\_SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](ksproperty-sysaudio-attach-virtual-source.md)set-property request can be used to attach that virtual source to a pin instance on the virtual audio device.

The user controls the volume levels of various audio sources through the SndVol32 application. These sources include the wave-output device, MIDI synthesizer, CD player, and line-in jack. SndVol32 uses the Windows multimedia **waveOut***Xxx*, **midiOut***Xxx*, and **aux***Xxx* functions to control the volume levels for these sources. For more information about Windows multimedia functions, see the Microsoft Windows SDK documentation.

SysAudio intercepts volume changes made to these devices and applies them to its virtual sources. For example, if a software MIDI synthesizer that converts a MIDI file to wave data is connected to one of the virtual audio device's wave-rendering pins, SysAudio applies midiOut*Xxx* volume changes to the pin (instead of **waveOut***Xxx* volume changes). Similarly, if the [Redbook system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#redbook-system-driver), which converts digital audio from a CD player to wave data, is connected to one of the virtual audio device's wave-rendering pins, SysAudio applies AUXCAPS\_CDAUDIO volume changes to the pin. For more information about the AUXCAPS\_CDAUDIO structure, see the Windows SDK documentation.

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


[**SYSAUDIO\_CREATE\_VIRTUAL\_SOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff538485)

[**KSPROPERTY\_SYSAUDIO\_ATTACH\_VIRTUAL\_SOURCE**](ksproperty-sysaudio-attach-virtual-source.md)

 

 






