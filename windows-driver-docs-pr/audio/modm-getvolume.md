---
title: MODM_GETVOLUME Function (Windows Drivers)
description: Learn more about the MODM_GETVOLUME function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_GETVOLUME function

WINMM sends the `MODM_GETVOLUME` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to request the current volume level setting for a MIDI device.

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
  WINMM sets this parameter to **MODM\_GETVOLUME** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  This parameter specifies a far pointer to a **DWORD** location. The driver fills this location with the current volume level setting. The high-order word contains the right channel setting and the low-order word contains the left channel setting. A value of zero is silence, and a value of 0xFFFF is full volume. If the driver does not support both left and right channel volume changes, it returns the volume level setting in the low-order word.

- *dwParam2*  
  Not used.

## Return value

The **modMessage** message returns MMSYSERR\_NOERROR, if the operation is successful. Otherwise, it returns one of the error messages in the following table.

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
<td><p>The driver does not support changes to volume level settings.</p></td>
</tr>
</tbody>
</table>

## Remarks

Only drivers for internal synthesizer devices can support volume level changes. Drivers for MIDI output ports should return an MMSYSERR\_NOTSUPPORTED error for this message. Support for volume level changes by internal synthesizer devices is optional. However, if a driver supports changes to the volume level with the [**MODM\_SETVOLUME**](modm-setvolume.md) message, it must support queries with the `MODM_GETVOLUME` message.

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

[**MODM\_SETVOLUME**](modm-setvolume.md)
