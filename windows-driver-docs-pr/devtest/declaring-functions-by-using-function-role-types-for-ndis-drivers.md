---
title: Declaring Functions by Using Function Role Types for NDIS Drivers
description: Declaring Functions by Using Function Role Types for NDIS Drivers
ms.assetid: 232c4272-0bf0-4a4e-9560-3bceeca8a3e3
---

# Declaring Functions by Using Function Role Types for NDIS Drivers


To enable SDV to analyze an NDIS driver, you must declare your functions by using the function role type declarations for NDIS. The function role types are defined in Ndis.h.

For the list of function role types and their corresponding event callback functions, see the [Static Driver Verifier NDIS Function Declarations](static-driver-verifier-ndis-function-declarations.md).

Each callback function in an NDIS driver must be declared by specifying the corresponding role type.

The following code example shows the function role type declaration for the *MiniportPause* callback function. In this example, the callback function is called *myMiniportPause*. The function role type is MINIPORT\_PAUSE.

```
MINIPORT_PAUSE myMiniportPause;
```

If a callback function has a function prototype declaration, you must replace the function prototype with the function role type declaration.

The following example shows NDIS function declarations from the header file MP.h, which is located in the SDV fail\_drivers subdirectory of the WDK. The related functions are declared in Main.c.

\\tools\\sdv\\samples\\fail\_drivers\\NDIS\\fail\_driver1.

```
/--------------------------------------
// Miniport routines in MAIN.C
//--------------------------------------

NDIS_STATUS
DriverEntry(
    IN  PDRIVER_OBJECT      DriverObject,
    IN  PUNICODE_STRING     RegistryPath
    );


MINIPORT_ALLOCATE_SHARED_MEM_COMPLETE MPAllocateComplete;

MINIPORT_HALT MPHalt;
MINIPORT_SET_OPTIONS MPSetOptions;
MINIPORT_INITIALIZE MPInitialize;
MINIPORT_PAUSE MPPause;
MINIPORT_RESTART MPRestart;
MINIPORT_OID_REQUEST MPOidRequest;
MINIPORT_INTERRUPT_DPC MPHandleInterrupt;
MINIPORT_ISR MPIsr;
MINIPORT_RESET MPReset;
MINIPORT_RETURN_NET_BUFFER_LISTS MPReturnNetBufferLists;
MINIPORT_CANCEL_OID_REQUEST MPCancelOidRequest;
MINIPORT_SHUTDOWN MPShutdown;
MINIPORT_SEND_NET_BUFFER_LISTS MPSendNetBufferLists;
MINIPORT_CANCEL_SEND MPCancelSendNetBufferLists;
MINIPORT_DEVICE_PNP_EVENT_NOTIFY MPPnPEventNotify;
MINIPORT_UNLOAD MPUnload;
MINIPORT_CHECK_FOR_HANG MPCheckForHang;
MINIPORT_ENABLE_INTERRUPT MpEnableInterrupt;
MINIPORT_DISABLE_INTERRUPT MpDisableInterrupt;
MINIPORT_SYNCHRONIZE_INTERRUPT MPSynchronizeInterrupt;
MINIPORT_PROCESS_SG_LIST MPProcessSGList;
NDIS_TIMER_FUNCTION MpDemonstrationTimer;
NDIS_IO_WORKITEM MPQueuedWorkItem;
```

### <span id="function_parameters_and_function_role_types"></span><span id="FUNCTION_PARAMETERS_AND_FUNCTION_ROLE_TYPES"></span>Function Parameters and Function Role Types

As required in the C programming language, the parameter types that you use in the function definition must match the parameter types of the function prototype, or in this case, the function role type. SDV depends upon the function signatures for analysis and ignores functions whose signatures do not match.

For example, you should declare an [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function using the MINIPORT\_ISR function role type:

```
MINIPORT_ISR myMPIsr;
```

When you implement the interrupt routine, *myMPIsr*, the parameter types must match those used by MINIPORT\_ISR, namely, NDIS\_HANDLE, PBOOLEAN, and PULONG (see the [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function for syntax).

```
BOOLEAN 
myMPIsr(
    __in  NDIS_HANDLE      MiniportInterruptContext,
    __out PBOOLEAN        QueueMiniportInterruptDpcHandler,
    __out PULONG          TargetProcessors
    ) {
}
```

## <span id="running_code_analysis_for_drivers_to_verify_the_function_declarations"></span><span id="RUNNING_CODE_ANALYSIS_FOR_DRIVERS_TO_VERIFY_THE_FUNCTION_DECLARATIONS"></span> Running Code Analysis for Drivers to verify the function declarations


To help you determine whether the source code is prepared, run [Code Analysis for Drivers](code-analysis-for-drivers.md). Code Analysis for Drivers checks for function role type declarations and can help identify function declarations that might have been missed or warn you when the parameters of the function definition do not match those in the function role type.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Declaring%20Functions%20by%20Using%20Function%20Role%20Types%20for%20NDIS%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




