---
title: DRV_QUERYDEVICEINTERFACESIZE Function (Windows Drivers)
description: Learn more about the DRV_QUERYDEVICEINTERFACESIZE function.
keywords:
- mmddk/xxxMessage
- xxxMessage
ms.date: 03/06/2023
ms.topic: reference
---

# DRV\_QUERYDEVICEINTERFACESIZE function

The DRV\_QUERYDEVICEINTERFACESIZE message queries for the size of the buffer required to hold the device-interface name.

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
  Caller sets this parameter to DRV\_QUERYDEVICEINTERFACESIZE when it calls **xxxMessage** to process this device message.

- *dwParam1*  
  Pointer to buffer size. This parameter points to a ULONG variable into which the function writes the required buffer size in bytes. The size includes storage space for the name string's terminating null. The size is zero if the device ID identifies a device that has no device interface.

- *dwParam2*  
  Unused. Set this parameter to zero.

## Return value

The **xxxMessage** function returns MMSYSERR\_NOERROR if the message is handled successfully. Otherwise, it returns an appropriate error code.

## Remarks

This message is valid only for the [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage), [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage), [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage), [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage), and [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage) functions. The system intercepts this message and returns the appropriate value without sending the message to the device driver. For general information about system-intercepted **xxxMessage** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

The buffer size retrieved by this message is expressed as a byte count. It specifies the size of the buffer needed to hold the null-terminated Unicode string that contains the device-interface name. The caller allocates a buffer of the specified size and uses the [**DRV\_QUERYDEVICEINTERFACE**](drv-querydeviceinterface.md) message to retrieve the device-interface name string.

For more information, see [Obtaining a Device Interface Name](obtaining-a-device-interface-name.md).

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

[**DRV\_QUERYDEVICEINTERFACE**](drv-querydeviceinterface.md)

[**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)

[**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

[**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

[Obtaining a Device Interface Name](obtaining-a-device-interface-name.md)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)

[**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)
