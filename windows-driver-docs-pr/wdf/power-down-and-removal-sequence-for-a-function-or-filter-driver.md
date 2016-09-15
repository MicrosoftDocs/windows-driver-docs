---
title: Power-Down and Removal Sequence for a Function or Filter Driver
author: windows-driver-content
description: Power-Down and Removal Sequence for a Function or Filter Driver
ms.assetid: E5A22C91-5967-42D6-A991-42B46C72ED82
---

# Power-Down and Removal Sequence for a Function or Filter Driver

The following tables show the order in which the framework calls a KMDF function or filter driver's event callback functions when powering down and removing the device. The sequence starts at the top of the tables with an operational device that is in the working power state (D0).  The framework calls each callback function in the order presented.

**Device Operational**

| Framework Action | Callback Invoked |
|---|---|
| Suspend self-managed I/O, if driver supports it. | [EVT_WDF_DEVICE_SELF_MANAGED_IO_SUSPEND](http://msdn.microsoft.com/library/windows/hardware/ff540907) |
| Stop power-managed queues. | [EVT_WDF_IO_QUEUE_IO_STOP](http://msdn.microsoft.com/library/windows/hardware/ff541788) |
| Arm wake signal, if driver supports it. (called only during transitions to low power, not during resource rebalance or device removal) | [EVT_WDF_DEVICE_ARM_WAKE_FROM_SX](http://msdn.microsoft.com/library/windows/hardware/ff540844), [EVT_WDF_DEVICE_ARM_WAKE_FROM_S0](http://msdn.microsoft.com/library/windows/hardware/ff540843) |
| Disable DMA, if driver supports it. | [EVT_WDF_DMA_ENABLER_SELFMANAGED_IO_STOP](http://msdn.microsoft.com/library/windows/hardware/ff541677), [EVT_WDF_DMA_ENABLER_DISABLE](http://msdn.microsoft.com/library/windows/hardware/ff540927), [EVT_WDF_DMA_ENABLER_FLUSH](http://msdn.microsoft.com/library/windows/hardware/ff541655) |
| Disconnect interrupts. |[EVT_WDF_DEVICE_D0_EXIT_PRE_INTERRUPTS_DISABLED](http://msdn.microsoft.com/library/windows/hardware/ff540856), [EVT_WDF_INTERRUPT_DISABLE](http://msdn.microsoft.com/library/windows/hardware/ff541714) |
| Notify driver of state change. |[EVT_WDF_DEVICE_D0_EXIT](http://msdn.microsoft.com/library/windows/hardware/ff540855)|

**Stop here if transitioning to low-power state.**

| Framework Action | Callback Invoked |
|---|---|
| Release hardware. (not called during system shutdown if target device state is **WdfPowerDeviceD3Final**)|[EVT_WDF_DEVICE_RELEASE_HARDWARE](http://msdn.microsoft.com/library/windows/hardware/ff540890)|

**Stop here if rebalancing resources.**

| Framework Action | Callback Invoked |
|---|---|
| Purge power-managed queues. | [EVT_WDF_IO_QUEUE_IO_STOP](http://msdn.microsoft.com/library/windows/hardware/ff541788) |
| Flush I/O buffers, if driver supports self-managed I/O. |[EVT_WDF_DEVICE_SELF_MANAGED_IO_FLUSH](http://msdn.microsoft.com/library/windows/hardware/ff540901)|
| Purge non-power-managed queues. |[EVT_WDF_IO_QUEUE_IO_STOP](http://msdn.microsoft.com/library/windows/hardware/ff541788)|
| Clean up I/O buffers, if driver supports self-managed I/O. |[EVT_WDF_DEVICE_SELF_MANAGED_IO_CLEANUP](http://msdn.microsoft.com/library/windows/hardware/ff540898)|
| Delete device object's context area. |[EVT_WDF_IO_IN_CALLER_CONTEXT](https://msdn.microsoft.com/library/windows/hardware/ff541764), [EVT_WDF_OBJECT_CONTEXT_DESTROY](https://msdn.microsoft.com/library/windows/hardware/ff540841) |

**Device Removed**

As the tables show, the KMDF power-down and removal sequence involves calling the corresponding "undo" callbacks in the reverse order in which the framework called the functions that are involved in making the device operational. The framework deletes the device object after it deletes the device object context area.

 

 





