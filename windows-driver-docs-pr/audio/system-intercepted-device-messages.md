---
title: System-Intercepted Device Messages
description: System-Intercepted Device Messages
ms.assetid: 5cf1c9a6-e56f-4358-933f-e8aa2ad1b1da
keywords:
- device messages to legacy devices WDK audio
- WDM audio extensions WDK , system-intercepted device messages
- system-intercepted device messages WDK audio
- messages WDK audio
- intercepted device messages WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Intercepted Device Messages


## <span id="system_intercepted_device_messages"></span><span id="SYSTEM_INTERCEPTED_DEVICE_MESSAGES"></span>


The following Windows multimedia functions provide a way for callers to pass messages to legacy audio devices:

-   [**waveInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743846)

-   [**waveOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743865)

-   [**midiInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798457)

-   [**midiOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798475)

-   [**mixerMessage**](https://msdn.microsoft.com/library/windows/desktop/dd757307)

-   [**auxOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd756716)

Some of these device messages are handled directly by the device driver, and some are handled by the system on behalf of the device.

This section discusses only messages that are intercepted by the system and handled without ever being passed to the device driver. System-intercepted messages can obtain the preferred device for voice communications or general audio usage. In addition, system-intercepted messages can provide the following information about a particular device:

-   **The device interface name**

    For information about device interface names, see [Introduction to Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff549460).

-   **The device's Plug and Play devnode number**

    For information about devnodes, see [Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff543194).

-   **Whether the device can be used by a mapper**

    A mapper selects an appropriate device by mapping an application's requirements to one of the available devices in the system. For more information about mappers, see the Microsoft Windows SDK documentation.

For information about other types of device messages, see the Windows SDK documentation.

An *Xxx*Message function has the following syntax:

```cpp
DWORD XxxMessage(
<device ID>,
    UINT  uMsg,
    DWORD_PTR  dwParam1,
    DWORD_PTR  dwParam2
    );
```

The first parameter is a device ID. The [**auxOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd756716) function definition specifies this parameter to be of type UINT, as expected. However, in the case of [**waveInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743846), [**waveOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd743865), [**midiInMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798457), [**midiOutMessage**](https://msdn.microsoft.com/library/windows/desktop/dd798475), or [**mixerMessage**](https://msdn.microsoft.com/library/windows/desktop/dd757307), the caller must cast the device ID to handle type HWAVEIN, HWAVEOUT, HMIDIIN, HMIDIOUT, or HMIXER, respectively. Note that if the caller supplies a valid handle instead of a device ID for this parameter, the function fails and returns error code MMSYSERR\_NOSUPPORT.

The *uMsg* parameter specifies a message value (for example, [**DRV\_QUERYDEVICEINTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536363)). For a list of driver-specific messages, see header file Mmddk.h.

The meaning of parameters *dwParam1* and *dwParam2* depends on the message. For example, a particular message might require that *dwParam1* be a ULONG value; the caller must cast this value to type DWORD\_PTR to satisfy the function definition.

The function returns MMERR\_NOERROR if the call succeeds, or an error status code if it does not.

For more information about the *Xxx*Message functions, see the Windows SDK documentation.

Header file Mmddk.h defines the following system-intercepted device messages:

[**DRV\_QUERYDEVICEINTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536363)

For more information, see [Obtaining a Device Interface Name](obtaining-a-device-interface-name.md).

[**DRV\_QUERYDEVICEINTERFACESIZE**](https://msdn.microsoft.com/library/windows/hardware/ff536364)

For more information, see **Obtaining a Device Interface Name**.

[**DRV\_QUERYDEVNODE**](https://msdn.microsoft.com/library/windows/hardware/ff536365)

Queries for a device's devnode number.

[**DRV\_QUERYMAPPABLE**](https://msdn.microsoft.com/library/windows/hardware/ff536366)

Queries whether a device can be used by a mapper.

[**DRVM\_MAPPER\_CONSOLEVOICECOM\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536361)

For more information, see [Preferred Voice-Communications Device ID](preferred-voice-communications-device-id.md).

[**DRVM\_MAPPER\_PREFERRED\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536362)

For more information, see [Accessing the Preferred Device ID](accessing-the-preferred-device-id.md).

 

 




