---
title: Device-Specific Method for Microsoft thermal extensions
description: To support more flexible design of thermal zones and thermal sensors, Windows supports extensions to the ACPI thermal zone model.
ms.assetid: A8D90493-EE4A-40EC-BE8D-54B1C9EE94AD
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




