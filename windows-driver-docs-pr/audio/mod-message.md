---
title: modMessage function (Windows Drivers)
description: Learn more about the modMessage function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 10/27/2022
---

# modMessage function

The **modMessage** function is the entry-point function for musical instrument digital interface (MIDI) output drivers and for internal synthesizer drivers. For more information about audio device messages related to MIDI, see [Audio Device Messages for MIDI](https://msdn.microsoft.com/library/ff536194\(v=vs.85\)).

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
  Specifies the ID of the target device. Device IDs are sequential and have an initial value of zero and a final value equal to one less than the number of devices the driver supports.

- *uMsg*  
  Specifies the message that WINMM sends to the driver in response to a call from the client application.

- *dwUser*  
  For the [**MODM\_OPEN**](modm-open.md) message, the driver should fill this location with its instance data. For any other messages, the instance data is returned to the driver. Drivers that support multiple clients can use this instance data to track which client is associated with the message.

- *dwParam1*  
  Specifies a message-dependent parameter.

- *dwParam2*  
  Specifies a message-dependent parameter. If there are flags that provide additional information to the driver that works with **modMessage**, WINMM uses this parameter to pass the flags.

## Return value

The **modMessage** function returns MMSYSERR\_NOERROR if it can successfully process the message it received from MMSYSTEM. Otherwise, it returns one of the following error messages.

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MMSYSERR_ERROR</strong></td>
<td><p>Unspecified error.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_BADDEVICEID</strong></td>
<td><p>The specified device ID is out of range.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_NOTENABLED</strong></td>
<td><p>The driver failed to load or initialize.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_ALLOCATED</strong></td>
<td><p>The specified device is already allocated.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_INVALHANDLE</strong></td>
<td><p>The handle of the specified device is invalid.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_NODRIVER</strong></td>
<td><p>No device driver is present.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_NOMEM</strong></td>
<td><p>Memory allocation error.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_NOTSUPPORTED</strong></td>
<td><p>The function requested by the message is not supported.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_BADERRNUM</strong></td>
<td><p>Error value is out of range. See Remarks section for more details.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_INVALFLAG</strong></td>
<td><p>An invalid flag was passed to <a href="mod-message.md"><strong>modMessage</strong></a>(by using <em>dwParam2</em>).</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_INVALPARAM</strong></td>
<td><p>An invalid parameter was passed to <a href="mod-message.md"><strong>modMessage</strong></a>.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_HANDLEBUSY</strong></td>
<td><p>The specified handle is being used simultaneously by another thread (for example, a callback thread).</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_INVALIDALIAS</strong></td>
<td><p>The specified alias was not found.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_BADDB</strong></td>
<td><p>Bad registry database.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_KEYNOTFOUND</strong></td>
<td><p>The specified registry key was not found.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_READERROR</strong></td>
<td><p>Registry read error.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_WRITEERROR</strong></td>
<td><p>Registry write error.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_DELETEERROR</strong></td>
<td><p>Registry delete error.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_VALNOTFOUND</strong></td>
<td><p>The specified registry value was not found.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_NODRIVERCB</strong></td>
<td><p>The driver that works with <a href="mod-message.md"><strong>modMessage</strong></a> does not call <a href="/windows/win32/api/mmiscapi/nf-mmiscapi-drivercallback">DriverCallback</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>MMSYSERR_MOREDATA</strong></td>
<td><p><a href="mod-message.md"><strong>modMessage</strong></a> has more data to return.</p></td>
</tr>
<tr class="even">
<td><strong>MMSYSERR_LASTERROR</strong></td>
<td><p>Indicates that this is the last error in the range of error values. See the Remarks section for more details.</p></td>
</tr>
</tbody>
</table>

## Remarks

Audio device messages are system-defined constants. So when **modMessage** receives an audio device message, it uses a switch statement to determine the action to perform, based on the value of the message.

The range of error messages that **modMessage** can return depends on the message that it was processing when the error occurred. The numerical values of the MMSYSERR\_ error messages start with zero (for MMSYSERR\_NOERROR) and continue with MMSYSERR\_BASE + *n*, where *n* is an integer from 1 to 21. The value for MMSYSERR\_BASE is a defined constant. For more information about MSYSERR\_BASE and the MMSYSERR\_ error messages, see Mmsystem.h in the Windows SDK and Mmddk.h in the WDK respectively.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available with Windows XP and later Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h, Mmsystem.h, or Windows.h)</td>
</tr>
</tbody>
</table>

## See also

[**MODM\_OPEN**](modm-open.md)
