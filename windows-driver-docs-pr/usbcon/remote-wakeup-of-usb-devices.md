---
description: This topic describes best practices for implementing the remote wake-up capability in a client driver.
title: Remote wake-up of USB devices
ms.date: 03/18/2022
---

# Remote wake-up of USB devices

USB devices that can respond to external wake signals while suspended are said to have a *remote wake-up* capability. Examples of devices that have a remote wake-up capability are mice, keyboards, USB hubs, modems (wake on ring), NICs, wake on cable insertion. All of these devices are capable of producing remote wake signaling. Devices that are not capable of generating remote wake signaling include video cameras, mass storage devices, audio devices, and printers.

Drivers for devices that support remote wake-up signaling must issue an [**IRP\_MN\_WAIT\_WAKE**](../kernel/irp-mn-wait-wake.md) IRP, also known as a wait wake IRP, to arm the device for remote wake-up. The wait wake mechanism is described in the section [Supporting Devices That Have Wake-Up Capabilities](../kernel/supporting-devices-that-have-wake-up-capabilities.md).

## Remote wake-up on a USB leaf device

In USB terminology, a USB device is enabled for remote wake-up when its DEVICE\_REMOTE\_WAKEUP feature is set. The USB specification specifies that host software must set the remote wake-up feature on a device "only just prior" to putting the device to sleep.

For this reason, the USB stack does not set the DEVICE\_REMOTE\_WAKEUP feature on a device after receiving a wait wake IRP for the device. Instead, it waits until it receives a [**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md) request to change the WDM device state of the device to D1/D2. Under most circumstances, when the USB stack receives this request, it both sets the remote wake-up feature on the device and puts the device to sleep by suspending the device's upstream port. When you design and debug your driver, you should keep in mind that there is a loose relationship between arming a USB device for wake-up in software, by means of a wait wake IRP, and arming the device for wake-up in hardware by setting the remote wake-up feature.

The USB stack does not enable the device for remote wake-up when it receives a request to change the device to a sleep state of D3, because according to the WDM power model, devices in D3 cannot wake the system.

## Wake-up behavior when attaching or detaching a USB device

Another unique aspect of the USB implementation of the WDM power mode regards the arming of USB hubs for remote wake-up. If a USB leaf device on the bus is armed for wake, the USB stack will also arm the USB host controller for wake, but it will not necessarily arm any of the USB hubs upstream of the device. The USB hub driver arms a hub for remote wake-up only if the USB stack is configured to wake up the system on attach and detach (plug/unplug) events.

Universal Host Controller Interface (UHCI) USB host controllers do not distinguish between remote wake signaling and connect change events on root hub ports. This means the system will always wake from a low system power state when a USB device is connected to or disconnected from a root hub port if there is at least one device behind the UHCI controller that is armed for wake.

## Related topics

[USB Power Management](usb-power-management.md)
