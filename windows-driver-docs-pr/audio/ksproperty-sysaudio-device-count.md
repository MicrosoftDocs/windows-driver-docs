---
title: KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT
description: The KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT property retrieves a count specifying the number of virtual audio devices that a DirectSound application program has to choose from.
keywords: ["KSPROPERTY_SYSAUDIO_DEVICE_COUNT Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_SYSAUDIO_DEVICE_COUNT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT


The KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT property retrieves a count specifying the number of virtual audio devices that a DirectSound application program has to choose from.

## <span id="ddk_ksproperty_sysaudio_device_count_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_DEVICE_COUNT_KS"></span>


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
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG variable into which SysAudio writes a count specifying the number of virtual audio devices to choose from. If SysAudio enumerates *n* virtual audio devices, these devices are identified by device IDs 0 through *n*-1.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

SysAudio enumerates a unique virtual audio device for each enabled hardware device in the system that performs wave rendering. In each instance, the virtual audio device is composed of the hardware device, the [KMixer system driver](./kernel-mode-wdm-audio-components.md#kmixer-system-driver), and other audio components. A DirectSound application program selects a particular hardware device by selecting the virtual audio device that incorporates the hardware device.

For example, if three audio cards are plugged into the system bus and each contains a wave-rendering device with a WaveCyclic or WavePci miniport driver, SysAudio enumerates three virtual audio devices with device IDs 0, 1, and 2.

SysAudio maintains its list of virtual audio devices in the system registry under the category KSCATEGORY\_AUDIO\_DEVICE. This category is reserved exclusively for use by SysAudio. DirectSound does not directly access information about the virtual audio devices from the system registry. Instead, it queries SysAudio for the properties of the virtual audio devices.

## Requirements

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


[**KSPROPERTY**](../stream/ksproperty-structure.md)
