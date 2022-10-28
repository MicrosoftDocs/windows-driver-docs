---
title: MODM_RESET function (Windows Drivers)
description: Learn more about the MODM_RESET function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 10/27/2022
---

# MODM\_RESET function

WINMM sends the `MODM_RESET` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to stop output from the output queue and to turn off any notes that are playing.

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
  WINMM sets this parameter to **MODM\_RESET** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Not used.

- *dwParam2*  
  Not used.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation is successful. Otherwise, it returns MMSYSERR\_NOTENABLED to indicate that the driver failed to load or initialize.

## Remarks

If the output queue of the MIDI output driver is not empty, it must stop all pending data blocks and mark them as done by setting the MHDR\_DONE bit in the **dwFlags** field of the [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure for each block. The driver must then notify the client by using [DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback) to send a [**MOM\_DONE**](mom-done.md) message for each data block.

If the device is an output port, the driver must send a MIDI note-off event for all 128 notes on all 16 channels. Optionally, the driver can track the notes that are turned on and send note-off events for only those notes. In addition, the driver must send a 'damper pedal off' event (controller 0x40) for each channel. If the device is an internal synthesizer, the driver must turn off any notes that are playing.

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

[MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr)

[DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback)

[**MOM\_DONE**](mom-done.md)
