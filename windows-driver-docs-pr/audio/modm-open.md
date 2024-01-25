---
title: MODM_OPEN Function (Windows Drivers)
description: Learn more about the MODM_OPEN function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_OPEN function

WINMM sends the `MODM_OPEN` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to allocate a specified device that a client application can use.

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
  Specifies the ID of the target device. Device IDs are sequential and have an initial value of zero and a final value equal that is to one less than the number of devices that the driver supports.

- *uMsg*  
  WINMM sets this parameter to **MODM\_OPEN** when it calls **modMessage** to process this message.

- *dwUser*  
  The MIDI output driver must fill this location with its instance data, but only in response to the `MODM_OPEN`.

- *dwParam1*  
  This parameter specifies a far pointer to a [**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc) structure. This structure contains additional information for the driver such as instance data from the client and a callback function for the client.

- *dwParam2*  
  This parameter specifies option flags that determine how the device is opened. The flags can be any of the values in the following table.

    <table>
    <thead>
    <tr class="header">
    <th>Flag</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>CALLBACK_EVENT</p></td>
    <td><p>If this flag is specified, <strong>dwCallback</strong> in the <strong>MIDIOPENDESC</strong> structure is assumed to be an event handle.</p></td>
    </tr>
    <tr class="even">
    <td><p>CALLBACK_FUNCTION</p></td>
    <td><p>If this flag is specified, <strong>dwCallback</strong> in the <strong>MIDIOPENDESC</strong> structure is assumed to be the address of a callback function.</p></td>
    </tr>
    <tr class="odd">
    <td><p>CALLBACK_THREAD</p></td>
    <td><p>If this flag is specified, <strong>dwCallback</strong> in the <strong>MIDIOPENDESC</strong> structure is assumed to be a handle to a thread.</p></td>
    </tr>
    <tr class="even">
    <td><p>CALLBACK_WINDOW</p></td>
    <td><p>If this flag is specified, <strong>dwCallback</strong> in the <strong>MIDIOPENDESC</strong> structure is assumed to be a window handle.</p></td>
    </tr>
    <tr class="odd">
    <td><p>MIDI_IO_COOKED</p></td>
    <td><p>If this flag is specified, the device is opened in stream mode and the driver receives stream messages. The driver must be able to handle any contingencies that arise. For example, the driver must be able to play short messages and system-exclusive messages asynchronously to the stream.</p></td>
    </tr>
    </tbody>
    </table>

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if the operation is successful. Otherwise it returns one of the error messages in the following table.

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
<td><strong>MMSYSERR_ALLOCATED</strong></td>
<td><p>The MIDI device is already allocated by the maximum number of clients that the driver supports or the device cannot be opened because of system resource limitations other than memory.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_NOMEM</strong></td>
<td><p>The device cannot be opened because of a failure to allocate or lock memory.</p></td>
</tr>
</tbody>
</table>

## Remarks

The driver must be able to determine the number of clients it can allow to use a particular device. After a device is opened for the maximum number of clients that the driver supports, the driver returns MMSYSERR\_ALLOCATED for any additional requests to open the device. If the open operation is successful, the driver uses the [DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback) function to send the client a [**MOM\_OPEN**](mom-open.md) message.

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

[**MIDIOPENDESC**](/windows/win32/api/mmddk/ns-mmddk-midiopendesc)

[DriverCallback](/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback)

[**MOM\_OPEN**](mom-open.md)
