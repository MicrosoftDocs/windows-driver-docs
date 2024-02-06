---
title: MODM_GETPOS Function (Windows Drivers)
description: Learn more about the MODM_GETPOS function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_GETPOS function

WINMM sends the `MODM_GETPOS` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to request the current position of the stream pointer in the data stream.

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
  WINMM sets this parameter to **MODM\_GETPOS** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Specifies a far pointer to an [MMTIME](/previous-versions//dd757347(v=vs.85)) structure.

- *dwParam2*  
  Specifies the size, in bytes, of the **MMTIME** structure.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation is successful. Otherwise, it returns MMSYSERR\_NOTENABLED to indicate that the driver failed to load or initialize.

## Remarks

The driver should return the position in the time format specified in the **wType** member of **MMTIME**. If the time format specified in **wType** is not supported, the driver must change **wType** to the default time format and return the position in that format.

Time is measured relative to the start of the first buffer that was sent while the driver was in the last stopped state. The stopped state is entered whenever a [**MODM\_OPEN**](modm-open.md), [**MODM\_RESET**](modm-reset.md), or [**MODM\_STOP**](modm-stop.md) message is received. Time spent between a [**MODM\_PAUSE**](modm-pause.md) and the matching [**MODM\_RESTART**](modm-restart.md) is not counted, but the clock should not be reset. Likewise, the time during which the driver is starved for data must not be counted; the returned time must be as if the stream played perfectly with no interruptions or pauses.

If the device is paused or starved, the time returned must be the time of the last event played.

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

[MMTIME](/previous-versions//dd757347(v=vs.85))

[**MODM\_OPEN**](modm-open.md)

[**MODM\_RESET**](modm-reset.md)

[**MODM\_STOP**](modm-stop.md)

[**MODM\_PAUSE**](modm-pause.md)

[**MODM\_RESTART**](modm-restart.md)
