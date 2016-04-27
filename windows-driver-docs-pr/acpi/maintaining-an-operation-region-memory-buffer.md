---
title: Maintaining an Operation Region Memory Buffer
description: Maintaining an Operation Region Memory Buffer
MS-HAID:
- 'opregdg\_44c44b4a-302c-4896-b4ba-4008f027f368.xml'
- 'acpi.maintaining\_an\_operation\_region\_memory\_buffer'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4abe82ec-d8c4-43c1-a72f-5114ba07160e
keywords: ["ACPI devices WDK , operation regions", "operation regions WDK ACPI", "function drivers WDK ACPI , operation regions", "WDM function drivers WDK ACPI , operation regions", "operation region memory buffer WDK ACPI", "memory buffers WDK ACPI"]
---

# Maintaining an Operation Region Memory Buffer


## <a href="" id="ddk-maintaining-an-operation-region-memory-buffer-kg"></a>


The driver maintains an operation region memory buffer. The memory buffer contains the data fields associated with an operation region. The ACPI driver calls an operation region handler to access the data fields in an operation region memory buffer.

The operation region memory buffer must comply with the following:

-   The memory buffer must be allocated from nonpageable system memory.

-   The buffer size must be greater than or equal to the size of the operation region defined for the ACPI device.

-   The buffer must be allocated before the driver registers an operation region handler that accesses it, and maintained as long as the handler is registered.

For detailed information about constraints on operation regions, see the [Advanced Configuration and Power Interface Specification](http://go.microsoft.com/fwlink/p/?linkid=57185).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Maintaining%20an%20Operation%20Region%20Memory%20Buffer%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




