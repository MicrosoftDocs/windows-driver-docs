---
title: Overview of SPB controller drivers
description: An SPB controller is a device that controls a simple peripheral bus (SPB) and that transfers data to and from the peripheral devices that are connected to the SPB.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of SPB controller drivers

An SPB controller is a device that controls a [simple peripheral bus](/previous-versions/hh450903(v=vs.85)) (SPB) and that transfers data to and from the peripheral devices that are connected to the SPB. The hardware vendor for an SPB controller provides an SPB controller driver to manage the hardware functions in the controller.

Starting with Windows 8, the SPB framework extension (SpbCx) simplifies the development of controller drivers for [simple peripheral buses](/previous-versions/hh450903(v=vs.85)) (SPBs). SpbCx is a system-supplied extension to the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF). The hardware vendor for the SPB controller device supplies a controller driver to perform all hardware-specific driver operations. This driver communicates with SpbCx to perform operations that are specific to SPB controllers, and communicates directly with KMDF to perform generic driver operations.

For example, an SPB controller driver typically calls the [**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks) method in KMDF to register to receive power event callbacks, and calls the [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) method to connect the driver's interrupt service routine (ISR) to the interrupt from the SPB controller. To perform SPB-specific operations, the SPB controller communicates with SpbCx through the [SpbCx device driver interface](/previous-versions/hh698219(v=vs.85)) (DDI).

SpbCx cooperates with the SBP controller driver to handle I/O requests for peripheral devices that are connected to the SPB. SpbCx performs processing tasks that are common to SPB controller drivers. These tasks include managing the I/O request queues for the SPB controller. These queues contain I/O requests from the drivers that manage the peripheral devices that are connected to the bus. The SPB controller driver performs all hardware-specific operations that are required to handle these requests.

The following diagram shows the SPB controller driver and SpbCx.

![block diagram of spb components.](images/spbmodules.png)

The SPB controller driver and SpbCx both run in kernel mode, and communicate with each other through the SpbCx DDI. The SPB controller driver calls driver support methods that are implemented by SpbCx. SpbCx calls event callback functions that are implemented by the SPB controller driver.

The drivers that send I/O requests to the SPB controller are either kernel-mode drivers that use the [Kernel-Mode Driver Framework](../wdf/index.md) (KMDF), or user-mode drivers that use the [User-Mode Driver Framework](/previous-versions/ff554928(v=vs.85)) (UMDF). These drivers can send read and write requests to transfer data to and from SPB-connected peripheral devices. In addition, the drivers can send I/O control (IOCTL) requests to perform SPB-specific operations.

The SPB controller driver directly accesses the hardware registers of the SPB controller device to initiate data transfers to and from peripheral devices that are connected to the SPB. For an SPB such as I²C, these data transfers occur at relatively slow speeds. Although the hardware registers of the SPB controller are likely to be memory mapped, the registers of the peripheral devices must be accessed serially through the SPB.

In response to an I/O request to transfer data to or from an SPB-connected peripheral device, the SPB controller driver initiates the bus transfer, marks the I/O request as pending, and returns without waiting for the transfer to complete. Later, when the SPB controller hardware finishes the transfer, the controller signals an interrupt, and the ISR in the SPB controller driver either completes the pending I/O request or initiates the next transfer in the requested I/O operation.

Only drivers can send I/O requests directly to an SPB controller. When a user-mode application transfers data to or from an SPB-connected peripheral device, the application must rely on the SPB peripheral device driver to send the corresponding read or write requests to the SPB controller.
