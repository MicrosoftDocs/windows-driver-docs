---
title: Legacy Audio Device Messages
description: Legacy Audio Device Messages
ms.date: 03/06/2023
ms.topic: reference
---


# Legacy Audio Device Messages


## <span id="ddk_legacy_audio_device_messages_ks"></span><span id="DDK_LEGACY_AUDIO_DEVICE_MESSAGES_KS"></span>


The following Windows Multimedia functions provide a way for callers to pass messages to legacy audio devices:

-   **waveInMessage**

-   **waveOutMessage**

-   **midiInMessage**

-   **midiOutMessage**

-   **mixerMessage**

-   **auxOutMessage**

Some of these device messages are handled directly by the device driver, and some are handled by the system on behalf of the device.

This section describes only messages that are intercepted by the system and handled without ever being passed to the device driver. For more information, see [System-Intercepted Device Messages](./system-intercepted-device-messages.md).

Each message described in this section is valid for use with one or more of the six *xxx*Message functions in the preceding list.

This section describes the following messages:

[**DRV\_QUERYDEVICEINTERFACE**](/previous-versions/windows/hardware/drivers/ff536363(v=vs.85))

[**DRV\_QUERYDEVICEINTERFACESIZE**](/previous-versions/windows/hardware/drivers/ff536364(v=vs.85))

[**DRV\_QUERYDEVNODE**](/previous-versions/windows/hardware/drivers/ff536365(v=vs.85))

[**DRV\_QUERYMAPPABLE**](/previous-versions/windows/hardware/drivers/ff536366(v=vs.85))

[**DRVM\_MAPPER\_CONSOLEVOICECOM\_GET**](/previous-versions/windows/hardware/drivers/ff536361(v=vs.85))

[**DRVM\_MAPPER\_PREFERRED\_GET**](/previous-versions/windows/hardware/drivers/ff536362(v=vs.85))

 

