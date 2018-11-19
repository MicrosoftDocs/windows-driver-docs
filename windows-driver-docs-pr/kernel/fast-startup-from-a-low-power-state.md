---
title: Fast Startup from a Low-Power State
description: Fast Startup from a Low-Power State
ms.assetid: 1091571c-2e30-4ad5-b4b9-0f8633e68288
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Fast Startup from a Low-Power State


To achieve a fast startup from a low-power state, a driver for a leaf-node device should handle an S0 power IRP (that is, an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) IRP for the S0 system power state). Devices that are leaf nodes in the device hierarchy have no child devices. Because a leaf-node device has no dependencies on child devices, the functional driver for the device can reinitialize the device as a background task to avoid causing unnecessary delays to the operating system or to other drivers. In contrast, bus drivers have dependencies that require additional synchronization logic to coordinate power-on sequences with their child devices.

Use the following steps to achieve fast startup of a leaf-node device from a low-power state:

1.  Set a completion routine for the S0 power IRP.

2.  Send the S0 power IRP down the device stack.

3.  Complete the S0 power IRP immediately instead of waiting until the D0 power IRP is completed. When the completion routine for the S0 power IRP runs, do the following:

    1.  Request a D0 power IRP (that is, an **IRP\_MN\_SET\_POWER** IRP for the D0 device power state).

    2.  Return STATUS\_SUCCESS to the completion routine for the S0 power IRP.

4.  The driver should queue any I/O requests that it receives but defer handling any of these requests until it finishes processing the D0 power IRP.

5.  When the completion routine for the D0 power IRP runs, initialize the device, but limit this routine to what is required to make the device ready to use.

6.  After the previous steps are completed, your driver can begin to handle I/O requests, including any I/O requests that might already be queued.

**Note**   The preceding steps do not apply to the handling of power IRPs for any power state other than PowerSystemWorking (S0). These steps specifically apply to the handling of power IRPs for transitions from a low-power state to the power-on (S0) state.

 

A system startup is complete after all devices have completed their S0 power IRPs. These devices are not required, at the completion of system startup, to have completed their D0 power IRPs or to be fully functioning. The kernel power manager has a limited set of IRP dispatch queues and must use these queues to notify all devices in the system of the return to the S0 state. Drivers that fail to quickly complete their S0 power IRPs prevent drivers for other devices from receiving their S0 power IRPs. Thus, poorly designed drivers impair overall system startup performance by causing driver operations that should be performed concurrently to be performed serially.

After a driver completes its S0 power IRP, it might receive I/O requests from applications that have opened handles to the device. Drivers must never fail these I/O requests because doing so might cause applications to stop responding and to produce time-out error messages. Instead, drivers must queue I/O requests until the device is ready to process them.

A bus driver can achieve a fast startup from a low-power state by using a technique similar to that just described for the driver of a leaf-node device. A bus driver must meet an additional requirement, which is to ensure that any requests from child devices to enter the D0 state are marked as pending and are not completed by the bus driver until the bus device has entered the D0 state.

For example, when the bus driver for a USB hub receives an S0 power IRP, the driver requests a D0 power IRP and completes the S0 power IRP after receiving the requested D0 power IRP. However, after the S0 power IRP is completed, the hub's child devices are likely to start receiving their S0 power IRPs and requesting D0 power IRPs. The bus driver should prevent the child devices from entering D0 until the hub device enters D0. Therefore, the bus driver should mark all D0 power IRPs from child devices as pending and wait to complete these IRPs until the bus driver finishes handling the D0 power IRP for the hub and the hub device is fully initialized.

For more information about power IRPs, see the following topics:

[Handling IRP\_MN\_SET\_POWER for System Power States](handling-irp-mn-set-power-for-system-power-states.md)

[Handling IRP\_MN\_SET\_POWER for Device Power States](handling-irp-mn-set-power-for-device-power-states.md)

 

 




