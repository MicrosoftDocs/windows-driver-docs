---
title: KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT
description: The KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT property retrieves a count specifying the number of virtual audio devices that a DirectSound application program has to choose from.
ms.assetid: c70b6b5e-78fc-4f03-99cf-892297e592be
keywords: ["KSPROPERTY_SYSAUDIO_DEVICE_COUNT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_DEVICE_COUNT
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
<td align="left"><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG variable into which SysAudio writes a count specifying the number of virtual audio devices to choose from. If SysAudio enumerates *n* virtual audio devices, these devices are identified by device IDs 0 through *n*-1.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

SysAudio enumerates a unique virtual audio device for each enabled hardware device in the system that performs wave rendering. In each instance, the virtual audio device is composed of the hardware device, the [KMixer system driver](https://msdn.microsoft.com/library/windows/hardware/ff537039#kmixer-system-driver), and other audio components. A DirectSound application program selects a particular hardware device by selecting the virtual audio device that incorporates the hardware device.

For example, if three audio cards are plugged into the system bus and each contains a wave-rendering device with a WaveCyclic or WavePci miniport driver, SysAudio enumerates three virtual audio devices with device IDs 0, 1, and 2.

SysAudio maintains its list of virtual audio devices in the system registry under the category KSCATEGORY\_AUDIO\_DEVICE. This category is reserved exclusively for use by SysAudio. DirectSound does not directly access information about the virtual audio devices from the system registry. Instead, it queries SysAudio for the properties of the virtual audio devices.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_SYSAUDIO_DEVICE_COUNT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





