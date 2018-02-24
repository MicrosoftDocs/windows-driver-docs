---
title: Handling dispatch routines in stream drivers
description: Provides guidance for handling driver dispatch routines.
ms.author: windowsdriverdev
ms.date: 02/23/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling dispatch routines in stream drivers

This topic provides guidance for handling driver dispatch routines.

## AddDevice routine for AVStream minidrivers

Most AVStream minidrivers do not supply their own *AddDevice* routines. Instead, they use [**KsAddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560927), the default *AddDevice* handler installed by [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683). Minidrivers that nonetheless wish to provide their own *AddDevice* handler should follow the following guidelines.

If the driver calls [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) during *DriverEntry* and later replaces the *AddDevice* handler, the minidriver can call [**KsAddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560927) from within this routine, to perform the default add handling.

The minidriver may call [**KsCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff561647) from this routine, passing in a nominally optional [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691). If [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) is not called, this is the highest level call that will create an AVStream device described by a descriptor.

If the minidriver creates its own FDO and manually attaches itself to the device stack, it should call [**KsInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff562682) to create the AVStream device.

If the driver does not provide a [**KSDEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff561691) and yet still creates a device, AVStream creates a default AVStream device. This device contains no filter factories and never dispatches to the minidriver. The minidriver can still instantiate [**KSFILTERFACTORY**](https://msdn.microsoft.com/library/windows/hardware/ff562530) structures on the device by calling [**KsCreateFilterFactory**](https://msdn.microsoft.com/library/windows/hardware/ff561650).

To install your own *AddDevice* handler:

```
DriverObject->DriverExtension->AddDevice=MyAddDevice();
```
We recommended that AVStream minidrivers use the functionality provided by [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683), rather than override the default *AddDevice* routine supplied by the class driver.

For more information, see the [DRIVER_INITIALIZE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) callback function.

## DriverEntry routine for Stream class minidrivers

**DriverEntry** is the initial entry point for a stream class minidriver. This routine is required.

Since [**StreamClassRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff568263) performs most of the required driver initialization, the primary task of a stream class minidriver's **DriverEntry** routine is to allocate and fill in a [**HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff559682) structure with driver-specific constants and entry points. The **DriverEntry** should then call **StreamClassRegisterMinidriver**.

For more information, see the [DRIVER_INITIALIZE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) callback function.

## DriverEntry function of AVStream minidriver function

The *DriverEntry* function is the initial entry point into an AVStream minidriver.

Each AVStream minidriver must have a function explicitly named *DriverEntry* in order to be loaded. *DriverEntry* is called directly by the I/O system. Usually, *DriverEntry* calls [**KsInitializeDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562683) and then returns the value returned by **KsInitializeDriver**.

For more information, see the [DRIVER_INITIALIZE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) callback function.

## KsCancelRoutine function

The **KsCancelRoutine** function performs standard IRP cancel functionality: it removes the entry and then cancels and completes the request. The function is defined as a PDRIVER\_CANCEL routine. It is the default function used for **KsAddIrpToCancelableQueue** if none is provided.

This function would typically be called by the I/O subsystem on canceling an IRP but can be called directly in response to an KSMETHOD\_STREAM\_PRESENTATION Set request. As with any typical cancel routine, this function expects the I/O cancel spin lock to have been acquired upon entering the function.

Note that this routine expects the KSQUEUE\_SPINLOCK\_IRP\_STORAGE(Irp) to point to the list access spin lock as provided in **KsAddIrpToCancelableQueue**.

**KsCancelRoutine** can be used to do the preliminary list removal processing, without actually completing the IRP. If the Irp-&gt;IoStatus.Status is set to STATUS\_CANCELLED on entering this function, then the IRP will not be completed. Otherwise, the status will be set to STATUS\_CANCELLED and the IRP will be completed. This **KsCancelRoutine** can be used within a cancel routine to do the initial list and spin lock manipulation and return to the driver's completion routine to do specific processing and final IRP completion.

For more information, see the [DRIVER_CANCEL](https://msdn.microsoft.com/en-us/library/windows/hardware/ff540742) routine.

## KsDefaultDispatchPnp function

```
KSDDKAPI 
_Dispatch_type_(IRP_MJ_PNP) DRIVER_DISPATCH KsDefaultDispatchPnp;
```

The **KsDefaultDispatchPnp** function is the default, main PnP dispatch handler; notifications regarding the functional device object can be directed to this handler. This function passes all notifications to the PnP device object previously set with **KsSetDevicePnpAndBaseObject** and assumes the use of a device header. When the function is passed an IRP\_MN\_REMOVE\_DEVICE, the device object is deleted.

The **KsDefaultDispatchPnp** function returns the status of the underlying physical device object IRP processing.

The **KsDefaultDispatchPnp** function is useful when there is no extra cleanup needed when removing a device beyond freeing the device header and deleting the actual device object.

For more information, see the [DRIVER_DISPATCH](https://msdn.microsoft.com/en-us/library/windows/hardware/ff543233) routine.


## KsDefaultDispatchPower function

```
KSDDKAPI 
_Dispatch_type_(IRP_MJ_POWER) DRIVER_DISPATCH KsDefaultDispatchPower;
```

The **KsDefaultDispatchPower** function is a default main Power dispatch handler. Notifications regarding the Functional Device Object can be directed here. This function passes all notifications to the PnP Device Object previously set with **KsSetDevicePnpAndBaseObject**, and assumes the use of a device header.

The **KsDefaultDispatchPower** function is useful when there is no extra cleanup needed on power IRPs, or just as a way of completing any power IRP. It also allows specific file objects, such as the default clock imlementation, to attach themselves to the power IRPs using **KsSetPowerDispatch**, and act on them before they are completed by this routine. This function calls each power dispatch routine before completing the IRP.

For more information, see the [DRIVER_DISPATCH](https://msdn.microsoft.com/en-us/library/windows/hardware/ff543233) routine.

## KsDefaultForwardIrp routine

```
KSDDKAPI
_Dispatch_type_(IRP_MJ_SYSTEM_CONTROL) 
_Dispatch_type_(IRP_MJ_DEVICE_CONTROL)
DRIVER_DISPATCH KsDefaultForwardIrp;
```

This default handler allows dispatch routines to forward I/O requests to corresponding Physical Device Objects.

This default handler provides a way for dispatch routines to fulfill the requirement that a driver have an IRP\_MJ\_\* function handler for specific major functions.

For more information, see the [DRIVER_DISPATCH](https://msdn.microsoft.com/en-us/library/windows/hardware/ff543233) routine.

See also
--------

[KsAddDevice](https://msdn.microsoft.com/library/windows/hardware/ff560927)

[KsCreateDevice](https://msdn.microsoft.com/library/windows/hardware/ff561647)

[KSDEVICE](https://msdn.microsoft.com/library/windows/hardware/ff561681)

[KsDispatchIrp](https://msdn.microsoft.com/library/windows/hardware/ff561709)

[KsInitializeDevice](https://msdn.microsoft.com/library/windows/hardware/ff562682)

[KsInitializeDriver](https://msdn.microsoft.com/library/windows/hardware/ff562683)

[KsAddIrpToCancelableQueue](https://msdn.microsoft.com/library/windows/hardware/ff560934)

[DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113)

[DRIVER\_OBJECT](https://msdn.microsoft.com/library/windows/hardware/ff544174)

[DEVICE\_OBJECT](https://msdn.microsoft.com/library/windows/hardware/ff543147)

[StreamClassRegisterMinidriver](https://msdn.microsoft.com/library/windows/hardware/ff568263)

[HW\_INITIALIZATION\_DATA](https://msdn.microsoft.com/library/windows/hardware/ff559682)

[Writing a DriverEntry Routine](https://msdn.microsoft.com/library/windows/hardware/ff566402)



[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AddDevice%20Routine%20for%20AVStream%20Minidrivers%20routine%20%20RELEASE:%20%282/23/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





