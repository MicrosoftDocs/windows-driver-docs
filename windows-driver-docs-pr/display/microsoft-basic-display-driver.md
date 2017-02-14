---
title: Microsoft Basic Display Driver
description: In Windows 8, The Microsoft Basic Display Driver (MSBDD) is the in-box display driver that replaces the XDDM VGA Save and VGA PnP drivers.
ms.assetid: CE89E02E-6527-4285-998B-618EE235CB8F
---

# Microsoft Basic Display Driver


In Windows 8, The Microsoft Basic Display Driver (MSBDD) is the in-box display driver that replaces the XDDM VGA Save and VGA PnP drivers.

The key benefits of using MSBDD are as follows:

-   MSBDD helps to enable a consistent end user and developer experience because it is compatible with DirectX APIs and technologies such as the Desktop Composition.
-   Server scenarios can benefit from the higher functionality (specifically, features like reboot-less updates, dynamic start and stop, and so on) that are provided by the WDDM driver model.
-   MSBDD supports Unified Extensible Firmware Interface (UEFI) Graphics Output Protocol (GOP).
-   MSBDD works on both XDDM and WDDM hardware.

MSBDD is the default in-box display driver that is loaded during setup, in safe mode, in the absence of an IHV graphics driver, or when the inbox installed graphics IHV driver is not working or is disabled. The primary purpose of this driver is to enable Windows to write to the display controllerâ€™s linear frame buffer.

MSBDD can use the video BIOS to manage modes and resolutions on a single monitor. On UEFI platforms, MSBDD inherits the linear frame buffer that is set during boot; in this case, no mode or resolution changes are possible. As shown in *Figure 1 Scenarios supported by Microsoft Basic Display Driver*, MSBDD is used in the following scenarios:

-   Server: Server configurations that lack WDDM-capable graphics hardware can use MSBDD.
-   Windows setup: In the early phases of Windows setup, just before the final boot, only the MSBDD is loaded.

    For example, a user has an older platform that is currently in working condition although it has no in-box graphics driver support for Windows 8. The user upgrades to Windows 8 and uses MSBDD for the setup, installation, and to retrieve an IHV driver if one is available.

-   â€¢ Driver installation, in the following cases:
    -   When a user is installing a new WDDM IHV driver, MSBDD is used during the transition (from the point when the old WDDM IHV driver is uninstalled to the point before the new IHV driver is installed).
    -   When a user encounters problems installing the latest WDDM IHV driver, the user or system can disable the current graphics driver and fallback to using MSBDD.
-   Driver upgrade: By using MSBDD, there is no need to go through a system reboot when upgrading to the IHV-recommended driver.
-   Safe mode: In this mode, only trusted drivers get loaded; this includes MSBDD.

![scenarios supported by microsoft basic display driver](images/scenariossupportedmicrosoftbasicdisplaydriver.jpg)

**Figure 1 Scenarios Supported by Microsoft Basic Display Driver**

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Microsoft%20Basic%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




