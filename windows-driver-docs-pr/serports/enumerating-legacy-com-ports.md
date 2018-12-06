---
title: Enumerating Legacy COM Ports
description: Enumerating Legacy COM Ports
ms.assetid: 36a73153-0e3e-4b41-9b3d-08b29b5220fe
keywords:
- Serial driver WDK , COM ports
- COM ports WDK serial devices
- serial devices WDK , COM ports
- enumerating COM ports WDK serial devices
- legacy COM ports WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Legacy COM Ports





The Serial function driver currently enumerates legacy [COM ports](configuration-of-com-ports.md) that are specified in the registry. Most COM ports that Serial enumerates are legacy devices on multiport boards that do not have a microcontroller. Note that this enumeration function will be removed from Serial and included as part of Setup in a future release.

Serial performs the following steps:

1.  Checks for COM ports identified by subkeys under the driver service registry key **..\\Services\\Serial\\Parameters**\\&lt;*Device subkey&gt;.*

    For each device subkey, Serial obtains the registry information described in [Registry Settings for a Legacy COM Port](registry-settings-for-a-legacy-com-port.md).

2.  Checks if the COM port is a legacy device. If the **PnPDeviceID** entry value is null, the device is a legacy device. Serial only does the remaining steps if the COM port is a legacy device. (If **PnPDeviceID** is nonnull, the port is a Plug and Play device that is enumerated by its bus driver.)

3.  If the COM port is a legacy device, Serial determines if it previously detected it.

    Serial uses a COM port's **LegacyDiscovered** entry value (REG\_DWORD). If **LegacyDiscovered** is nonzero, Serial previously detected the port and skips enumerating it again. The Plug and Play manager adds and starts the legacy port.

    If **LegacyDiscovered** is zero, Serial did not previously detect the port and reports the COM port to the Plug and Play manager. The Plug and Play manager returns a PDO and creates an entry for the COM port in its device tree.

4.  Creates an FDO for each detected legacy COM port and attaches it to the device stack.

5.  Sets COM port information under the Plug and Play registry key for the legacy COM port.

    Serial uses a subset of the information read from the registry for the legacy COM port. For more information, see [Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md).

6.  Starts the legacy COM port.

 

 




