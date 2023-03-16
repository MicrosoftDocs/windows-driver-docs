---
title: DRV_QUERYDEVNODE function (Windows Drivers)
description: Learn more about the DRV_QUERYDEVNODE function.
keywords:
- mmddk/xxxMessage
- xxxMessage
ms.date: 03/06/2023
ms.topic: reference
---

# DRV\_QUERYDEVNODE function

The DRV\_QUERYDEVNODE message queries for the [*devnode*](../debugger/-devnode.md) number assigned to the device by the Plug and Play manager.

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
  Caller sets this parameter to DRV\_QUERYDEVNODE when it calls **xxxMessage** to process this device message.

- *dwParam1*  
  Pointer to a caller-allocated DWORD variable into which the function writes the devnode number. If no devnode is assigned to the device, the function sets this variable to zero.

- *dwParam2*  
  Unused. Set this parameter to zero.

## Return value

The **xxxMessage** function returns MMSYSERR\_NOERROR if the message is handled successfully. Otherwise, it returns an appropriate error code.

## Remarks

In Windows 2000 and later, the message always returns MMSYSERR\_NOTSUPPORTED. This message is valid only for the [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage), [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage), [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage), [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage), and [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage) functions. The system intercepts this message and returns the appropriate value without sending the message to the device driver. For general information about system-intercepted **xxxMessage** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in Microsoft Windows Me/98 and not supported Windows 2000 and later operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h)</td>
</tr>
</tbody>
</table>

## See also

[**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)

[**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

[**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)

[**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)