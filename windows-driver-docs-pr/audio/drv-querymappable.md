---
title: DRV_QUERYMAPPABLE function (Windows Drivers)
description: Learn more about the DRV_QUERYMAPPABLE function.
keywords:
- mmddk/xxxMessage
- xxxMessage
ms.date: 10/27/2022
---

# DRV\_QUERYMAPPABLE function

The DRV\_QUERYMAPPABLE message queries for whether the specified device can be used by a mapper.

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
  Specifies the ID of the target device.

- *uMsg*  
  Caller sets this parameter to DRV\_QUERYMAPPABLE when it calls **xxxMessage** to process this device message.

- *dwParam1*  
  Unused. Set this parameter to zero.

- *dwParam2*  
  Unused. Set this parameter to zero.

## Return value

The **xxxMessage** function returns MMSYSERR\_NOERROR if the device is mappable. Otherwise, it returns an appropriate error code.

## Remarks

This message is valid only for the [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage), [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage), [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage), [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage), [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage) and [**auxOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-auxoutmessage) functions. The system intercepts this message and returns the appropriate value without sending the message to the device driver. For general information about system-intercepted **xxxMessage** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

When an application program opens a mapper instead of a specific audio device, the system inserts a mapper between the application and the available devices. The mapper selects an appropriate device by mapping the application's requirements to one of the available devices. For more information about mappers, see the Microsoft Windows SDK documentation.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in Microsoft Windows Me/98 and Windows 2000 and later operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h)</td>
</tr>
</tbody>
</table>

## See also

[**auxOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-auxoutmessage)

[**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)

[**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

[**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)

[**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)
