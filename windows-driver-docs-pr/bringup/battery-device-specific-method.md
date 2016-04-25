---
title: Battery Device-Specific Method
description: To support the passive thermal management of the battery by the platform, Microsoft defines a \_DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 622803F4-2548-4E8A-A330-179ABDF374AD
---

# Battery Device-Specific Method


To support the passive thermal management of the battery by the platform, Microsoft defines a \_DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone.

For more information, see [Thermal zones](acpi-defined-devices.md#thermal).

## Function 1: Battery thermal limit


The \_DSM control method parameters for the battery charging thermal limit function are as follows:

### Arguments

-   **Arg0:** UUID = 4c2067e3-887d-475c-9720-4af1d3ed602e
-   **Arg1:** Revision = 0
-   **Arg2:** Function index = 1
-   **Arg3:** Thermal limit (integer value from 0 to 100)

### Return

None. Firmware is responsible for taking the current thermal limit into account when engaging charging.
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Battery%20Device-Specific%20Method%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




