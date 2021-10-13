---
title: Surprise-Removal Sequence
description: Surprise-Removal Sequence
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Surprise-Removal Sequence


If the user removes the device without warning, by simply unplugging it without using Device Manager or the Safely Remove Hardware utility, the device is considered "surprise-removed." When this occurs, the framework follows a slightly different removal sequence. It also follows the surprise-removal sequence if another driver calls [**IoInvalidateDeviceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinvalidatedevicestate) on the device, even if the device is still physically present. In the surprise-removal sequence, the framework calls the [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback before calling any of the other callbacks in the removal sequence. When the sequence is complete, the framework destroys the device object. Drivers for all removable devices must ensure that the callbacks in both the shutdown and startup paths can handle failure, particularly failures that are caused by the removal of the hardware. Any attempts to access the hardware should not wait indefinitely, but should be subject to time-outs or a watchdog timer.

The following diagram shows the callbacks that are involved in a surprise removal:

![surprise-removal sequence.](images/surprise-removal.png)

If the device was not in the working state when it was removed, the framework calls the [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) event callback immediately after [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal). It omits the intervening steps, which were already performed when the device exited from the working state.

 

