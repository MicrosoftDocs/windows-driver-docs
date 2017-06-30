---
title: Setting Up AdapterControl Routines
author: windows-driver-content
description: Setting Up AdapterControl Routines
ms.assetid: 0d2add25-711a-4e5d-8409-b7ce60b08858
keywords: ["AdapterControl routines, setting up", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up AdapterControl Routines


## <a href="" id="ddk-setting-up-adaptercontrol-routines-kg"></a>


A driver's dispatch routine for a PnP [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request must do the following for an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine:

1.  Set up the adapter object for the device's DMA capabilities by filling in a [**DEVICE\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff543107) structure and calling [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220).

2.  Save the adapter object pointer and *NumberOfMapRegisters* returned by **IoGetDmaAdapter**.

    The platform-specific maximum *NumberOfMapRegisters* returned by **IoGetDmaAdapter** or the transfer capabilities of the driver's device, whichever is more restrictive, determines whether the driver must split up a given transfer request and carry out more than one DMA operation on its device to satisfy that IRP.

The returned adapter object pointer, the entry point of the driver's *AdapterControl* routine, the *DeviceObject* pointer representing the target device for the current IRP, a *Context* pointer to an area already set up for the *AdapterControl* routine, and a *NumberOfMapRegisters* value, which can be less than the maximum possible number for smaller transfer requests, must be passed in calls to [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573). Usually, a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) (or possibly [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049)) routine sets up the area at *Context* before it calls **AllocateAdapterChannel**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Up%20AdapterControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


