---
title: Registry Settings for Serial
author: windows-driver-content
description: Registry Settings for Serial
ms.assetid: be64d9d7-6d6b-4430-96a3-ac071d48b121
keywords:
- Serial driver WDK , registry settings
- registry WDK serial devices
- serial devices WDK , registry settings
- serial devices WDK , Serial driver
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registry Settings for Serial


## <a href="" id="ddk-registry-settings-for-serial-kg"></a>


This section describes the following registry settings that Serial uses to configure a serial device:

[Registry Settings for the Serial Service](registry-settings-for-the-serial-service.md)

[Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md)

[Registry Settings for a Legacy COM Port](registry-settings-for-a-legacy-com-port.md)

Serial uses the registry settings to configure a serial device in the following way:

-   If a device-specific entry value is present, Serial uses it.

-   If a device-specific entry value is not present, but there is a corresponding Serial service entry value, Serial uses the service entry value.

-   If a device-specific entry value is not present and there is no corresponding Serial service entry value, Serial uses a default service value that is statically defined in *serial.sys*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Registry%20Settings%20for%20Serial%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


