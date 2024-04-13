---
title: MODM_UNPREPARE Function (Windows Drivers)
description: Learn more about the MODM_UNPREPARE function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_UNPREPARE function

WINMM sends the `MODM_UNPREPARE` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to clean up the memory segment that was configured by [**MODM\_PREPARE**](modm-prepare.md).

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
  WINMM sets this parameter to **MODM\_UNPREPAE** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Specifies a far pointer to a [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies the data block.

- *dwParam2*  
  Specifies the size of the **MIDIHDR** structure.

## Return value

The **modMEssage** function returns MMSYSERR\_NOERROR if the operation is successful. Otherwise, it returns MMSYSERR\_NOTENABLED to indicate that the driver failed to load or initialize.

## Remarks

Driver support for this message is optional. If a driver supports the [**MODM\_PREPARE**](modm-prepare.md) message, it must also support `MODM_UNPREPARE`.

The default response for this message is to return MMSYSERR\_NOTSUPPORTED. In this case, Mmsystem.dll cleans up the preparation that was previously done on the memory block. If a driver performs the PREPARE operation, it must clean up the preparation and reset the MHDR\_PREPARED flag in the **dwFlags** field of the **MIDIHDR** structure.

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

[**MODM\_PREPARE**](modm-prepare.md)

[MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr)
