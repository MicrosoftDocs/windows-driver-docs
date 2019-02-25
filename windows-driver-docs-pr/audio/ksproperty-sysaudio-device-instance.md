---
title: KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE
description: The KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE property specifies the current instance of a virtual audio device.
ms.assetid: 67cdc1ec-c696-454f-a3cc-1b50418c4056
keywords: ["KSPROPERTY_SYSAUDIO_DEVICE_INSTANCE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_DEVICE_INSTANCE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE


The KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE property specifies the current instance of a virtual audio device.

## <span id="ddk_ksproperty_sysaudio_device_instance_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_DEVICE_INSTANCE_KS"></span>


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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the device ID of a virtual audio device. If SysAudio enumerates *n* virtual audio devices (see [**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)), then valid device IDs range from 0 to *n*-1.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

A KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE set-property request opens the virtual audio device specified by the device ID contained in the property value. The last device to be opened is referred to as the current device.

Some SysAudio properties allow the current device to be identified by a null device ID of -1 rather than by a valid device ID in the range 0 to *n*-1, where *n* is the number of available virtual audio devices. These properties include [**KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME**](ksproperty-sysaudio-device-interface-name.md) and [**KSPROPERTY\_SYSAUDIO\_DEVICE\_FRIENDLY\_NAME**](ksproperty-sysaudio-device-friendly-name.md).

A get-property request retrieves the device ID of the current (last opened) virtual audio device.

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

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME**](ksproperty-sysaudio-device-interface-name.md)

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_FRIENDLY\_NAME**](ksproperty-sysaudio-device-friendly-name.md)

 

 






