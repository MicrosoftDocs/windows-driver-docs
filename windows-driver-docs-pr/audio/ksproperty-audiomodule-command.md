---
title: KSPROPERTY\_AUDIOMODULE\_COMMAND
description: The KSPROPERTY\_AUDIOMODULE\_COMMAND property is a command property used to get and set buffers and instructions on the hardware (pin handle) or software cache (filter handle).
ms.assetid: 90C69481-A3DF-4801-8733-C417950880E5
keywords: ["KSPROPERTY_AUDIOMODULE_COMMAND Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOMODULE_COMMAND
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_AUDIOMODULE\_COMMAND


The **KSPROPERTY\_AUDIOMODULE\_COMMAND** property is a command property used to get and set buffers and instructions on the hardware (pin handle) or software cache (filter handle).

The *Set* value is provided as part of the command. When the *Get* is used, it returns the the results of this command.

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
<td align="left"><p>Filter or Pin</p></td>
<td align="left"><p>[<strong>KSAUDIOMODULE_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/mt808139) + [optional custom module arguments]</p></td>
<td align="left"><p>UNDEFINED</p></td>
</tr>
</tbody>
</table>

 

The property value type is a undefined. The implementer can create a module specific custom command structure.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

**KSPROPERTY\_AUDIOMODULE\_COMMAND** returns audio module command specific information.

Remarks
-------

Support for the **KSPROPERTY\_AUDIOMODULE\_COMMAND** property allows Audio Module clients to send custom commands to query and set parameters on Audio Modules. The property can be sent through the filter or pin handle and a [**KSAUDIOMODULE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/mt808139) is passed as the input buffer for the DeviceIoControl call. A client can optionally send additional information immediately adjacent to the **KSAUDIOMODULE\_PROPERTY** in the input buffer to send custom commands.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIOMODULE_COMMAND%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





