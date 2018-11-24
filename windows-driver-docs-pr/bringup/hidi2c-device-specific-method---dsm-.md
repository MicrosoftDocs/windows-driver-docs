---
title: HIDI2C Device-Specific Method (_DSM)
description: The _DSM method is defined in section 9.14.1, \ 0034;_DSM (Device Specific Method) \ 0034;, in the ACPI 5.0 specification.
ms.assetid: D78077F4-9995-4DC6-9DF6-89D0F8E0C545
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HIDI2C Device-Specific Method (\_DSM)


The \_DSM method is defined in section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications). This method provides for individual, device-specific data and control functions that can be called by a device driver without conflicting with other such device-specific methods.

The \_DSM for a particular device or class defines a UUID (GUID) that is guaranteed not to clash with other UUIDs. For each UUID, there is a set of defined functions that the \_DSM method can implement to provide data or perform control functions for the driver.

For the HIDI2C class of devices, Function 1 is defined as follows:

### Arguments

-   **Arg0:** UUID = 3cdff6f7-4267-4555-ad05-b30a3d8938de
-   **Arg1:** Revision ID = 1
-   **Arg2:** Function index = 1
-   **Arg3:** None

### Return

An integer containing the HidDescriptorAddress. This address is the register offset in the I2C device at which the HID descriptor(s) can be read.
**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

 

 

 




