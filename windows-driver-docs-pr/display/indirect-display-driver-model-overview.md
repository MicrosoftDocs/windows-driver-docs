---
title: Indirect display driver model overview
description: The indirect display driver model was designed to provide a simple user mode driver model to support monitors that are not connected to traditional GPU display outputs.
ms.assetid: E2E64500-5F99-42A7-8945-B496026EA142
ms.date: 07/17/2020
ms.localizationpriority: medium
---

# Indirect display driver model overview

The indirect display driver (IDD) model was designed to provide a simple user-mode driver model to support monitors that are not connected to traditional GPU display outputs. An example is a dongle connected to the PC via USB that has a regular (VGA, DVI, HDMI, DP etc) monitor connected to it.

## IDD implementation

An IDD is implemented as a [UMDF](../wdf/getting-started-with-umdf-version-2.md) class extension. The IDD is the developer-provided UMDF driver for the device, using the functionality exposed by the [IddCx](/windows-hardware/drivers/ddi/iddcx/) (Indirect Display Driver Class eXtension) to interface with the windows graphics sub-systems.

![indirect display driver within UMDF architecture](images/idd_umdf_arch.png)

## IDD functionality

Because the IDD is a UMDF driver, it is responsible for all UMDF functionality such as device communications, power management, plug and play etc. The IDD uses the IddCx interface to interact with the Windows graphics sub-system in the following ways:

* Create the graphics adapter representing the indirect display device
* Report monitors being connected and disconnected from the system
* Provide descriptions of the monitors connected
* Provide available display modes
* Support other display functionality, like hardware mouse cursor, gamma, I2C communications, and protected content
* Process the desktop images to display on the monitor

The IDD runs in [Session 0](../wdf/session-zero-guidelines-for-umdf-drivers.md) without any components running in the user session, so any driver instability will not affect the stability of the system as a whole.

## User-mode model

The IDD is a user-mode only model with no support for kernel-mode components. As such, the driver is able to use any DirectX APIs in order to process the desktop image. In fact, the IddCx provides the desktop image to encode in a DirectX surface. The driver should not call user-mode APIs that are not appropriate for driver use, such as GDI, windowing APIs, OpenGL, or Vulkan.

> [!NOTE]
>
> The IDD should be built as a [universal windows driver](../gettingstarted/writing-a-umdf-driver-based-on-a-template.md) so it can be used on multiple Windows platforms.

At build time, the UMDF IDD declares the version of IddCx it was built against and the OS ensures that the correct version of IddCx is loaded when the driver is loaded.

The following sections describe the IDD Model:

[IddCx Objects](iddcx-objects.md)  
[Debugging](indirect-display-debugging.md)

## Sample code

Microsoft provides a sample IDD implementation at the [Windows Driver Samples GitHub](https://github.com/microsoft/Windows-driver-samples/tree/master/video/IndirectDisplay). This sample demonstrates how to connect a monitor, how to respond to a mode set, and how to receive frames.