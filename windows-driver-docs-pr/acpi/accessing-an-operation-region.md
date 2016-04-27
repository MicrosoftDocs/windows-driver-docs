---
title: Accessing an Operation Region
description: Accessing an Operation Region
MS-HAID:
- 'opregdg\_03c5d195-449e-4a6e-ab94-532fa9856edb.xml'
- 'acpi.accessing\_an\_operation\_region'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9a1aa29e-679c-4f7f-a16c-3e1c94be66a7
keywords: ["ACPI devices WDK , operation regions", "operation regions WDK ACPI", "function drivers WDK ACPI , operation regions", "WDM function drivers WDK ACPI , operation regions"]
---

# Accessing an Operation Region


## <a href="" id="ddk-accessing-an-operation-region-kg"></a>


When a function driver registers an operation region handler, the driver must specify the access type ACPI\_OPREGION\_ACCESS\_AS\_COOKED. Cooked access supports transfer of information from an ACPI device to the device's function driver, but not from the function driver to the device.

Only the system-supplied ACPI driver modifies the data in an operation region. The function driver can read the data in an operation region. However, it must not modify the data. When called, an operation region handler transfers bytes in the operation region to and from the ACPI driver's data buffer. The ACPI driver manages accessing the correct bytes to read and write a data field in an operation region.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Accessing%20an%20Operation%20Region%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




