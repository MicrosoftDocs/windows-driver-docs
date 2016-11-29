---
title: Declaring Functions by Using Function Role Types for KMDF Drivers
description: Declaring Functions by Using Function Role Types for KMDF Drivers
ms.assetid: 73a408ba-0219-4fde-8dad-ca330e4e67c3
---

# Declaring Functions by Using Function Role Types for KMDF Drivers


To enable SDV to analyze a KMDF driver, you must declare your functions using the function role type declarations for KMDF. The function role types are defined in Wdf.h and in other KMDF header files that are included in Wdf.h. For the list of function role types and their corresponding event callback functions, see [Static Driver Verifier KMDF Function Declarations](static-driver-verifier-kmdf-function-declarations.md).

Each event callback function in a KMDF driver must be declared by specifying the corresponding role type.

For example, the following code example shows the function role type declaration for the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. In this example, the callback function is called *myDriver\_EvtDriverDeviceAdd*. The function role type is EVT\_WDF\_DRIVER\_DEVICE\_ADD.

```
EVT_WDF_DRIVER_DEVICE_ADD myDriver_EvtDriverDeviceAdd;
```

If a callback function has a function prototype declaration, you must replace the function prototype with the function role type declaration.

The following listing is from the header file Fail\_Driver6.h. The related functions are declared in FailDriver6.c.

```
/*++

Copyright (C) Microsoft.  All rights reserved.
Module Name:
    fail_driver6.h
Environment:
    Kernel mode
--*/

#include <NTDDK.h>  
#include <wdf.h>

#include "fail_library6.h"

DRIVER_INITIALIZE DriverEntry;
EVT_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd;
EVT_WDF_IO_QUEUE_IO_READ EvtIoRead;
EVT_WDF_IO_QUEUE_IO_WRITE EvtIoWrite;
EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL EvtIoDeviceControl;
EVT_WDF_DEVICE_CONTEXT_CLEANUP DeviceContextCleanUp;
EVT_WDF_DEVICE_CONTEXT_DESTROY DeviceContextDestroy;
EVT_WDF_IO_QUEUE_CONTEXT_CLEANUP_CALLBACK QueueCleanup;
EVT_WDF_IO_QUEUE_CONTEXT_DESTROY_CALLBACK QueueDestroy;
EVT_WDF_FILE_CONTEXT_CLEANUP_CALLBACK FileContextCleanup;
EVT_WDF_FILE_CONTEXT_DESTROY_CALLBACK FileContextDestroy;
```

After you have declared your driver callback functions using role type declarations, you can [scan the driver](scanning-the-driver.md). Scanning the driver produces the Sdv-map.h file, which you can examine to determine if the entry points were correctly identified.

### <span id="running_code_analysis_for_drivers_to_verify_the_function_declarations"></span><span id="RUNNING_CODE_ANALYSIS_FOR_DRIVERS_TO_VERIFY_THE_FUNCTION_DECLARATIONS"></span> Running Code Analysis for Drivers to verify the function declarations

To help you determine whether the source code is prepared, run [Code Analysis for Drivers](code-analysis-for-drivers.md). Code Analysis for Drivers checks for function role type declarations and can help identify function declarations that might have been missed or warn you when the parameters of the function definition do not match those in the function role type.

### <span id="function_parameters_and_function_role_types"></span><span id="FUNCTION_PARAMETERS_AND_FUNCTION_ROLE_TYPES"></span>Function Parameters and Function Role Types

As required in the C programming language, the parameter types that you use in the function definition must match the parameter types of the function prototype, or in this case, the function role type. SDV depends upon the function signatures for analysis and ignores functions whose signatures do not match.

For example, you should declare an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine using the EVT\_WDF\_DRIVER\_DEVICE\_ADD function role type.

```
EVT_WDF_DRIVER_DEVICE_ADD myEvtDriverDeviceAdd;
```

When you implement the function *myEvtDriverDeviceAdd*, the parameter types must match those used by EVT\_WDF\_DRIVER\_DEVICE\_ADD, namely, WDFDRIVER and PWDFDEVICE\_INIT (see [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine for syntax).

```
NTSTATUS
 myEvtDriverDeviceAdd (
  WDFDRIVER Driver,
 PWDFDEVICE_INIT DeviceInit
 )
{
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Declaring%20Functions%20by%20Using%20Function%20Role%20Types%20for%20KMDF%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




