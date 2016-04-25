---
title: Device-Specific Method for Microsoft thermal extensions
description: To support more flexible design of thermal zones and thermal sensors, Windows supports extensions to the ACPI thermal zone model.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A8D90493-EE4A-40EC-BE8D-54B1C9EE94AD
---

# Device-Specific Method for Microsoft thermal extensions


To support more flexible design of thermal zones and thermal sensors, Windows supports extensions to the ACPI thermal zone model. Specifically, Windows supports a thermal minimum throttle limit (MTL) for each thermal zone, and also supports sharing a temperature sensor between thermal zones.

For more information about MTL, see the document titled "Thermal Management in Windows" on the [Microsoft Connect website](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=48106).

To use these features, OEMs can include the following Device-Specific Method (\_DSM) in the namespace of any thermal zone.

## Function 1: Minimum throttle limit


The \_DSM control method parameters for the thermal minimum throttle limit are as follows:

### Arguments

-   **Arg0:** UUID = 14d399cd-7a27-4b18-8fb4-7cb7b9f4e500
-   **Arg1:** Revision ID = 0
-   **Arg2:** Function index = 1
-   **Arg3:** Empty package (not used)

### Return

An integer value with the current minimum throttle limit, expressed as a percentage. Windows will not set the throttle limit below this value.
## Function 2: Temperature sensor device


The \_DSM control method parameters for the temperature sensor device are as follows:

### Arguments

-   **Arg0:** UUID = 14d399cd-7a27-4b18-8fb4-7cb7b9f4e500
-   **Arg1:** Revision ID = 0
-   **Arg2:** Function index = 2
-   **Arg3:** Empty package (not used)

### Return

A reference to the device that will return the temperature of this thermal zone.
## Temperature sensor device dependency requirement


If a temperature sensor device is reported via \_DSM function index 2, the thermal zone is additionally required to include a \_DEP object that identifies the thermal zone's dependence on the temperature sensor device.

**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", of the ACPI 5.0 specification.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Device-Specific%20Method%20for%20Microsoft%20thermal%20extensions%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




