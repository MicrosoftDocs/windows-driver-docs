---
title: Supporting Multifunction PCI Devices
author: windows-driver-content
description: Supporting Multifunction PCI Devices
MS-HAID:
- 'mf-supp\_1b21d9a2-c4a9-45f9-b81d-386e482c82fb.xml'
- 'multifunc.supporting\_multifunction\_pci\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 57cbbcdb-7201-4bf4-a2a0-e613607e4509
keywords: ["multifunction devices WDK , PCI", "PCI multifunction standard WDK", "functional device objects WDK multifunction devices", "FDOs WDK multifunction devices", "physical device objects WDK multifunction devices", "PDOs WDK multifunction devices"]
---

# Supporting Multifunction PCI Devices


## <a href="" id="ddk-supporting-multifunction-pci-devices-dg"></a>


If a multifunction PCI device conforms completely to the PCI multifunction standard, the PCI bus driver enumerates the individual functions. The PCI bus driver manages the fact that there is more than one function residing at a single device location. To the rest of the system, the individual functions operate like independent devices.

Vendors of a PCI multifunction device on an NT-based platform must do the following:

-   Ensure that the device conforms to the PCI multifunction specification.

-   Provide a PnP function driver for each function of the device.

    Since the system-supplied bus driver handles the multifunction semantics, the function drivers can be the same drivers that would be used if the functions were packaged as individual devices.

-   Provide an INF file for each function of the device.

    The INF files can be the same files that would be used if the functions were packaged as a individual devices. The INF files do not need any special multifunction semantics.

For example, the following figure shows the sample device stacks that might be created for a multifunction PCI device with ISDN and modem functions.

![diagram illustrating device stacks for a multifunction device whose parent enumerates each function](images/mf-indep.png)

As shown in the previous figure, rather than enumerating one multifunction device, the PCI driver enumerates two child devices. The PnP manager treats each child device like a typical device, locating INF files, loading the appropriate drivers, calling their AddDevice routines, and so forth until a device stack is created for each device. The PCI driver arbitrates the resources for the child devices and manages any other multifunction aspects of the device. The vendor of the multifunction card provides function drivers and INFs for the ISDN and modem devices, just as if they were separate devices.

The illustration focuses on the function driver and bus driver for each function and their associated FDO and PDO. Any filter drivers (and filter DOs) are omitted for simplicity.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Supporting%20Multifunction%20PCI%20Devices%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


