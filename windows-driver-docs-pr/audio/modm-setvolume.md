---
title: MODM_SETVOLUME Function (Windows Drivers)
description: Learn more about the MODM_SETVOLUME function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_SETVOLUME function

WINMM sends the `MODM_SETVOLUME` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to set the volume for a MIDI device.

## Syntax

``` c++
DWORD modMessage(
   UINT      uDeviceID,
   UINT      uMsg,
   DWORD_PTR dwUser,
   DWORD_PTR dwParam1,
   DWORD_PTR dwParam2
);
```

## Parameters

- *uDeviceID*  
  Specifies the ID of the target device. Device IDs are sequential and have an initial value of zero and a final value that is equal to one less than the number of devices that the driver supports.

- *uMsg*  
  WINMM sets this parameter to **MODM\_SETVOLUME** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  This parameter specifies the new volume level. The high-order word contains the right channel setting and the low-order word contains the left channel setting. A value of zero is silence, and a value of 0xFFFF is full volume. If the driver does not support both left and right channel volume changes, it uses the volume specified in the low-order word. The driver will typically not support the full 16 bits of volume control and must truncate the lower bits if necessary. However, the original volume level set with MODM\_SETVOLUME must be returned with [**MODM\_GETVOLUME**](modm-getvolume.md).

- *dwParam2*  
  Not used.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation was successful. Otherwise, it returns one of the error messages in the following table.

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
<td><strong>MMSYSERR_NOTSUPPORTED</strong></td>
<td><p>The driver does not support changes to volume level.</p></td>
</tr>
</tbody>
</table>

## Remarks

This volume level is the final output volume; therefore, only drivers for internal synthesizer devices can support volume level changes. Drivers for MIDI output ports must return a MMSYSERR\_NOTSUPPORTED error for this message. Support for volume level changes is optional for internal synthesizer devices. When a driver receives a [**MODM\_GETDEVCAPS**](modm-getdevcaps.md) message, it must indicate support for volume level changes by setting or clearing the MIDICAPS\_VOLUME and MIDICAPS\_LRVOLUME bits in the **dwSupport** field of the [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) data structure. If a driver supports the **MODM\_SETVOLUME** message, it must also support **MODM\_GETVOLUME**.

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

[**MODM\_GETDEVCAPS**](modm-getdevcaps.md)

[MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps)
