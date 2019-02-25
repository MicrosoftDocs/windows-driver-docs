---
title: Registry Settings for Serial
description: Registry Settings for Serial
ms.assetid: be64d9d7-6d6b-4430-96a3-ac071d48b121
keywords:
- Serial driver WDK , registry settings
- registry WDK serial devices
- serial devices WDK , registry settings
- serial devices WDK , Serial driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Settings for Serial





This section describes the following registry settings that Serial uses to configure a serial device:

[Registry Settings for the Serial Service](registry-settings-for-the-serial-service.md)

[Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md)

[Registry Settings for a Legacy COM Port](registry-settings-for-a-legacy-com-port.md)

Serial uses the registry settings to configure a serial device in the following way:

-   If a device-specific entry value is present, Serial uses it.

-   If a device-specific entry value is not present, but there is a corresponding Serial service entry value, Serial uses the service entry value.

-   If a device-specific entry value is not present and there is no corresponding Serial service entry value, Serial uses a default service value that is statically defined in *serial.sys*.

 

 




