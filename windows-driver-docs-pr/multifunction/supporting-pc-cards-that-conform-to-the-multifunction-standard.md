---
title: Supporting PC Cards That Conform to the Multifunction Standard
author: windows-driver-content
description: Supporting PC Cards That Conform to the Multifunction Standard
ms.assetid: 1ab295b6-42c9-46fc-97e0-2228e189ff37
keywords:
- PCMCIA buses WDK multifunction devices
- mf.inf
- hardware IDs WDK multifunction devices
- child function hardware IDs WDK multifunction devices
- system-supplied multifunction bus drivers WDK
- mf.sys
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting PC Cards That Conform to the Multifunction Standard


## <a href="" id="ddk-supporting-pc-cards-that-conform-to-the-multifunction-standard-dg"></a>


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

```
    <Manufacturer-name>-<Product-ID-string>-DEV<number>-CRC
```

In this format, &lt;*number*&gt; is a zero-based number for the function.

For example, the PCMCIA bus driver creates child function hardware IDs such as the following:

```
    3COM_Corporation-3C562D/3C563D-DEV0-4893
    3COM_Corporation-3C562D/3C563D-DEV1-4893
```

An INF file for a child function of a multifunction PC Card device must specify the hardware ID that is reported by the PCMCIA bus driver and mf.sys.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Supporting%20PC%20Cards%20That%20Conform%20to%20the%20Multifunction%20Standard%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


