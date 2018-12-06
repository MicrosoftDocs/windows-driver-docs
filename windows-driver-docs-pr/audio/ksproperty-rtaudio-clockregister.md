---
title: KSPROPERTY\_RTAUDIO\_CLOCKREGISTER
description: The KSPROPERTY\_RTAUDIO\_CLOCKREGISTER property maps the wall clock register of the audio device into a virtual memory location that the client can access. The following table summarizes the features of this property.
ms.assetid: a35b5830-55e4-4e92-a4f1-df9edcc2f5bb
keywords: ["KSPROPERTY_RTAUDIO_CLOCKREGISTER Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_CLOCKREGISTER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_CLOCKREGISTER


The KSPROPERTY\_RTAUDIO\_CLOCKREGISTER property maps the wall clock register of the audio device into a virtual memory location that the client can access.

The following table summarizes the features of this property.

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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537498" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER_PROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537498)"><strong>KSRTAUDIO_HWREGISTER_PROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537497" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537497)"><strong>KSRTAUDIO_HWREGISTER</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSRTAUDIO\_HWREGISTER\_PROPERTY structure that contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. Before sending the request, the client loads the KSRTAUDIO\_HWREGISTER\_PROPERTY structure with values that indicate the preferred base address for the clock register.

The property value (operation data) is a pointer to a KSRTAUDIO\_HWREGISTER structure into which the property handler writes the register address and the register-update frequency. This register address is the user-mode or kernel-mode virtual address into which the hardware register is mapped. The client can directly read the register from this address.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_CLOCKREGISTER property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an error code that indicates a failure.

Remarks
-------

Some audio devices contain clock registers. A clock register is a wall clock counter that starts running when the hardware powers up and stops when the hardware powers down. Software uses clock registers to synchronize between two or more controller devices by measuring the relative drift between the hardware clocks of the device.

If successful, the property request maps the clock register to a virtual memory address that is accessible from either user-mode or kernel-mode, as specified by the client. Thereafter, the client reads from this address to obtain the current value of the clock register.

The property request fails if the audio hardware does not support a clock register that can be mapped to virtual memory.

The mapping of the clock register is destroyed when the pin closes. The client can map the register only once in the lifetime of a pin instance, and any subsequent call to map the clock register again for that instance fails.

It is typically faster to read a clock register than it is to send a [**KSPROPERTY\_CLOCK\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff565095) request, which requires transitions between user-mode and kernel-mode for user-mode clients.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSRTAUDIO\_HWREGISTER\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537498)

[**KSRTAUDIO\_HWREGISTER**](https://msdn.microsoft.com/library/windows/hardware/ff537497)

 

 






