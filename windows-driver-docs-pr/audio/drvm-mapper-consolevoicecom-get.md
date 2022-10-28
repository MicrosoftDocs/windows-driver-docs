---
title: DRVM_MAPPER_CONSOLEVOICECOM_GET function (Windows Drivers)
description: Learn more about the DRVM_MAPPER_CONSOLEVOICECOM_GET function.
keywords:
- mmddk/xxxMessage
- xxxMessage
ms.date: 10/27/2022
---

# DRVM\_MAPPER\_CONSOLEVOICECOM\_GET function

The DRVM\_MAPPER\_CONSOLEVOICECOM\_GET message retrieves the device ID of the preferred voice-communications device.

## Syntax

``` c++
DWORD  xxxMessage(
   UINT      uDeviceID,
   UINT      uMsg,
   DWORD_PTR dwParam1,
   DWORD_PTR dwParam2
);
```

## Parameters

- *uDeviceID*  
  Specifies the ID of the target device. See the following **Remarks** section for more information about how to cast this value for use with the appropriate function.

- *uMsg*  
  Caller sets this parameter to DRVM\_MAPPER\_CONSOLEVOICECOM\_GET when it calls **xxxMessage** to process this device message.

- *dwParam1*  
  Pointer to device ID. This parameter points to a DWORD variable into which the function writes the device ID of the current preferred voice-communications device. The function writes the value (-1) if no device is available that qualifies as a preferred voice-communications device.

- *dwParam2*  
  Pointer to status flags. This parameter points to a DWORD variable into which the function writes the device-status flags. Only one flag bit is currently defined: DRVM\_MAPPER\_PREFERRED\_FLAGS\_PREFERREDONLY. For more information, see the following Remarks section.

## Return value

The *xxx*Message function returns MMSYSERR\_NOERROR if the message is handled successfully. Otherwise, it returns an appropriate error code.

## Remarks

This message is valid only for the [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage) and [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage) functions. When a caller calls these two functions with the DRVM\_MAPPER\_CONSOLEVOICECOM\_GET message, the caller must specify the device ID as WAVE\_MAPPER, and then cast this value to the appropriate handle type. For the **waveInMessage**, **waveOutMessage**, [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage), [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage), or [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage) functions, the caller must cast the device ID to a handle of type HWAVEIN, HWAVEOUT, HMIDIIN, HMIDIOUT, or HMIXER, respectively. Note that if the caller supplies a valid handle instead of a device ID for this parameter, the function fails and returns error code MMSYSERR\_NOSUPPORT.

The system intercepts this message and returns the appropriate value without sending the message to the device driver. For general information about system-intercepted **xxxMessage** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

This message provides a way to determine which device is preferred specifically for voice communications, in contrast to the [**DRVM\_MAPPER\_PREFERRED\_GET**](drvm-mapper-preferred-get.md) message, which determines which device is preferred for all other audio functions.

For example, the preferred **waveOut** device for voice communications might be the earpiece in a headset, but the preferred **waveOut** device for all other audio functions might be a set of stereo speakers.

When the DRVM\_MAPPER\_PREFERRED\_FLAGS\_PREFERREDONLY flag bit is set in the DWORD location pointed to by *dwParam2*, the **waveIn** and **waveOut** APIs use only the current preferred voice-communications device and do not search for other available devices if the preferred device is unavailable. The flag that is output by either the **waveInMessage** or **waveOutMessage** call applies to the preferred voice-communications device for both the **waveIn** and **waveOut** APIs, regardless of whether the call is made to **waveInMessage** or **waveOutMessage**. For more information, see [Preferred Voice-Communications Device ID](preferred-voice-communications-device-id.md).

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in Microsoft Windows Me and Windows 2000 and later operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h)</td>
</tr>
</tbody>
</table>

## See also

[**DRVM\_MAPPER\_PREFERRED\_GET**](drvm-mapper-preferred-get.md)

[**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)

[**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

[**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

[Preferred Voice-Communications Device ID](preferred-voice-communications-device-id.md)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)

[**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)
