---
title: Supported Drivers
description: Supported Drivers
ms.assetid: 1d41a9a9-415a-4dba-8b52-138c47ad63fd
keywords:
- Static Driver Verifier WDK , requirements
- StaticDV WDK , requirements
- SDV WDK , requirements
- function prototypes WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supported Drivers


For SDV to verify a driver, it must be able to interpret the driver code, specifically, the driver's entry points and the code in functions and routines that support required driver functionality.

The following sections describe the basic requirements for drivers and the specific syntax that SDV expects of the drivers that it verifies. SDV does not verify that drivers comply with these requirements, but if the driver does not comply, SDV may fail to run and, in rare situations, it reports false positive or false negative results because of misinterpretation.

### <span id="basic_driver_characteristics"></span><span id="BASIC_DRIVER_CHARACTERISTICS"></span>Basic Driver Characteristics

SDV is able to verify only drivers with the following characteristics:

-   SDV verifies drivers and libraries that are written in C and C++.

-   SDV performs full verification only on KMDF-compliant and WDM-compliant device drivers (function drivers, filter drivers, and bus drivers), NDIS drivers (filter, miniport, and protocol drivers), and Storport drivers.

-   SDV attempts limited verification of generic properties (such as [NullCheck](nullcheckw.md)) on drivers that do not fit into the above categories.

-   SDV can verify WDM drivers that declare their driver callback functions by using the WDM function role types. For information about how to declare functions, see [Declaring Functions Using Function Role Types for WDM Drivers](declaring-functions-using-function-role-types-for-wdm-drivers.md).

-   SDV can verify drivers that are produced from the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff544296), provided you declare each callback function by using an SDV-KMDF callback function role type. For more information, see [Declaring Functions by Using Function Role Types for KMDF Drivers](static-driver-verifier-kmdf-function-declarations.md).

-   SDV can verify NDIS drivers, provided you annotate each callback function with the function declaration by using an SDV-NDIS callback function type. For more information, see [Declaring Functions by Using Function Role Types for NDIS Drivers](static-driver-verifier-ndis-function-declarations.md).

-   SDV can verify Storport drivers, provided that you annotate each callback function with the function declaration. You do this by using an SDV-Storport callback function type. For more information, see [Declaring Functions by Using Function Role Types for Storport Drivers](declaring-functions-by-using-function-role-types-for-storport-drivers.md).

### <span id="basic_driver_requirements"></span><span id="BASIC_DRIVER_REQUIREMENTS"></span>Basic Driver Requirements

For SDV to verify a WDM driver, the driver must:

- Include Wdm.h or Ntddk.h (Wdm.h is a subset of Ntddk.h).

- Create device objects by using methods that are described in [WDM Device Objects and Device Stacks](https://msdn.microsoft.com/library/windows/hardware/ff565639).

- Have an Unload routine that is written as recommended in [Writing an Unload Routine](https://msdn.microsoft.com/library/windows/hardware/ff566400).

- Declare each dispatch function using a function role type declaration, described in [Using Function Role Type Declarations](using-function-role-type-declarations.md). For information about the WDM role types and the **\_Dispatch\_type\_ (**<em>type</em>**)** annotations, see [Declaring Functions Using Function Role Types for WDM Drivers](declaring-functions-using-function-role-types-for-wdm-drivers.md).

For SDV to verify a KMDF driver, the driver must:

-   Include Wdf.h and Ntddk.h.

-   Create the KMDF objects described in [Using the Framework to Develop a Driver](https://msdn.microsoft.com/library/windows/hardware/ff545545).

-   Annotate each callback function using an SDV-KMDF callback function role type, described in [Using Function Role Type Declarations](using-function-role-type-declarations.md). For a list of the supported role types, see [Static Driver Verifier KMDF Function Declarations](static-driver-verifier-kmdf-function-declarations.md).

For SDV to verify an NDIS driver, the driver must:

-   Include Ndis.h and Ntddk.h.

-   Follow the guidelines in the [Network Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568356) to create NDIS drivers.

-   Annotate each callback function by using an SDV-NDIS callback function role type, as described in [Using Function Role Type Declarations](using-function-role-type-declarations.md). For a list of the supported role types, see [Static Driver Verifier NDIS Function Declarations](static-driver-verifier-ndis-function-declarations.md).

In addition, SDV can verify drivers that support:

-   [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

-   [Power management](https://msdn.microsoft.com/library/windows/hardware/ff547131).

-   [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI).

### <span id="reserved_function_names"></span><span id="RESERVED_FUNCTION_NAMES"></span>Reserved Function Names

The SDV [verification engine](verification-engine.md) does not operate properly when the driver or library code uses the same function name patterns that SDV uses internally.

Specifically, SDV does not correctly interpret code if:

-   The code includes function names that begin with \_\_init and are followed by one or more integers, such as \_\_init123.

-   The code includes function names that begin with sdv\_, such as sdv\_Func, or include the string \_sdv\_, such as Func\_sdv\_ or Func\_sdv\_foo.

-   The library uses a .def file to rename an exported function and the external name is the same as the name of another static function in the library.

If the driver code or library code includes these elements, SDV attempts to verify the driver or process the library, but the result is **Not Supported Feature (NSF)**. For more information about SDV results, see [Interpreting Static Driver Verifier Results](interpreting-static-driver-verifier-results.md).

 

 





