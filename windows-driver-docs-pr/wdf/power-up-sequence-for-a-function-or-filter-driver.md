---
title: Power Up Sequence for a Function or Filter Driver
description: Power Up Sequence for a Function or Filter Driver
ms.assetid: 3E904641-A1E2-400C-A201-2D1D2D359657
---

# Power-Up Sequence for a Function or Filter Driver


The following figure shows the order in which the framework calls a KMDF function or filter driver's event callback functions when bringing a device to the fully operational state, starting from the Device Inserted state at the bottom of the figure:

![device enumeration and power-up sequence for function or filter driver](images/fdo-fido-powerup.png)

The broad horizontal lines mark the steps that are involved in starting a device. The column on the left side of the figure describes the step, and the column on the right lists the event callbacks that accomplish it.

At the bottom of the figure, the device is not present on the system. When the user inserts the device, the framework begins by calling the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback so that the driver can create a device object to represent the device. The framework continues calling the driver’s callback routines by progressing up through the sequence until the device is operational. Remember that the framework invokes the event callbacks in bottom-up order as shown in the figure, so [*EvtDeviceFilterRemoveResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540872) is called before [*EvtDeviceFilterAddResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540870) and so on. If the device was stopped to rebalance resources or was physically present but in a low-power state, not all of the steps are required, as the figure shows.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Power-Up%20Sequence%20for%20a%20Function%20or%20Filter%20Driver%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




