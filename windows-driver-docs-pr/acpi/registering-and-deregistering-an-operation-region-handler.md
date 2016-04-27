---
title: Registering and Deregistering an Operation Region Handler
description: Registering and Deregistering an Operation Region Handler
MS-HAID:
- 'opregdg\_32a2162f-28c6-4bce-863a-02883229566b.xml'
- 'acpi.registering\_and\_deregistering\_an\_operation\_region\_handler'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: de40488d-7935-431c-b1f4-87f8aff1125b
keywords: ["ACPI devices WDK , operation regions", "operation regions WDK ACPI", "function drivers WDK ACPI , operation regions", "WDM function drivers WDK ACPI , operation regions", "registering operation region handlers", "deregistering operation region handlers"]
---

# Registering and Deregistering an Operation Region Handler


## <a href="" id="ddk-registering-and-deregistering-an-operation-region-handler-kg"></a>


An ACPI device function driver registers an operation region handler by calling [**RegisterOpRegionHandler**](https://msdn.microsoft.com/library/windows/hardware/ff536158) and supplying the following information:

-   The physical device object (PDO) representing the ACPI device that defines the operation region.

-   The type of access, which can be *raw* or *cooked.*

    For more information, see [Accessing an Operation Region](accessing-an-operation-region.md)

-   The type of region space.

    The vendor should specify a vendor-defined value from 0x80 to 0xFF. (Values less than 0x80 are defined by the ACPI specification and are reserved for internal use.)

-   A pointer to the driver's operation region handler.

    The ACPI driver accesses an operation region by calling the driver's operation region handler.

-   A pointer to the *operation region context*.

    The operation region context is device-specific and is only used by the function driver. When the ACPI driver calls the operation region handler, it passes the operation region context back to the handler. Typically, it is the device extension of the functional device object (FDO).

**RegisterOpRegionHandler** returns an operation region object that the function driver uses to uniquely identify the operation region handler only when the driver deregisters the handler.

Typically, a driver registers an operation region handler in the driver's Plug and Play dispatch routine after it starts an FDO in response to an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. The driver must register the handler after it allocates the handler's operation region context. If the driver creates a vendor-defined device interface, the driver should enable the device interface after it registers the handler.

An ACPI device function driver deregisters an operation region handler by calling [**DeRegisterOpRegionHandler**](https://msdn.microsoft.com/library/windows/hardware/ff536135) and supplying the following information:

-   The PDO that represents the ACPI device that defines the operation region.

-   The operation region object that the ACPI driver returned when the driver registered the operation region handler. This object uniquely identifies the operation region handler.

Typically, a driver deregisters an operation region handler in the driver's Plug and Play dispatch routine before it stops an FDO in response to an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request. The driver must deregister the handler before it frees the handler's operation region context. If the driver creates a vendor-defined device interface, the driver should disable the device interface before it deregisters the handler.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Registering%20and%20Deregistering%20an%20Operation%20Region%20Handler%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




