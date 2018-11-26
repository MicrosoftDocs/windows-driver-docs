---
title: Surprise-Removal Sequence
description: Surprise-Removal Sequence
ms.assetid: 5A89BEDA-BAC3-476F-99B3-4E6E6DDDE5F5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Surprise-Removal Sequence


If the user removes the device without warning, by simply unplugging it without using Device Manager or the Safely Remove Hardware utility, the device is considered "surprise-removed." When this occurs, the framework follows a slightly different removal sequence. It also follows the surprise-removal sequence if another driver calls [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361) on the device, even if the device is still physically present. In the surprise-removal sequence, the framework calls the [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback before calling any of the other callbacks in the removal sequence. When the sequence is complete, the framework destroys the device object. Drivers for all removable devices must ensure that the callbacks in both the shutdown and startup paths can handle failure, particularly failures that are caused by the removal of the hardware. Any attempts to access the hardware should not wait indefinitely, but should be subject to time-outs or a watchdog timer.

The following diagram shows the callbacks that are involved in a surprise removal:

![surprise-removal sequence](images/surprise-removal.png)

If the device was not in the working state when it was removed, the framework calls the [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) event callback immediately after [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913). It omits the intervening steps, which were already performed when the device exited from the working state.

 

 





