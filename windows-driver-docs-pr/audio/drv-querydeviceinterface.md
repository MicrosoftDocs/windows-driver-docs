---
title: DRV_QUERYDEVICEINTERFACE function (Windows Drivers)
description: Learn more about the DRV_QUERYDEVICEINTERFACE function.
keywords:
- mmddk/xxxMessage
- xxxMessage
ms.date: 10/27/2022
---

# DRV\_QUERYDEVICEINTERFACE function

The DRV\_QUERYDEVICEINTERFACE message queries for the device-interface name of a **waveIn**, **waveOut**, **midiIn**, **midiOut**, or **mixer** device.

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
  Caller sets this parameter to DRV\_QUERYDEVICEINTERFACE when it calls **xxxMessage** to process this device message.

- *dwParam1*  
  Pointer to a caller-allocated buffer into which the function writes a null-terminated Unicode string containing the device-interface name. If the device has no device interface, the string length is zero.

- *dwParam2*  
  Specifies the buffer size in bytes. This is an input parameter to the function. The caller should specify a size that is greater than or equal to the buffer size retrieved by the [**DRV\_QUERYDEVICEINTERFACESIZE**](drv-querydeviceinterfacesize.md) message.

## Return value

The *xxx*Message function returns MMSYSERR\_NOERROR if the message is handled successfully. Otherwise, it returns an appropriate error code.

## Remarks

The DRV\_QUERYDEVICEINTERFACE message is supported in Windows Me, and Windows 2000 and later. This message is valid only for the [**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage), [**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage), [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage), [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage), and [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage) functions. The system intercepts this message and returns the appropriate value without sending the message to the device driver. For general information about system-intercepted **xxxMessage** functions, see [System-Intercepted Device Messages](system-intercepted-device-messages.md).

The following two message constants are used together for the purpose of obtaining device interface names:

- DRV\_QUERYDEVICEINTERFACESIZE

- DRV\_QUERYDEVICEINTERFACE

The first message obtains the size in bytes of the buffer needed to hold the string containing the device interface name. The second message retrieves the name string in a buffer of the required size.

For more information, see [Obtaining a Device Interface Name](obtaining-a-device-interface-name.md).

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h)</td>
</tr>
</tbody>
</table>

## See also

[**DRV\_QUERYDEVICEINTERFACESIZE**](drv-querydeviceinterfacesize.md)

[**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)

[**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

[**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

[System-Intercepted Device Messages](system-intercepted-device-messages.md)

[**waveInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveinmessage)

[**waveOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutmessage)
