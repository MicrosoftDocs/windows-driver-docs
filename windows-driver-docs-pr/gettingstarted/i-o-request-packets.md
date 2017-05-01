---
title: I/O request packets
description: I/O request packets
ms.assetid: 72288D9A-86F7-4145-8470-FFA1AC26E9BF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# I/O request packets


Most of the requests that are sent to device drivers are packaged in I/O request packets ([**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)s). An operating system component or a driver sends an IRP to a driver by calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), which has two parameters: a pointer to a [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) and a pointer to an **IRP**. The **DEVICE\_OBJECT** has a pointer to an associated [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174). When a component calls **IoCallDriver**, we say the component *sends the IRP to the device object* or *sends the IRP to the driver associated with the device object*. Sometimes we use the phrase *passes the IRP* or *forwards the IRP* instead of *sends the IRP*.

Typically an IRP is processed by several drivers that are arranged in a stack. Each driver in the stack is associated with a device object. For more information, see [Device nodes and device stacks](device-nodes-and-device-stacks.md). When an [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) is processed by a device stack, the **IRP** is usually sent first to the top device object in the device stack. For example, if an **IRP** is processed by the device stack shown in this diagram, the IRP would be sent first to the filter device object (Filter DO) at the top of the device stack.

![diagram of a device node and its device stack](images/prosewaredevicenode03.png)

## <span id="Passing_an_IRP_down_the_device_stack"></span><span id="passing_an_irp_down_the_device_stack"></span><span id="PASSING_AN_IRP_DOWN_THE_DEVICE_STACK"></span>Passing an IRP down the device stack


Suppose the I/O manager sends an IRP to the Filter DO in the diagram. The driver associated with the Filter DO, AfterThought.sys, processes the IRP and then passes it to the functional device object (FDO), which is the next lower device object in the device stack. When a driver passes an IRP to the next lower device object in the device stack, we say the driver *passes the IRP down the device stack*.

Some IRPs are passed all the way down the device stack to the physical device object (PDO). Other IRPs never reach the PDO because they are completed by one of the drivers above the PDO.

## <span id="IRPs_are_self-contained"></span><span id="irps_are_self-contained"></span><span id="IRPS_ARE_SELF-CONTAINED"></span>IRPs are self-contained


The IRP structure is self-contained in the sense that it holds all of the information that a driver needs to handle an I/O request. Some parts of the IRP structure hold information that is common to all of the participating drivers in the stack. Other parts of the IRP hold information that is specific to a particular driver in the stack.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wdkgetstart\wdkgetstart]:%20I/O%20request%20packets%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




