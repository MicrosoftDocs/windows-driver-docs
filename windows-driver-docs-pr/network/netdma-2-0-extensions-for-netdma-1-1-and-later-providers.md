---
title: NetDMA 2.0 Extensions for NetDMA 1.1 and Later Providers
description: NetDMA 2.0 Extensions for NetDMA 1.1 and Later Providers
ms.assetid: 2fc3de6d-56d9-47df-b420-f1ccc5f28c5e
keywords:
- extensions WDK NetDMA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NetDMA 2.0 Extensions for NetDMA 1.1 and Later Providers


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




NetDMA 2.0 extends the NetDMA 1.0 interface to version 1.1. NetDMA 1.1 provider drivers can obtain the NetDMA version and also can indicate NetDMA Plug and Play (PnP) and power management events.

**Note**  The [**NetDmaGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff568329) function is not available in NetDMA version 1.0. To avoid using a function import that might stop the driver from loading, a NetDMA 1.1 or later provider driver must verify the presence of **NetDmaGetVersion** before it calls **NetDmaGetVersion** to obtain the NetDMA version. To call **NetDmaGetVersion**, first call the [**NdisGetRoutineAddress**](https://msdn.microsoft.com/library/windows/hardware/ff562665) function to get the entry point and then, if **NetDmaGetVersion** is available, call **NetDmaGetVersion** at the entry point that **NdisGetRoutineAddress** provided. If the provider driver cannot get the address of **NetDmaGetVersion**, the supported NetDMA interface must be version 1.0.

 

NetDMA 2.0 includes power management extensions for NetDMA 1.1 and later NetDMA providers. Because a NetDMA 1.0 provider cannot notify the NetDMA interface or NetDMA clients that it is entering a low-power state, the NetDMA 1.0 driver must ensure that the DMA engine remains available while a client continues posting DMA copy requests.

To ensure that the DMA engine remains available, NetDMA 1.0 providers declare themselves to the PnP and power management systems as a device in the paging path. This action forces the PnP manager to turn off the NetDMA provider device after all of the network I/O operations are complete and turn the device back on before any networking I/O operations are started.

NetDMA 1.0 providers must also reinitialize the DMA engine before they can resume DMA operations. Because the NetDMA 1.0 interface does not receive any notifications about the power state of the device, NetDMA might try to continue using the DMA device "Append" operation. However, the DMA device might have lost the hardware context (that is, the address of the last completed DMA descriptor) that is required to perform an "Append" operation.

To ensure that NetDMA does not issue a DMA "Append" operation after the hardware context is lost, the NetDMA 1.0 interface provides the ability to request a "Start" operation with a **NULL** (nothing to copy) DMA operation. This "Start" request enables the NetDMA 1.0 provider to force the NetDMA interface to reinitialize the DMA engine with the correct DMA descriptor.

NetDMA 2.0 provides an interface for NetDMA 1.1 and later drivers to notify the NetDMA interface when a provider will transition to a low-power state and again when the provider completes the transition back to the working power state. The NetDMA interface propagates the provider notifications to the NetDMA clients.

To make a power state change notification, the NetDMA provider calls the [**NetDmaPnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff568332) function and specifies one of the [**NET\_DMA\_PNP\_NOTIFICATION\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff568736) values in the **NotificationCode** member of the [**NET\_DMA\_PNP\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff568735) structure.

A **NetDmaNotificationProviderPowerDown** notification before the DMA device transitions to a low-power state gives NetDMA clients the opportunity to stop using DMA copy services and to wait for outstanding DMA copy requests on all the channels that are allocated on that provider to complete before the provider transitions to low-power state.

A **NetDmaNotificationProviderPowerUp** notification after the DMA device is in the working power state enables the NetDMA interface to re-initialize the DMA engine with a "Start" operation on all of the allocated channels on that provider and then notify the NetDMA clients that they can start using the DMA services on all of the channels that are allocated on that provider.

 

 





