---
title: Enumerating Legacy COM Ports
author: windows-driver-content
description: Enumerating Legacy COM Ports
MS-HAID:
- 'sseovr\_6ae5c2bb-a184-483e-9265-9a35daa2d5b6.xml'
- 'serports.enumerating\_legacy\_com\_ports'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 36a73153-0e3e-4b41-9b3d-08b29b5220fe
keywords: ["Serial driver WDK , COM ports", "COM ports WDK serial devices", "serial devices WDK , COM ports", "enumerating COM ports WDK serial devices", "legacy COM ports WDK serial devices"]
---

# Enumerating Legacy COM Ports


## <a href="" id="ddk-enumerating-legacy-com-ports-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Enumerating%20Legacy%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


