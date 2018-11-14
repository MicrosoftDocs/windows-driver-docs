---
title: Communicating with the Driver of a Child Device
description: Communicating with the Driver of a Child Device
ms.assetid: f1311941-bfba-44a4-867c-95fcbef19510
keywords:
- video miniport drivers WDK Windows 2000 , child devices
- child devices WDK video miniport , communicating with the driver
- HwVidQueryInterface
- IRP_MN_QUERY_INTERFACE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communicating with the Driver of a Child Device


## <span id="ddk_communicating_with_the_driver_of_a_child_device_gg"></span><span id="DDK_COMMUNICATING_WITH_THE_DRIVER_OF_A_CHILD_DEVICE_GG"></span>


A video miniport driver and the driver of a child device can mutually define an interface that allows the child driver to communicate with its hardware through the parent miniport driver. The child driver obtains this interface by sending an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to the video port driver for the parent miniport driver. Upon receiving such a request, the video port driver calls the miniport driver's [*HwVidQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff567358) function, if it is defined, and the miniport driver returns a pointer to the interface. The driver of the child device can then call into the miniport driver through the functions exposed by *HwVidQueryInterface* at any time.

If the miniport driver does not implement [*HwVidQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff567358) or fails the call, the video port driver passes the request to the parent of the miniport driver's device. If a child driver sends an IRP\_MN\_QUERY\_INTERFACE to another child of the miniport driver and the other child driver does not implement *HwVidQueryInterface* or fails the call, the video port driver returns an error.

Because the child driver can call into the miniport driver without the video port driver's knowledge, the miniport driver must synchronize access to itself in all of the functions exposed by [*HwVidQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff567358). It does this by calling [**VideoPortAcquireDeviceLock**](https://msdn.microsoft.com/library/windows/hardware/ff570174) and [**VideoPortReleaseDeviceLock**](https://msdn.microsoft.com/library/windows/hardware/ff570356) to grab and release the video port driver-maintained device lock, respectively.

A child device is enumerated by [*HwVidGetVideoChildDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff567341).

 

 





