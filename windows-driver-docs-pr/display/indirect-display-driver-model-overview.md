---
title: Indirect Display Driver Model Overview
description: The indirect display driver model provides a simple user mode driver model to support monitors that aren't connected to traditional GPU display outputs.
keywords:
- IddCx
- Indirect display driver, WDK
- IDD, WDK
- Indirect display driver model
- IDD model
- Indirect display driver implementation
- IDD implementation
ms.date: 12/06/2023
---

# Indirect display driver overview

The indirect display driver (IDD) model provides a simple user-mode driver model to support monitors that aren't connected to traditional GPU display outputs. For example, a dongle connected to a PC via USB that has a regular (VGA, DVI, HDMI, DP, etc.) monitor connected to it requires an IDD.

## IDD implementation

An IDD is the third party-provided [UMDF](../wdf/umdf-driver-host-process.md) driver for the device. An IDD is developed using the functionality exposed by the [IddCx](/windows-hardware/drivers/ddi/iddcx/) (Indirect Display Driver Class eXtension) to interface with the windows graphics subsystems in the following ways:

* Create the graphics adapter representing the indirect display device
* Report monitors being connected and disconnected from the system
* Provide descriptions of the monitors connected
* Provide available display modes
* Support other display functionality, like hardware mouse cursor, gamma, I2C communications, and protected content
* Process the desktop images to display on the monitor

Because an IDD is a UMDF driver, it's also responsible for implementing all [UMDF](../wdf/overview-of-the-umdf.md) functionality such as device communications, power management, plug and play etc.

The IDD runs in [Session 0](../wdf/session-zero-guidelines-for-umdf-drivers.md) without any components running in the user session, so any driver instability doesn't affect the stability of the system as a whole.

The following diagram provides an architectural overview.

:::image type="content" source="images/idd_umdf_arch.png" alt-text="Diagram that shows the indirect display driver within the UMDF architecture.":::

## User-mode model

The IDD is a user-mode only model with no support for kernel-mode components. As such, the driver is able to use any DirectX APIs in order to process the desktop image. In fact, the IddCx provides the desktop image to encode in a DirectX surface.

> [!NOTE]
>
> The driver should not call user-mode APIs that are not appropriate for driver use, such as GDI, windowing APIs, OpenGL, or Vulkan.
>
> The IDD should be built as a [universal windows driver](../gettingstarted/writing-a-umdf-driver-based-on-a-template.md) so it can be used on multiple Windows platforms.

At build time:

* The UMDF IDD declares the version of IddCx it was built against.
* The OS ensures that the correct version of IddCx is loaded when the driver is loaded.

## IddCx callback and function naming conventions

| Prefix | Type | Notes |
| ------ | ---- | ----- |
| **EVT_IDD_CX**\_*XXX* | IDD callback function | IDDs implement both IddCx-specific callbacks such as [**EVT_IDD_CX_ADAPTER_COMMIT_MODES**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_commit_modes), and relevant WDF callbacks such as [**EVT_WDF_DEVICE_D0_EXIT**](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit). |
| **IddCx***Xxx* | Function | System-supplied IddCx class extension functions that IDDs can call; for example, [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync). |
| **PFN_IDDCX**\_*XXX* | Pointers to IddCx functions | IDDs don't use these pointers. Instead, drivers should use the equivalent **IddCx***Xxx* functions. |

## Sample code

Microsoft provides a sample IDD implementation at the [Windows Driver Samples GitHub](https://github.com/Microsoft/Windows-driver-samples/tree/main/video/IndirectDisplay). This sample demonstrates how to connect a monitor, how to respond to a mode set, and how to receive frames.
