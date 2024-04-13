---
title: DriverEntry for WDF Drivers Routine
description: DriverEntry is the first driver-supplied routine that is called after a driver is loaded. It is responsible for initializing the driver.
keywords: ["DriverEntry routine", "routine", "DRIVER_INITIALIZE routine"]
topic_type:
- apiref
ms.topic: reference
api_type:
- NA
ms.date: 10/17/2018
---

# DriverEntry for WDF Drivers routine


\[Applies to KMDF and UMDF\]

**DriverEntry** is the first driver-supplied routine that is called after a driver is loaded. It is responsible for initializing the driver.

## Syntax

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

## Parameters

*DriverObject* \[in\]  
A pointer to a [**DRIVER\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object) structure that represents the driver's WDM driver object.

*RegistryPath* \[in\]  
A pointer to a [**UNICODE\_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure that specifies the path to the driver's [Parameters key](./introduction-to-registry-keys-for-drivers.md) in the registry.

## Return value

If the routine succeeds, it must return STATUS\_SUCCESS. Otherwise, it must return one of the error status values that are defined in *ntstatus.h*.

## Remarks

Like all WDM drivers, framework-based drivers must have a **DriverEntry** routine, which is called after the driver is loaded. A framework-based driver's **DriverEntry** routine must:

-   Activate [WPP software tracing](./using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md).

    **DriverEntry** should include a [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro to activate software tracing.

-   Call [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate).

    The call to [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate) enables the driver to use Windows Driver Framework interfaces. (The driver cannot call other framework routines before calling **WdfDriverCreate**.)

-   Allocate any non-device-specific system resources and global variables that it might need.

    Typically, drivers associate system resources with individual devices. Therefore, framework-based drivers allocate most resources in an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback, which is called when individual devices are detected.

    Because multiple instances of a UMDF driver might be hosted by separate instances of Wudfhost, a global variable might not be available across all instances of a UMDF driver.

-   Obtain driver-specific parameters from the registry.

    Some drivers obtain parameters from the registry. These drivers can call [**WdfDriverOpenParametersRegistryKey**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriveropenparametersregistrykey) to open the registry key that contains these parameters.

-   Provide a [DriverEntry return value](../kernel/driverentry-return-values.md).

**Note**  A UMDF driver runs in a user-mode host process, while a KMDF driver runs in kernel mode in a system process. The framework might load multiple instances of a UMDF driver into separate instances of the host process. As a result:

 

-   The framework might call a UMDF driver’s DriverEntry routine multiple times if it loads instances of the driver in different host processes. In contrast, the framework calls a KMDF driver's DriverEntry routine only once.
-   If a UMDF driver creates a global variable in its DriverEntry routine, the variable might may not be available to all instances of the driver. However, a global variable that a KMDF driver creates in its DriverEntry routine is available to all instances of the driver.

For more information about when a framework-based driver's **DriverEntry** routine is called, see [Building and Loading a WDF Driver](./building-and-loading-a-kmdf-driver.md).

The **DriverEntry** routine is not declared in WDK headers. Static Driver Verifier (SDV) and other verification tools may require a declaration such as the following:

``` syntax
DRIVER_INITIALIZE MyDriverEntry;

NTSTATUS
DriverEntry(
    IN PDRIVER_OBJECT  DriverObject,
    IN PUNICODE_STRING  RegistryPath
    )
{
// Function body
}
```

## Examples

The following code example shows the Serial (KMDF) sample driver's **DriverEntry** routine.

```cpp
NTSTATUS
DriverEntry(
    IN PDRIVER_OBJECT  DriverObject,
    IN PUNICODE_STRING  RegistryPath
    )
{
    WDF_DRIVER_CONFIG  config;
    WDFDRIVER  hDriver;
    NTSTATUS  status;
    WDF_OBJECT_ATTRIBUTES  attributes;
    SERIAL_FIRMWARE_DATA driverDefaults;

    //
    // Initialize WPP tracing.
    //
    WPP_INIT_TRACING(
                     DriverObject,
                     RegistryPath
                     );

    SerialDbgPrintEx(
                     TRACE_LEVEL_INFORMATION,
                     DBG_INIT,
                     "Serial Sample (WDF Version) - Built %s %s\n",
                     __DATE__, __TIME__
                     );
    //
    // Register a cleanup callback function (which calls WPP_CLEANUP)
    // for the framework driver object. The framework will call
    // the cleanup callback function when it deletes the driver object,
    // before the driver is unloaded.
    //
    WDF_OBJECT_ATTRIBUTES_INIT(&attributes);
    attributes.EvtCleanupCallback = SerialEvtDriverContextCleanup;

    WDF_DRIVER_CONFIG_INIT(
                           &config,
                           SerialEvtDeviceAdd
                           );

    status = WdfDriverCreate(
                             DriverObject,
                             RegistryPath,
                             &attributes,
                             &config,
                             &hDriver
                             );
    if (!NT_SUCCESS(status)) {
        SerialDbgPrintEx(
                         TRACE_LEVEL_ERROR,
                         DBG_INIT,
                         "WdfDriverCreate failed with status 0x%x\n",
                         status
                         );
        //
        // Clean up tracing here because WdfDriverCreate failed.
        //
        WPP_CLEANUP(DriverObject);
        return status;
    }

    //
    // Call an internal routine to obtain registry values
    // to use for all the devices that the driver 
    // controls, including whether or not to break on entry.
    //
    SerialGetConfigDefaults(
                            &driverDefaults,
                            hDriver
                            );

    //
    // Break on entry if requested bt registry value.
    //
    if (driverDefaults.ShouldBreakOnEntry) {
        DbgBreakPoint();
    }

    return status;
}
```

## See also


[**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate)

[*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)

