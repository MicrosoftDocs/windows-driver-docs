---
title: Supporting Power Management for DMA Devices
description: Supporting Power Management for DMA Devices
ms.assetid: abbb8f60-560f-41c9-85c5-1ec82078b99e
keywords:
- DMA operations WDK KMDF , power management
- bus-master DMA WDK KMDF , power management
- power management WDK KMDF , DMA devices
- DMA enabler objects WDK KMDF
- enabler objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





