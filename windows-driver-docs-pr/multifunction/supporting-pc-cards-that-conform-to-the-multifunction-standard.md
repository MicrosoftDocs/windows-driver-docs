---
title: Supporting PC Cards That Conform to the Multifunction Standard
description: Supporting PC Cards That Conform to the Multifunction Standard
ms.assetid: 1ab295b6-42c9-46fc-97e0-2228e189ff37
keywords:
- PCMCIA buses WDK multifunction devices
- mf.inf
- hardware IDs WDK multifunction devices
- child function hardware IDs WDK multifunction devices
- system-supplied multifunction bus drivers WDK
- mf.sys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting PC Cards That Conform to the Multifunction Standard





If a 16-bit, ISA-style PC Card device implements the PC Card multifunction standard completely and correctly, the vendor of such a device on an NT-based platform can rely on the following system-supplied components to handle the software aspects of the multifunction semantics:

-   An INF file for the multifunction device. (system-supplied)

    The PCMCIA bus driver specifies a hardware ID for the device that causes the configuration manager to use the system-supplied multifunction INF file (mf.inf) to configure the device. The mf.inf file specifies the class "MultiFunction" and its associated GUID (as defined in devguid.h).

-   A function driver for the multifunction device. (system-supplied)

    The mf.inf file specifies the system-supplied multifunction bus driver (mf.sys) as the function driver for the device.

    The mf.sys bus driver enumerates the functions of the device. The PCMCIA bus driver reads the configuration registers on the device to determine the resource requirements of each function.

    See [Using the System-Supplied Multifunction Bus Driver](using-the-system-supplied-multifunction-bus-driver.md) for more information about using the system-supplied mf.sys driver.

The vendor of a multifunction PC Card device that conforms to the standard must provide the following support for the individual functions:

-   A PnP function driver for each function of the device. (vendor-supplied)

    Since the multifunction bus driver handles the multifunction semantics, the function drivers can be the same drivers that would be used if the functions were packaged as individual devices.

-   An INF file for each function of the device. (vendor-supplied)

    The INF files can be the same files that would be used if the functions were packaged as individual devices. The INF files do not need any special multifunction semantics.

### Child Function Hardware IDs Created by the PCMCIA Bus Driver

For a true multifunction PC Card device, the PCMCIA bus driver, together with mf.sys, creates hardware IDs for the child functions. Those IDs have the format:

```cpp
    <Manufacturer-name>-<Product-ID-string>-DEV<number>-CRC
```

In this format, &lt;*number*&gt; is a zero-based number for the function.

For example, the PCMCIA bus driver creates child function hardware IDs such as the following:

```cpp
    3COM_Corporation-3C562D/3C563D-DEV0-4893
    3COM_Corporation-3C562D/3C563D-DEV1-4893
```

An INF file for a child function of a multifunction PC Card device must specify the hardware ID that is reported by the PCMCIA bus driver and mf.sys.

 

 




