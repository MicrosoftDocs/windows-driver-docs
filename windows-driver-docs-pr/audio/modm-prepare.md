---
title: MODM_PREPARE function (Windows Drivers)
description: Learn more about the MODM_PREPARE function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_PREPARE function

WINMM sends the `MODM_PREPARE` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to request that the driver configure a system-exclusive data block for output. If data blocks are accessed at interrupt time, they must be page-locked to ensure that the memory is not swapped out to disk.

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
  WINMM sets this parameter to **MODM\_PREPARE** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Specifies a far pointer to the [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies the data block.

- *dwParam2*  
  Specifies the size of the **MIDIHDR** structure.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation is successful. Otherwise, it returns one of the error messages in the following table.

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
<td><p>The driver does not support this message.</p></td>
</tr>
</tbody>
</table>

## Remarks

Driver support for this message is optional. If a driver supports this message, it must also support [**MODM\_UNPREPARE**](modm-unprepare.md).

The default response for this message is to return MMSYSERR\_NOTSUPPORTED. In this case, WINMM converts the memory segment to page-locked memory for the driver. If a driver has to perform other operations so that it can prepare a data block for output, it must set the MHDR\_PREPARED bit in the **dwFlags** field of the **MIDIHDR** structure and return MMSYSERR\_NOERROR. In this case, WINMM assumes the driver has prepared the data block and does not page-lock the memory.

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

[**MODM\_UNPREPARE**](modm-unprepare.md)
