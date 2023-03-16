---
title: MODM_GETNUMDEVS function (Windows Drivers)
description: Learn more about the MODM_GETNUMDEVS function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_GETNUMDEVS function

WINMM sends the `MODM_GETNUMDEVS` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to request the number of MIDI output devices available.

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
  WINMM sets this parameter to **MODM\_GETNUMDEVS** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to keep track of the client that is associated with the message.

- *dwParam1*  
  Not used.

- *dwParam2*  
  Not used.

## Return value

The **modMessage** function returns the number of MIDI output devices that the driver supports.

## Remarks

Drivers can be structured in several ways. The simplest and most common drivers use one physical device to support one logical device. Drivers can also support multiple logical devices by using a single physical device. For example, a driver can use a single digital signal processor (DSP) to support two different types of internal synthesizers. Such a driver would return a value of "2" in response to the `MODM_GETNUMDEVS` message.

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

[**ModMessage**](mod-message.md)
