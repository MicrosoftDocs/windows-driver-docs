---
title: MODM_DATA function (Windows Drivers)
description: Learn more about the MODM_DATA function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 10/27/2022
---

# MODM\_DATA function

MMSYSTEM sends the `MODM_DATA` message to the [**modMessage**](mod-message.md) function of a MIDI output driver when the client wants to make a single MIDI event available as output.

## Syntax

``` c++
DWORD modMessage(
   UINT      uDeviceID,
   UINT      uMSG,
   DWORD_PTR dwUser,
   DWORD_PTR dwParam1,
   DWORD_PTR dwParam2
);
```

## Parameters

- *uDeviceID*  
  Specifies the ID of the target device. Device IDs are sequential and have an initial value of zero and a final value that is equal to one less than the number of devices that the driver supports.

- *uMSG*  
  WINMM sets this parameter to **MODM\_DATA** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Specifies the MIDI event that will be available at the output. The low-order byte is the first byte of the event.

- *dwParam2*  
  Not used.

## Return value

If the operation is successful, **modMessage** returns MMSYSERR\_NOERROR. Otherwise, it returns one of the error messages in the following table.

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MMSYSERR_NOTENABLED</strong></td>
<td><p>The driver failed to load or initialize.</p></td>
</tr>
<tr class="even">
<td><strong>MIDIERR_NOTREADY</strong></td>
<td><p>The MIDI hardware is busy processing other data.</p></td>
</tr>
</tbody>
</table>

## Remarks

This message is used to make all MIDI events available as output, except system-exclusive events. System-exclusive events are communicated with the [**MODM\_LONGDATA**](modm-longdata.md) message. MIDI events that are communicated with `MODM_DATA` can be one, two, or three bytes long. The driver must parse the event to determine how many bytes to transfer. Unused bytes are not guaranteed to be zero.

The driver developer can develop a driver to not return until the message has been sent to the output device. Alternatively, the driver can return immediately and the MIDI data can be output in the background.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows XP and later Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h, Mmsystem.h, or Windows.h)</td>
</tr>
</tbody>
</table>

## See also

[**modMessage**](mod-message.md)

[**MODM\_LONGDATA**](modm-longdata.md)
