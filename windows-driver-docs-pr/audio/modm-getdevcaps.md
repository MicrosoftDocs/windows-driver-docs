---
title: MODM_GETDEVCAPS function (Windows Drivers)
description: Learn more about the MODM_GETDEVCAPS function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 10/27/2022
---

# MODM\_GETDEVCAPS function

WINMM sends the `MODM_GETDEVCAPS` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to retrieve information about the capabilities of a specific MIDI output device.

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
  WINMM sets this parameter to **MODM\_GETDEVCAPS** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  For Plug and Play (PnP) drivers, this parameter specifies a pointer to an [**MDEVICECAPSEX**](/windows/win32/api/mmddk/ns-mmddk-mdevicecapsex) structure. The driver fills this structure with the capabilities of the device.

  For drivers that are not Plug and Play, this parameter specifies a far pointer to a [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) data structure. The driver fills this structure with the capabilities of the device.

- *dwParam2*  
  For Plug and Play drivers, this parameter specifies a device node. For drivers that are not Plug and Play, this parameter specifies the size of the **MIDIOUTCAPS** structure in bytes.

## Return value

If the operation is successful, **modMessage** returns MMSYSERR\_NOERROR. Otherwise, it returns MMSYSERR\_NOTENABLED to indicate that the driver failed to load or initialize.

## Remarks

For drivers that are not Plug and Play, the driver must only write *dwParam2* or less bytes to the location pointed to by *dwParam1*.

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

[**MDEVICECAPSEX**](/windows/win32/api/mmddk/ns-mmddk-mdevicecapsex)

[MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps)
