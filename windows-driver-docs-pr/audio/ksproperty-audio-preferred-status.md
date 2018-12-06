---
title: KSPROPERTY\_AUDIO\_PREFERRED\_STATUS
description: The KSPROPERTY\_AUDIO\_PREFERRED\_STATUS property informs a device that it is the system's preferred audio device.
ms.assetid: a0e89143-ead1-4e0d-a550-398ec1abf9e9
keywords: ["KSPROPERTY_AUDIO_PREFERRED_STATUS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_PREFERRED_STATUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_PREFERRED\_STATUS


The KSPROPERTY\_AUDIO\_PREFERRED\_STATUS property informs a device that it is the system's preferred audio device.

## <span id="ddk_ksproperty_audio_preferred_status_ks"></span><span id="DDK_KSPROPERTY_AUDIO_PREFERRED_STATUS_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537093" data-raw-source="[&lt;strong&gt;KSAUDIO_PREFERRED_STATUS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537093)"><strong>KSAUDIO_PREFERRED_STATUS</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_PREFERRED\_STATUS that specifies the type of preferred device and whether the device is selected or deselected as the preferred device for that device type.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_PREFERRED\_STATUS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The [SysAudio system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#sysaudio-system-driver) uses this property to inform a wave playback, wave record, MIDI, or mixer device when it is selected to be the new preferred device, or when a previously selected preferred device is deselected.

For information about preferred devices, see [**SetupPreferredAudioDevices**](setuppreferredaudiodevices.md).

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

[**KSAUDIO\_PREFERRED\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff537093)

[**SetupPreferredAudioDevices**](setuppreferredaudiodevices.md)

 

 






