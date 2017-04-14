---
title: Supporting Multifunction Devices On Other Buses
author: windows-driver-content
description: Supporting Multifunction Devices On Other Buses
ms.assetid: 5fc78dc5-0553-4557-b188-a34810305061
keywords: ["multifunction devices WDK , other buses", "PnP WDK multifunction devices", "ISA WDK multifunction devices", "USB WDK multifunction devices", "IEEE 1394 WDK multifunction devices"]
---

# Supporting Multifunction Devices On Other Buses


## <a href="" id="ddk-supporting-multifunction-devices-on-other-buses-dg"></a>


For a multifunction device on a PnP ISA, USB, or IEEE 1394 bus, the parent bus driver enumerates the individual functions if the device conforms to the bus standard.

For such a device, the parent bus driver manages the fact that there is more than one device residing at a single bus location. To the rest of the system, the individual functions operate like independent devices.

Vendors of this type of multifunction device must do the following:

-   Ensure that the device conforms to the specification for the bus on which the device will reside.

-   Provide a PnP function driver for each function of the device.

    Since the system-supplied bus driver handles the multifunction semantics, the function drivers can be the same drivers that are used when the functions are packaged as individual devices.

-   Provide an INF file for each function of the device.

    The INF files can be the same files that are used when the functions are packaged as a individual devices. The INF files do not need any special multifunction semantics.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Supporting%20Multifunction%20Devices%20On%20Other%20Buses%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


