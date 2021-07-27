---
title: Setting Up AdapterControl Routines
description: Describes how a driver's dispatch routine for a PnP IRP_MN_START_DEVICE request sets up an AdapterControl routine.
keywords: ["AdapterControl routines, setting up", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.date: 07/22/2021
ms.localizationpriority: medium
---

# Setting Up AdapterControl Routines

A driver's dispatch routine for a PnP [**IRP_MN_START_DEVICE**](irp-mn-start-device.md) request must do the following for an [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine:

1. Set up the adapter object for the device's DMA capabilities by filling in a [**DEVICE_DESCRIPTION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_description) structure and calling [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter).

1. Save the adapter object pointer and *NumberOfMapRegisters* returned by **IoGetDmaAdapter**.

    The platform-specific maximum *NumberOfMapRegisters* returned by **IoGetDmaAdapter** or the transfer capabilities of the driver's device, whichever is more restrictive, determines whether the driver must split up a given transfer request and carry out more than one DMA operation on its device to satisfy that IRP.

The returned adapter object pointer, the entry point of the driver's *AdapterControl* routine, the *DeviceObject* pointer representing the target device for the current IRP, a *Context* pointer to an area already set up for the *AdapterControl* routine, and a *NumberOfMapRegisters* value, which can be less than the maximum possible number for smaller transfer requests, must be passed in calls to [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel). Usually, a driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) (or possibly [*ControllerControl*](writing-controllercontrolroutines.md)) routine sets up the area at *Context* before it calls **AllocateAdapterChannel**.
