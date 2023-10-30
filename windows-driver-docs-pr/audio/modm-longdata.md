---
title: MODM_LONGDATA function (Windows Drivers)
description: Learn more about the MODM_LONGDATA function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_LONGDATA function

WINMM sends the `MODM_LONGDATA` message to the [**modMessage**](mod-message.md) function of a MIDI output driver when a client application wants the driver to make a data block available as output. This data block typically contains one or more MIDI events, including system-exclusive events. If the data block contains more than one MIDI event, the events are packed into the data block with no padding.

If a client of the MIDI output driver wants to send a single MIDI event, it is more efficient to use the [**MODM\_DATA**](modm-data.md) message.

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
  WINMM sets this parameter to **MODM\_LONGDATA** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  This parameter specifies a far pointer to [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) data structure that identifies the data block.

- *dwParam2*  
  This parameter specifies the size of the **MIDIHDR** structure.

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
<td><strong>MIDIERR_UNPREPARED</strong></td>
<td><p>The specified data block has not been prepared.</p></td>
</tr>
<tr class="odd">
<td><strong>MIDIERR_NOTREADY</strong></td>
<td><p>The MIDI hardware is busy processing other data.</p></td>
</tr>
</tbody>
</table>

## Remarks

The driver must first check the MHDR\_PREPARED bit in the **dwFlags** field of the **MIDIHDR** structure. If the bit is not set, the driver must return MIDIERR\_UNPREPARED. The driver must also clear the MHDR\_DONE bit, set the MHDR\_INQUEUE bit, and place the data block in its output queue. Then the driver must return control to the client by returning MMSYSERR\_NOERROR.

After the data block has been sent as an output, the driver must set the MHDR\_DONE bit and clear the MHDR\_INQUEUE bit before it notifies the client by using [DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback) to send a [**MOM\_DONE**](mom-done.md) message.

The driver developer can design the driver to not return until the message has been sent to the output device. Alternatively, the driver can return immediately, but work in the background to send the MIDI data as output. The driver must maintain MIDI status across multiple [**MODM\_DATA**](modm-data.md) and `MODM_LONGDATA` calls.

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
