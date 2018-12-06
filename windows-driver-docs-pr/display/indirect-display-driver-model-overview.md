---
title: Indirect Display Driver Model Overview
description: The Indirect Display driver model was designed to provide a simple user mode driver model to support monitors that are not connected to traditional GPU display outputs.
ms.assetid: E2E64500-5F99-42A7-8945-B496026EA142
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indirect Display Driver Model Overview


The Indirect Display driver model was designed to provide a simple user mode driver model to support monitors that are not connected to traditional GPU display outputs. For example, a dongle connected to the PC via USB that has a regular (VGA, DVI, HDMI, DP etc) monitor connected to it.

## <span id="Driver_Implementation"></span><span id="driver_implementation"></span><span id="DRIVER_IMPLEMENTATION"></span>Driver Implementation


The Indirect Display driver model is implemented as a UMDF class extension. The driver is the UMDF driver for the device and uses the functionality exposed by the IddCx (Indirect Display Driver Class eXtension) to interface with the windows graphics sub-systems.

## <span id="Indirect_Display_Driver_Functionality"></span><span id="indirect_display_driver_functionality"></span><span id="INDIRECT_DISPLAY_DRIVER_FUNCTIONALITY"></span>Indirect Display Driver Functionality


As the Indirect Display driver is the UMDF driver, it is responsible for all UMDF functionality like device communications, power management, plug and play etc. The IddCx provides an interface to the Indirect Display driver to interact with the Windows graphics sub-system in the following ways:

1. Create the graphics adapter representing the Indirect Display device
2. Report monitors being connected and disconnected from the system
3. Provide descriptions of the monitors connected
4. Provide available display modes
5. Support other display functionality, like hardware mouse cursor, gamma, I2C communications and protected content
6. Process the desktop images to display on the monitor
Because the Indirect Display driver is a UMDF driver running in session 0, it does not have any component running in the user session so any driver instability will not affect the stability of the system as a whole.

## <span id="User_Mode_Model"></span><span id="user_mode_model"></span><span id="USER_MODE_MODEL"></span>User Mode Model


The Indirect Display driver is a user mode only model with no support for kernel mode components, hence the driver is able to use any DirectX API's in order to process the desktop image. In fact, the IddCx provides the desktop image to encode in a DirectX surface.

**Note**  The Indirect Display driver should be built as a universal windows driver so it can be used on multiple Windows platforms.

 

At build time, the UMDF Indirect Display driver declares the version of IddCx it was built against and the OS ensures that the correct version of IddCx is loaded when the driver is loaded.

The following sections describe the Indirect Display Driver Model:

[IddCx Objects](iddcx-objects.md)
 

 





