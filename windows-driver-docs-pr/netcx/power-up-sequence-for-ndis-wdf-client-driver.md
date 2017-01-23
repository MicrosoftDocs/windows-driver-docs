---
title: Power-Up Sequence for an NDIS-WDF Client Driver
author: windows-driver-content
description: Power-Up Sequence for an NDIS-WDF Client Driver
---

# Power-Up Sequence for an NDIS-WDF Client Driver

The following figure shows the order in which NetAdapterCx calls a client miniport driver's event callback functions when bringing a device to the fully operational state, starting from the Device Inserted state at the bottom of the figure:

![device enumeration and power-up sequence for NDIS client driver](images/netcx-powerup.png)

The broad horizontal lines mark the steps that are involved in starting a device. The column on the left side of the figure describes the step, and the column on the right lists the event callbacks that accomplish it.

At the bottom of the figure, the device is not present on the system. When the user inserts the device, the framework begins by calling the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback so that the driver can create a device object to represent the device. The framework continues calling the driver’s callback routines by progressing up through the sequence until the device is operational. Remember that the framework invokes the event callbacks in bottom-up order as shown in the figure, so [*EvtDeviceFilterRemoveResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540872) is called before [*EvtDeviceFilterAddResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540870) and so on. If the device was stopped to rebalance resources or was physically present but in a low-power state, not all of the steps are required, as the figure shows.

