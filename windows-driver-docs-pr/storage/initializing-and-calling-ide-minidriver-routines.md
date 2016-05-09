---
title: Initializing and Calling IDE Minidriver Routines
description: Initializing and Calling IDE Minidriver Routines
ms.assetid: ae7b19a9-0a2e-4231-b008-879b7f6c8566
keywords: ["IDE controller minidrivers WDK storage , initializing", "storage IDE controller minidrivers WDK , initializing", "IDE controller minidrivers WDK storage , calling", "storage IDE controller minidrivers WDK , calling", "initializing IDE controller minidrivers"]
---

# Initializing and Calling IDE Minidriver Routines


## <span id="ddk_initializing_and_calling_ide_minidriver_routines_kr"></span><span id="DDK_INITIALIZING_AND_CALLING_IDE_MINIDRIVER_ROUTINES_KR"></span>


All IDE controller minidrivers must provide a series of standard routines that implement hardware-specific functionality. The following figure illustrates how an IDE controller minidriver makes its routines available to the controller driver. Note that the PciIdeX library, though conceptually separate from the IDE controller driver as illustrated in the figure that follows, is contained within the controller driver's executable file, *pciidex.sys*. When a minidriver calls a PciIdeX library routine, it is in fact calling a routine within the controller driver.

![program flow for minidriver routine initialization](images/idecallbacks.png)

1.  The PnP manager loads the IDE controller driver-minidriver, then calls its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, passing it a pointer to the driver object for the controller driver.

2.  The minidriver's **DriverEntry** calls the [**PciIdeXInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff563788) library routine, passing it a pointer to the minidriver's **GetControllerProperties** routine.

3.  **PciIdeXInitialize** stores the pointer to **GetControllerProperties** in the driver object.

4.  PnP manager dispatches an IRP\_MN\_START\_DEVICE request to the IDE controller driver to start the controller. The IDE controller driver receives the request in its [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine and calls an internal routine that starts the device.

5.  The controller driver retrieves a pointer to **GetControllerProperties** that is stored in the driver object.

6.  The controller driver calls **GetControllerProperties**, passing it a pointer to an [**IDE\_CONTROLLER\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff559076) structure.

7.  **GetControllerProperties** loads pointers for a standard set of minidriver routines into IDE\_CONTROLLER\_PROPERTIES.

Once the minidriver populates the IDE\_CONTROLLER\_PROPERTIES structure with function pointers that point to the minidriver's routines, the controller driver can call them.

The routines that every minidriver must provide for the controller to call are as follows:

This routine determines whether the indicated channel is enabled.

This routine reports properties of the IDE controller hardware.

This routine indicates whether both channels of its controller can be accessed at once.

This routine returns the best PIO mode and the best DMA mode for each device indicated in *XferMode*.

This routine indicates which ultra-direct memory access (UDMA) transfer mode is current and which is best for the device.

This routine determines whether I/O can be done by means of DMA.

[**HwIdeXChannelEnabled**](https://msdn.microsoft.com/library/windows/hardware/ff557252)

[**HwIdeXGetControllerProperties**](https://msdn.microsoft.com/library/windows/hardware/ff557254)

[**HwIdeXSyncAccessRequired**](https://msdn.microsoft.com/library/windows/hardware/ff557256)

[**HwIdeXTransferModeSelect**](https://msdn.microsoft.com/library/windows/hardware/ff557260)

[**HwIdeXUdmaModesSupported**](https://msdn.microsoft.com/library/windows/hardware/ff557264)

[**HwIdeXUseDma**](https://msdn.microsoft.com/library/windows/hardware/ff557266)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Initializing%20and%20Calling%20IDE%20Minidriver%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




