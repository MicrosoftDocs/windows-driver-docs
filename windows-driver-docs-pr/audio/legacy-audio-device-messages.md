---
title: Legacy Audio Device Messages
description: Legacy Audio Device Messages
ms.assetid: d8b2807b-e72f-4f72-8a83-5700bc0239dc
ms.date: 11/28/2017
ms.localizationpriority: medium
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

This section describes only messages that are intercepted by the system and handled without ever being passed to the device driver. For more information, see [System-Intercepted Device Messages](https://msdn.microsoft.com/library/windows/hardware/ff538507).

Each message described in this section is valid for use with one or more of the six *xxx*Message functions in the preceding list.

This section describes the following messages:

[**DRV\_QUERYDEVICEINTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536363)

[**DRV\_QUERYDEVICEINTERFACESIZE**](https://msdn.microsoft.com/library/windows/hardware/ff536364)

[**DRV\_QUERYDEVNODE**](https://msdn.microsoft.com/library/windows/hardware/ff536365)

[**DRV\_QUERYMAPPABLE**](https://msdn.microsoft.com/library/windows/hardware/ff536366)

[**DRVM\_MAPPER\_CONSOLEVOICECOM\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536361)

[**DRVM\_MAPPER\_PREFERRED\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff536362)

 

 





