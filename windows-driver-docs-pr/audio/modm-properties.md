---
title: MODM_PROPERTIES Function (Windows Drivers)
description: Learn more about the MODM_PROPERTIES function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_PROPERTIES function

WINMM sends the `MODM_PROPERTIES` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to change the properties of the output stream.

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
  Specifies the ID of the target device. Device IDs are sequential and have with an initial value of zero and a final value that is equal to one less than the number of devices that the driver supports.

- *uMsg*  
  WINMM sets this parameter to **MODM\_PROPERTIES** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to track the client that is associated with the message.

- *dwParam1*  
  Contains a far pointer to a structure that contains information about the stream.

- *dwParam2*  
  Contains flags that specify the operation and property. The property flags are set in the lower 30 bits of the value. These property bits are combined with one of the flags in the following table, by using the logical OR operator.

    <table>
    <thead>
    <tr class="header">
    <th>Flag</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>MIDIPROP_SET</p></td>
    <td><p>Tells the driver to set the specified property.</p></td>
    </tr>
    <tr class="even">
    <td><p>MIDIPROP_GET</p></td>
    <td><p>Tells the driver to read (get) the specified property.</p></td>
    </tr>
    </tbody>
    </table>

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
<td><strong>MMSYSERR_INVALIDPARAM</strong></td>
<td><p>The specified property or property value is invalid.</p></td>
</tr>
</tbody>
</table>

## Remarks

For more information about the properties of a MIDI data stream, see [midiStreamProperties](/windows/win32/api/mmeapi/nf-mmeapi-midistreamproperty). Also see [MIDIPROPTEMPO](/windows/win32/api/mmeapi/ns-mmeapi-midiproptimediv).

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

[midiStreamProperties](/windows/win32/api/mmeapi/nf-mmeapi-midistreamproperty)

[MIDIPROPTIMEDIV](/windows/win32/api/mmeapi/ns-mmeapi-midiproptimediv)

[MIDIPROPTEMPO](/windows/win32/api/mmeapi/ns-mmeapi-midiproptempo)
