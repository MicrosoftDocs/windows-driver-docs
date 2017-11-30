---
title: KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID
description: The KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID retrieves the audio module notification device identifier GUID.
ms.assetid: CD9C5FCD-FB2A-4B21-A15E-BA520C3311A7
keywords: ["KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID


The **KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID** retrieves the audio module notification device identifier GUID.

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
<td align="left"><p>Filter Handle or Pin Handle</p></td>
<td align="left"><p>KSPROPERTY</p></td>
<td align="left"><p>GUID</p></td>
</tr>
</tbody>
</table>

 

The returned property value is a single GUID.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

**KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID** returns the GUID associated with the audio module notification device identifier.

The same device GUID value is returned if the filter handle or pin handle is provided as the target.

Remarks
-------

Support for the KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID is required to enable the miniport to signal notifications and pass information to Audio Module clients. The lifetime of this ID is tied to the lifetime of the audio device being exposed and active to the Windows Audio stack. The property can be sent through the filter or pin handle and a KSPROPERTY is passed as the input buffer for the DeviceIoControl call.

For an example of using this KSPROPERTY see the SYSVAD audio driver sample.

For more information about audio modules, see [Implementing Audio Module Discovery](https://msdn.microsoft.com/windows/hardware/drivers/audio/implementing-audio-module-communication).

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
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows 10, version 1703</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[KSPROPSETID\_AudioModule](kspropsetid-audiomodule.md)

[**KSAUDIOMODULE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/mt808138)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOMODULE_NOTIFICATION_DEVICE_ID%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





