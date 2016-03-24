---
title: Supporting Power Management for DMA Devices
description: Supporting Power Management for DMA Devices
ms.assetid: abbb8f60-560f-41c9-85c5-1ec82078b99e
keywords: ["DMA operations WDK KMDF , power management", "bus-master DMA WDK KMDF , power management", "power management WDK KMDF , DMA devices", "DMA enabler objects WDK KMDF", "enabler objects WDK KMDF"]
---

# Supporting Power Management for DMA Devices


\[Applies to KMDF only\]

The DMA enabler object defines a set of optional event callback functions that drivers for DMA devices can use to manage transitions into and out of a device's working (D0) state.

Each time a DMA device enters its working state, and after the framework has called the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function, the framework calls the following DMA callback functions, in the order that they are listed:

<a href="" id="---------evtdmaenablerfill--------"></a>[*EvtDmaEnablerFill*](https://msdn.microsoft.com/library/windows/hardware/ff540932)  
Allocates a device's DMA buffers.

<a href="" id="---------evtdmaenablerenable--------"></a>[*EvtDmaEnablerEnable*](https://msdn.microsoft.com/library/windows/hardware/ff540929)  
Enables a device's DMA capability after the device enters its working (D0) state.

<a href="" id="---------evtdmaenablerselfmanagediostart--------"></a>[*EvtDmaEnablerSelfManagedIoStart*](https://msdn.microsoft.com/library/windows/hardware/ff541663)  
Starts a DMA device's self-managed I/O operations.

Each time a DMA device leaves its working state, and before the framework has called the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback functions, the framework calls the following DMA callback functions, in the order that they are listed:

<a href="" id="---------evtdmaenablerselfmanagediostop--------"></a>[*EvtDmaEnablerSelfManagedIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541677)  
Stops a DMA device's self-managed I/O operations.

<a href="" id="---------evtdmaenablerdisable--------"></a>[*EvtDmaEnablerDisable*](https://msdn.microsoft.com/library/windows/hardware/ff540927)  
Disables a device's DMA capability before the device leaves its working (D0) state.

<a href="" id="---------evtdmaenablerflush--------"></a>[*EvtDmaEnablerFlush*](https://msdn.microsoft.com/library/windows/hardware/ff541655)  
Deallocates a device's DMA buffers.

For more information about the order in which the framework calls a driver's event callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Power%20Management%20for%20DMA%20Devices%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




