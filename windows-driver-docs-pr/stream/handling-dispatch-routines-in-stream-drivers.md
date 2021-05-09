---
title: Handling dispatch routines in stream drivers
description: Provides guidance for handling driver dispatch routines.
ms.date: 05/17/2018
ms.localizationpriority: medium
---

# Handling dispatch routines in stream drivers

This topic provides guidance for handling driver dispatch routines.

## AddDevice routine for AVStream minidrivers

Most AVStream minidrivers do not supply their own *AddDevice* routines. Instead, they use [**KsAddDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksadddevice), the default *AddDevice* handler installed by [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver). Minidrivers that nonetheless wish to provide their own *AddDevice* handler should follow the following guidelines.

If the driver calls [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver) during *DriverEntry* and later replaces the *AddDevice* handler, the minidriver can call [**KsAddDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksadddevice) from within this routine, to perform the default add handling.

The minidriver may call [**KsCreateDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatedevice) from this routine, passing in a nominally optional [**KSDEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_descriptor). If [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver) is not called, this is the highest level call that will create an AVStream device described by a descriptor.

If the minidriver creates its own FDO and manually attaches itself to the device stack, it should call [**KsInitializeDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedevice) to create the AVStream device.

If the driver does not provide a [**KSDEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_descriptor) and yet still creates a device, AVStream creates a default AVStream device. This device contains no filter factories and never dispatches to the minidriver. The minidriver can still instantiate [**KSFILTERFACTORY**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilterfactory) structures on the device by calling [**KsCreateFilterFactory**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatefilterfactory).

To install your own *AddDevice* handler:

```cpp
DriverObject->DriverExtension->AddDevice=MyAddDevice();
```
We recommended that AVStream minidrivers use the functionality provided by [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver), rather than override the default *AddDevice* routine supplied by the class driver.

For more information, see the [DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) callback function.

## DriverEntry routine for Stream class minidrivers

**DriverEntry** is the initial entry point for a stream class minidriver. This routine is required.

Since [**StreamClassRegisterMinidriver**](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisteradapter) performs most of the required driver initialization, the primary task of a stream class minidriver's **DriverEntry** routine is to allocate and fill in a [**HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure with driver-specific constants and entry points. The **DriverEntry** should then call **StreamClassRegisterMinidriver**.

For more information, see the [DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) callback function.

## DriverEntry function of AVStream minidriver function

The *DriverEntry* function is the initial entry point into an AVStream minidriver.

Each AVStream minidriver must have a function explicitly named *DriverEntry* in order to be loaded. *DriverEntry* is called directly by the I/O system. Usually, *DriverEntry* calls [**KsInitializeDriver**](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver) and then returns the value returned by **KsInitializeDriver**.

For more information, see the [DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) callback function.

## KsCancelRoutine function

The **KsCancelRoutine** function performs standard IRP cancel functionality: it removes the entry and then cancels and completes the request. The function is defined as a PDRIVER\_CANCEL routine. It is the default function used for **KsAddIrpToCancelableQueue** if none is provided.

This function would typically be called by the I/O subsystem on canceling an IRP but can be called directly in response to an KSMETHOD\_STREAM\_PRESENTATION Set request. As with any typical cancel routine, this function expects the I/O cancel spin lock to have been acquired upon entering the function.

Note that this routine expects the KSQUEUE\_SPINLOCK\_IRP\_STORAGE(Irp) to point to the list access spin lock as provided in **KsAddIrpToCancelableQueue**.

**KsCancelRoutine** can be used to do the preliminary list removal processing, without actually completing the IRP. If the Irp-&gt;IoStatus.Status is set to STATUS\_CANCELLED on entering this function, then the IRP will not be completed. Otherwise, the status will be set to STATUS\_CANCELLED and the IRP will be completed. This **KsCancelRoutine** can be used within a cancel routine to do the initial list and spin lock manipulation and return to the driver's completion routine to do specific processing and final IRP completion.

For more information, see the [DRIVER_CANCEL](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine.

## KsDefaultDispatchPnp function

```cpp
KSDDKAPI
_Dispatch_type_(IRP_MJ_PNP) DRIVER_DISPATCH KsDefaultDispatchPnp;
```

The **KsDefaultDispatchPnp** function is the default, main PnP dispatch handler; notifications regarding the functional device object can be directed to this handler. This function passes all notifications to the PnP device object previously set with **KsSetDevicePnpAndBaseObject** and assumes the use of a device header. When the function is passed an IRP\_MN\_REMOVE\_DEVICE, the device object is deleted.

The **KsDefaultDispatchPnp** function returns the status of the underlying physical device object IRP processing.

The **KsDefaultDispatchPnp** function is useful when there is no extra cleanup needed when removing a device beyond freeing the device header and deleting the actual device object.

For more information, see the [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.


## KsDefaultDispatchPower function

```cpp
KSDDKAPI
_Dispatch_type_(IRP_MJ_POWER) DRIVER_DISPATCH KsDefaultDispatchPower;
```

The **KsDefaultDispatchPower** function is a default main Power dispatch handler. Notifications regarding the Functional Device Object can be directed here. This function passes all notifications to the PnP Device Object previously set with **KsSetDevicePnpAndBaseObject**, and assumes the use of a device header.

The **KsDefaultDispatchPower** function is useful when there is no extra cleanup needed on power IRPs, or just as a way of completing any power IRP. It also allows specific file objects, such as the default clock imlementation, to attach themselves to the power IRPs using **KsSetPowerDispatch**, and act on them before they are completed by this routine. This function calls each power dispatch routine before completing the IRP.

For more information, see the [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

## KsDefaultForwardIrp routine

```cpp
KSDDKAPI
_Dispatch_type_(IRP_MJ_SYSTEM_CONTROL)
_Dispatch_type_(IRP_MJ_DEVICE_CONTROL)
DRIVER_DISPATCH KsDefaultForwardIrp;
```

This default handler allows dispatch routines to forward I/O requests to corresponding Physical Device Objects.

This default handler provides a way for dispatch routines to fulfill the requirement that a driver have an IRP\_MJ\_\* function handler for specific major functions.

For more information, see the [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

## See also

[KsAddDevice](/windows-hardware/drivers/ddi/ks/nf-ks-ksadddevice)

[KsCreateDevice](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatedevice)

[KSDEVICE](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice)

[KsDispatchIrp](/windows-hardware/drivers/ddi/ks/nf-ks-ksdispatchirp)

[KsInitializeDevice](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedevice)

[KsInitializeDriver](/windows-hardware/drivers/ddi/ks/nf-ks-ksinitializedriver)

[KsAddIrpToCancelableQueue](/windows-hardware/drivers/ddi/ks/nf-ks-ksaddirptocancelablequeue)

[DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)

[DRIVER\_OBJECT](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object)

[DEVICE\_OBJECT](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object)

[StreamClassRegisterMinidriver](/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisteradapter)

[HW\_INITIALIZATION\_DATA](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data)

[Writing a DriverEntry Routine](../kernel/writing-a-driverentry-routine.md)