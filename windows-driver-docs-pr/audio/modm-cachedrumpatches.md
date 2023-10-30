---
title: MODM_CACHEDRUMPATCHES function (Windows Drivers)
description: Learn more about the MODM_CACHEDRUMPATCHES function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_CACHEDRUMPATCHES function

WINMM sends the `MODM_CACHEDRUMPATCHES` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to ask the driver to cache or uncache the specified drum keys. This allows the internal synthesizer drivers to load the patches that are needed by the client application.

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
  Specifies the ID of the target device. Device IDs are sequential with an initial value of zero and a final value equal to one less than the number of devices that the driver supports.

- *uMsg*  
  WINMM sets this parameter to **MODM\_CACHEDRUMPATCHES** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to keep track of the client that is associated with the message.

- *dwParam1*  
  Specifies a far pointer to a [KEYARRAY](/windows/win32/multimedia/keyarray) array and indicates the patches that must be cached or uncached.

- *dwParam2*  
  The high-order word specifies the bank of patches to which the array refers. The low-order word specifies whether the patches must be cached or uncached (when you call **modMessage**) according to one of the following flags:

  **MIDI\_CACHE\_ALL**. All patches specified in the array must be cached. If the synthesizer cannot cache all the patches, it should not cache any. Instead, it must clear the **KEYARRAY** and return MMSYSERR\_NOMEM.

  **MIDI\_CACHE\_BESTFIT**. If the driver can cache all the patches specified in the array, it must do so. Otherwise, it must cache as many as it can and then alter the **KEYARRAY** to reflect what it has actually cached. The driver must return MMSYSERR\_NOMEM.

  **MIDI\_CACHE\_QUERY**. The array of patches in **KEYARRAY** must be read to determine the patches that have already been cached.

  **MIDI\_UNCACHE**. The patches that are specified in **KEYARRAY** must be uncached and the array must be cleared.

## Return value

**modMessage** returns **MMSYSERR\_NOERROR** if the `MODM_CACHEDRUMPATCHES` message was successfully processed. Otherwise, it returns one of the following error messages.

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
<td><p>The function specified in the call to <strong>modMessage</strong> is not supported.</p></td>
</tr>
</tbody>
</table>

## Remarks

Patch caching is only supported by internal synthesizer device drivers. Drivers for MIDI output ports must return an MMSYSERR\_NOTSUPPORTED error for this message. Support for patch caching is optional for internal synthesizer devices. When a driver receives a [**MODM\_GETDEVCAPS**](modm-getdevcaps.md) message, it must indicate support for patch caching by setting or clearing the MIDICAPS\_CACHE bit in the **dwSupport** field of the [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) data structure.

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

[**MODM\_GETDEVCAPS**](modm-getdevcaps.md)

[MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps)

[KEYARRAY](/windows/win32/multimedia/keyarray)
