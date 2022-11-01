---
title: MODM_STRMDATA function (Windows Drivers)
description: Learn more about the MODM_STRMDATA function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 10/27/2022
---

# MODM\_STRMDATA function

WINMM sends the `MODM_STRMDATA` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to get the MIDI output device to send stream data.

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
  WINMM sets this parameter to **MODM\_STRMDATA** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  This parameter specifies a far pointer to [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that contains data in the stream buffer format.

- *dwParam2*  
  This parameter specifies the size, in bytes, of the **MIDIHDR** structure.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation was successful. Otherwise, it returns MMSYSERR\_NOTENABLED to indicate that the driver failed to load or initialize.

## Remarks

The **dwStreamID** member of the [MIDIEVENT](/windows/win32/api/mmeapi/ns-mmeapi-midievent) structure is documented as reserved in the Windows SDK documentation. This member actually contains the destination of the given event. The driver must process the event only under the following circumstances:

- *dwStreamID* matches one of the stream identifiers given in the array that is specified by the **rgIds** member of the [**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc) structure (specified in the [**MODM\_OPEN**](modm-open.md) message). In this case, the driver must process the event on the port to which the stream identifier was bound by means of a device identifier in the **MODM\_OPEN** message.

- *dwStreamID* contains a -1 (0xFFFFFFFFL). In this case, the driver must process the event for all ports that are open on this stream.

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

[MIDIEVENT](/windows/win32/api/mmeapi/ns-mmeapi-midievent)

[**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc)
