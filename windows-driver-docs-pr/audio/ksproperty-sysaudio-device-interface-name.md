---
title: KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME
description: The KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME property retrieves a Unicode string containing the Plug and Play device interface name for the specified virtual audio device.
ms.assetid: 0541ebb3-ad9a-42c6-9cd6-ea7b056821df
keywords: ["KSPROPERTY_SYSAUDIO_DEVICE_INTERFACE_NAME Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_DEVICE_INTERFACE_NAME
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME


The KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME property retrieves a Unicode string containing the Plug and Play device interface name for the specified virtual audio device.

## <span id="ddk_ksproperty_sysaudio_device_interface_name_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_DEVICE_INTERFACE_NAME_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a>+ULONG</p></td>
<td align="left"><p>LPWSTR</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSPROPERTY structure followed by a ULONG variable containing a device ID that identifies a virtual audio device. If SysAudio enumerates *n* virtual audio devices (see [**KSPROPERTY\_SYSAUDIO\_DEVICE\_COUNT**](ksproperty-sysaudio-device-count.md)), then valid device IDs range from 0 to *n*-1. Also, a device ID value of -1 can be used to indicate the current device, which is the last virtual audio device opened by a [**KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE**](ksproperty-sysaudio-device-instance.md) or [**KSPROPERTY\_SYSAUDIO\_INSTANCE\_INFO**](ksproperty-sysaudio-instance-info.md)set-property request.

The property value (operation data) is a pointer to a null-terminated string of Unicode characters that contains the device's interface name.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_DEVICE\_INTERFACE\_NAME property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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

[**KSPROPERTY\_SYSAUDIO\_DEVICE\_INSTANCE**](ksproperty-sysaudio-device-instance.md)

[**KSPROPERTY\_SYSAUDIO\_INSTANCE\_INFO**](ksproperty-sysaudio-instance-info.md)

 

 






