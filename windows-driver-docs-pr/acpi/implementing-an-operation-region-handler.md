---
title: Implementing an Operation Region Handler
author: windows-driver-content
description: Implementing an Operation Region Handler
MS-HAID:
- 'opregdg\_d0eabdd0-b0b2-40be-a313-a098d04be4a8.xml'
- 'acpi.implementing\_an\_operation\_region\_handler'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e435393c-d637-45c1-ab65-0b23f796ec02
keywords: ["ACPI devices WDK , operation regions", "operation regions WDK ACPI", "function drivers WDK ACPI , operation regions", "WDM function drivers WDK ACPI , operation regions"]
---

# Implementing an Operation Region Handler


## <a href="" id="ddk-implementing-an-operation-region-handler-kg"></a>


The driver must provide an operation region handler, which is a [**PACPI\_OP\_REGION\_HANDLER**](https://msdn.microsoft.com/library/windows/hardware/ff536153)-typed callback. The ACPI driver calls the operation handler to access the data fields in the driver's operation region. The combined operation of the function driver and the ACPI BIOS is vendor-defined and device-specific. In general, the function driver and the ACPI BIOS access indexes in an operation region that result in device-specific operations and return whatever information is appropriate.

An operation region handler typically uses the following parameters that the ACPI driver passes to the handler:

-   *AccessType* specifies whether the access is a read or write.

    If the access is a read, data is transferred from the operation region memory buffer to the *Data* buffer. If the access is a write, data is transferred from the *Data* buffer to the operation region memory buffer. See [Accessing an Operation Region](accessing-an-operation-region.md).

-   *Address* specifies a byte offset in the operation region memory buffer.

-   *Size* specifies the number of bytes to transfer.

-   *Data* specifies a buffer supplied by the ACPI driver for the data transfer.

-   *Context* specifies the operation region context that the driver registered for the operation region handler.

    The operation region context is only used by the function driver and is device-specific.

In addition to the previously described parameters, the ACPI driver also passes to an operation region handler pointers to the following: an operation region object, a completion handler, and a completion context. However, the function driver does not use the operation region object in a handler, and the completion handler and context are reserved for internal use.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Implementing%20an%20Operation%20Region%20Handler%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


