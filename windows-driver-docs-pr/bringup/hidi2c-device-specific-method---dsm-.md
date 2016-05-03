---
title: HIDI2C Device-Specific Method (\_DSM)
author: windows-driver-content
description: The \_DSM method is defined in section 9.14.1, \ 0034;\_DSM (Device Specific Method) \ 0034;, in the ACPI 5.0 specification.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: D78077F4-9995-4DC6-9DF6-89D0F8E0C545
---

# HIDI2C Device-Specific Method (\_DSM)


The \_DSM method is defined in section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](http://www.acpi.info). This method provides for individual, device-specific data and control functions that can be called by a device driver without conflicting with other such device-specific methods.

The \_DSM for a particular device or class defines a UUID (GUID) that is guaranteed not to clash with other UUIDs. For each UUID, there is a set of defined functions that the \_DSM method can implement to provide data or perform control functions for the driver.

For the HIDI2C class of devices, Function 1 is defined as follows:

### Arguments

-   **Arg0:** UUID = 3cdff6f7-4267-4555-ad05-b30a3d8938de
-   **Arg1:** Revision ID = 1
-   **Arg2:** Function index = 1
-   **Arg3:** None

### Return

An integer containing the HidDescriptorAddress. This address is the register offset in the I2C device at which the HID descriptor(s) can be read.
**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](http://www.acpi.info).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20HIDI2C%20Device-Specific%20Method%20%28_DSM%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


