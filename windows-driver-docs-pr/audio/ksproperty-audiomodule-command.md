---
title: KSPROPERTY\_AUDIOMODULE\_COMMAND
description: The KSPROPERTY\_AUDIOMODULE\_COMMAND property is a command property used to get and set buffers and instructions on the hardware (pin handle) or software cache (filter handle).
keywords: ["KSPROPERTY_AUDIOMODULE_COMMAND Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIOMODULE_COMMAND
api_type:
- NA
ms.date: 03/06/2023
---


# KSPROPERTY\_AUDIOMODULE\_COMMAND


The **KSPROPERTY\_AUDIOMODULE\_COMMAND** property is a command property used to get and set buffers and instructions on the hardware (pin handle) or software cache (filter handle).

The *Set* value is provided as part of the command. When the *Get* is used, it returns the results of this command.

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudiomodule_property" data-raw-source="[&lt;strong&gt;KSAUDIOMODULE_PROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudiomodule_property)"><strong>KSAUDIOMODULE_PROPERTY</strong></a> + [optional custom module arguments]</p></td>
<td align="left"><p>UNDEFINED</p></td>
</tr>
</tbody>
</table>

 

The property value type is undefined. The implementer can create a module specific custom command structure.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

**KSPROPERTY\_AUDIOMODULE\_COMMAND** returns audio module command specific information.

## Remarks

Support for the **KSPROPERTY\_AUDIOMODULE\_COMMAND** property allows Audio Module clients to send custom commands to query and set parameters on Audio Modules. The property can be sent through the filter or pin handle and a [**KSAUDIOMODULE\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudiomodule_property) is passed as the input buffer for the DeviceIoControl call. A client can optionally send additional information immediately adjacent to the **KSAUDIOMODULE\_PROPERTY** in the input buffer to send custom commands.

For more information about audio modules, see [Implementing Audio Module Discovery](./implementing-audio-module-communication.md).

## Requirements

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

