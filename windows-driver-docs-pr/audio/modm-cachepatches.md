---
title: MODM_CACHEPATCHES Function (Windows Drivers)
description: Learn more about the MODM_CACHEPATCHES function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MODM\_CACHEPATCHES function

WINMM sends the `MODM_CACHEPATCHES` message to the [**modMessage**](mod-message.md) function of a MIDI output driver to request that the driver cache or uncache the specified patches. This allows internal synthesizer drivers to load the patches that are needed by a client application.

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
  WINMM sets this parameter to **MODM\_CACHEPATCHES** when it calls **modMessage** to process this message.

- *dwUser*  
  Use this parameter to return instance data to the driver. Drivers that support multiple clients can use this instance data to keep track of the client that is associated with the message.

- *dwParam1*  
  Specifies a far pointer to a [PATCHARRAY](/windows/win32/multimedia/patcharray) array and indicates the patches that must be cached or un-cached.

- *dwParam2*  
  The high-order word specifies the bank of patches to which the array refers. The low-order word specifies whether the patches must be cached or uncached according to one of the following flags:

  **MIDI\_CACHE\_ALL**. All patches specified in the array must be cached. If the synthesizer cannot cache all the patches, it must not cache any. If the synthesizer fails to cache any patches, it must clear the **PATCHARRAY** and return MMSYSERR\_NOMEM.

  **MIDI\_CACHE\_BESTFIT**. If the driver can cache all the patches specified in the array, it must do so. Otherwise, it must cache as many as it can, alter the **PATCHARRAY** to reflect what it has actually cached, and return MMSYSERR\_NOMEM.

  **MIDI\_CACHE\_QUERY**. The **PATCHARRAY** must be read to determine the patches that the driver has actually cached.

  **MIDI\_UNCACHE**. The patches specified in the array must be uncached and the **PATCHARRAY** must be cleared.

## Return value

The **modMessage** function returns zero if the operation is successful. Otherwise, it returns one of the error messages in the following table.

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

Patch caching is only supported by internal synthesizer drivers. Drivers for MIDI output ports must return an MMSYSERR\_NOTSUPPORTED error in response to the `MODM_CACHEPATCHES` message. Support for patch caching is optional for internal synthesizer devices. When a driver receives a [**MODM\_GETDEVCAPS**](modm-getdevcaps.md) message, it must either set or clear the MIDICAPS\_CACHE bit in the **dwSupport** field of the [MIDIOUTCAPS](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps) data structure to indicate support for patch caching.

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

[PATCHARRAY](/windows/win32/multimedia/patcharray)
