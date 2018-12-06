---
Description: A USB function driver supports runtime idle detection by implementing USB selective suspend. 
title: Selective suspend in USB drivers (WDF)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selective suspend in USB drivers (WDF)


A USB function driver supports runtime idle detection by implementing USB selective suspend. Here is content for driver developers about how to implement selective suspend in USB drivers that are based on the Windows® Driver Foundation (WDF).

## About selective suspend


Selective suspend is the ability to power down and later resume an idle USB device while the computer to which it is attached remains in the working state (S0). For energy-efficient operation—especially on mobile PCs—all USB devices and drivers should support selective suspend. Powering down a device when it is idle, but while the system remains in the S0 state, has the following significant advantages:

-   Selective suspend saves power.
-   Selective suspend can help reduce environmental factors such as thermal load and noise.

If your device hardware can power down while it is idle, the driver should support this feature. Selective suspend support in a USB driver that is based on the Windows® Driver Foundation (WDF) requires at most a few extra callbacks beyond those required for basic Plug and Play support.

Every function driver for a USB device should implement aggressive power management that suspends an idle device while the system is running. This topic describes how to implement selective suspend in a WDF-based driver. If you are not familiar with WDF, see the Windows Driver Kit (WDK) and Developing Drivers with the Windows Driver Foundation.

USB devices support runtime idle detection through USB selective suspend. Selective suspend allows an idle device to be put into a suspended state without affecting other devices that are connected to the same hub or—in the case of a multifunction device—without affecting the other functions in the device. When all devices or functions have been suspended, the entire hub or multifunction device can be powered down.

From the hardware perspective, selective suspend is a physical state on a USB port. When all functions that are attached to the port are idle, the port can enter selective suspend.

To conform to the USB specification, all USB devices must support selective suspend. When the USB bus is idle, the device must be able to power down. The Microsoft-supplied USB hub drivers implement selective suspend at the hardware level.

USB function drivers should implement selective suspend for their individual device functions through WDF, which communicates with the bus drivers and manages the device I/O control requests that suspend and resume device functions. WDF enables both kernel-mode and user-mode drivers to support selective suspend.

The details of a function driver’s USB selective suspend code depend on whether the driver runs in user mode or kernel mode. Consider these guidelines:

-   Use the user-mode driver framework (UMDF) to implement USB drivers whenever possible. User-mode drivers are less likely to corrupt system data and are simpler to debug than kernel-mode drivers.
-   Use the kernel-mode driver framework (KMDF) only if the driver streams data through isochronous endpoints or requires other features or resources that are available only in kernel mode.

## Power policy ownership, I/O queues, and selective suspend


The power policy owner (PPO) for a device stack is the driver that determines which power state the device should be in at any given time. Only one driver in each device stack can be the PPO. The function driver typically is the PPO for its device.

If your USB driver supports selective suspend and is layered above the PPO in its device stack, the driver must not use power-managed queues. This is true for both UMDF and KMDF drivers. If requests arrive for power-managed queues while the device is suspended, the entire device stack can stall.

Figure 1 shows the flow of I/O requests to a USB driver through its I/O queues.

![flow of requests to a wdf usb driver](images/flowrequestswdfusbdriver.png)

In the figure, a request arrives for a USB driver. The framework adds the request to the appropriate queue.

If the queue is not power managed, the framework presents the request to the driver according to the dispatch type that the driver configured for the queue (sequential, parallel, or manual). The driver then handles the request.

If the queue is power managed and the device is not suspended, the framework presents the request to the driver according to the configured dispatch type.

However, if the device is suspended, the framework’s actions depend on whether the driver is the PPO for the device stack. If the driver is the PPO, the framework communicates with the USB parent drivers to power up the device. After the device has resumed, the framework presents the request to the driver.

If the driver is not the PPO, the framework takes no further actions because only the PPO can resume the device. The request remains in the queue. The device stack stalls if the PPO does not receive any requests that cause it to resume the device.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="selective-suspend-in-umdf-drivers.md" data-raw-source="[Selective suspend in UMDF drivers](selective-suspend-in-umdf-drivers.md)">Selective suspend in UMDF drivers</a></p></td>
<td><p>This topic describes how UMDF function drivers support USB selective suspend.</p></td>
</tr>
<tr class="even">
<td><p><a href="selective-suspend-in-a-kmdf-function-driver.md" data-raw-source="[Selective suspend in USB KMDF function drivers](selective-suspend-in-a-kmdf-function-driver.md)">Selective suspend in USB KMDF function drivers</a></p></td>
<td><p>This topic describes how KMDF function drivers support USB selective suspend.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Windows Driver Frameworks (WDF)](http://go.microsoft.com/fwlink/p/?linkid=53698)  
[Plug and Play - Architecture and Driver Support](http://go.microsoft.com/fwlink/p/?linkid=320985)  
[PnP and Power Management in KMDF Drivers](http://go.microsoft.com/fwlink/p/?linkid=320986)  
[When WDF Drivers Can Use Power-Managed I/O Queues](http://go.microsoft.com/fwlink/p/?linkid=320987)  
[Writing USB Drivers with WDF](http://go.microsoft.com/fwlink/p/?linkid=320988)  
[Implementing power management in USB client drivers](http://go.microsoft.com/fwlink/p/?linkid=320989)  



