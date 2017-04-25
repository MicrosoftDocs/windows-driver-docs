---
title: Using the System-Supplied Multifunction Bus Driver
author: windows-driver-content
description: Using the System-Supplied Multifunction Bus Driver
ms.assetid: 75fe659d-5311-4bc6-adfb-fd608e10c718
keywords:
- multifunction devices WDK , system-supplied bus drivers
- system-supplied multifunction bus drivers WDK
- mf.sys
- functional device objects WDK multifunction devices
- FDOs WDK multifunction devices
- physical device objects WDK multifunction devices
- PDOs WDK multifunction devices
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the System-Supplied Multifunction Bus Driver


## <a href="" id="ddk-using-the-system-supplied-multifunction-bus-driver-dg"></a>


If a device's underlying bus supports a multifunction bus standard, such as PC Card, the vendor for a multifunction device on an NT-based platform can use the system-supplied multifunction bus driver (mf.sys) to support the device.

The mf.sys bus driver handles PnP enumeration of the device functions and arbitrates resources, such as I/O ports and IRQs, between the functions. The mf.sys driver handles power management for the child functions by power managing the parent multifunction device.

To use mf.sys, a multifunction device must meet the following requirements:

-   The device's underlying bus must have a multifunction standard.

-   The [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) of the child functions must be identical and must match those of the parent device. When queried for the device capabilities of a child function ([**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664)), the mf.sys driver reports the device capabilities of the parent device.

-   The driver for the bus on which the multifunction device resides, such as pcmcia.sys, must handle any [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) and [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769) requests. The mf.sys driver just passes these IRPs to the parent bus driver.

-   The functions must be independent: they cannot have start-order dependencies; the resource requirements for one function cannot be expressed in terms of the resources of another function (for example, function1 uses I/O port X and function2 uses portX + 200); and each function must be able to operate as a separate device, even if it is serviced by the same driver(s) as another function.

To use mf.sys, a vendor supplies an INF for the multifunction device that specifies mf.sys as the driver for the device. If a device completely and accurately conforms to the multifunction standard for its underlying bus, the vendor of such a device can use the system-supplied mf.inf. If a device does not completely conform to the standard, the vendor must provide a custom INF.

In either case, the vendor also supplies drivers and INF files for the individual functions on the device.

The following skeleton of a custom multifunction INF illustrates the required syntax for specifying mf.sys as the driver for a multifunction device:

```
[Version]
Signature = "$Windows NT$"
; ...
Class = Multifunction   ; the system-defined class for MF devices
ClassGUID  = {4d36e971-e325-11ce-bfc1-08002be10318} ; GUID for MF
; ...
; ...
[ControlFlags]
ExcludeFromSelect = *   ; don&#39;t include PnP devices in a displayed list of 
                        ; devices available for manual installation
[Manufacturer]
; ...
; ...
[ModelsSection]         ; models section
; ...
; ...
[DDInstall.NT]          ; install section
Include = mf.inf        ; specify that this device requires mf.sys
Needs = MFINSTALL.mf
; ...
 
[DDinstall.NT.Services]
Include = mf.inf
Needs = MFINSTALL.mf.Services

[DDInstall.NT.HW]
AddReg=DDInstall.RegHW
 
[DDInstall.RegHW]
; put entries with child function hardware IDs here
; ...
 
; put override sections here...
; ...
 
[Strings]
; ...
```

Consider a combination LAN/modem PC Card device. Without any special multifunction support, such a device might be reported by the PCMCIA bus driver as a single modem device. With the additional support of a multifunction INF and the mf.sys bus driver, both functions of the device are enumerated. The following figure shows the sample device stacks that might be created for such a combo PC Card with the required multifunction support.

![diagram illustrating device stacks for a multifunction device enumerated by mf.sys](images/mf-layers.png)

As shown in the preceding figure, the driver for the bus on which the multifunction device resides enumerates one device. The hardware ID in the multifunction INF file causes the PnP manager to load the mf.sys bus driver as the function driver for the device. The mf.sys bus driver enumerates two child devices, a LAN device and a modem.

The PnP manager treats each child device like a typical device, locating INF files, loading the appropriate drivers, calling their AddDevice routines, and so forth until a device stack is created for each device. The mf.sys bus driver arbitrates the resources for the child devices and manages any other multifunction aspects of the device. The vendor of the multifunction card provides function drivers and INFs for the multiple functions (LAN and modem), just as if they were separate devices.

The illustration focuses on the function drivers and parent bus drivers and their associated FDOs and PDOs. Any filter drivers (and filter DOs) are omitted for simplicity.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bmultifunc\multifunc%5D:%20Using%20the%20System-Supplied%20Multifunction%20Bus%20Driver%20%20RELEASE:%20%288/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


