---
title: Legacy Audio Device Messages
description: Legacy Audio Device Messages
ms.assetid: d8b2807b-e72f-4f72-8a83-5700bc0239dc
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Legacy%20Audio%20Device%20Messages%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




