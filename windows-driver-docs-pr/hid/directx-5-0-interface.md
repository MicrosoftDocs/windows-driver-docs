---
title: DDirectX 5.0 Interface
description: DirectX 5.0 interface
keywords:
- joysticks WDK HID , interfaces
- virtual joystick drivers WDK HID , interfaces
- VJoyD WDK HID , interfaces
- interfaces WDK joysticks
- joysticks WDK HID , callbacks
- virtual joystick drivers WDK HID , callbacks
- VJoyD WDK HID , callbacks
- callbacks WDK joysticks
- polling WDK joysticks
- joysticks WDK HID , versions
- VJoyD WDK HID , versions
ms.date: 01/11/2024
---

# DirectX 5.0 interface

VJoyD and any of its previous versions can't recognize the DirectX 5.0, and later interfaces. So, it's imperative that a minidriver checks the version of VJoyD before it attempts to register. VJoyD doesn't support the standard version message. So, you must get the device descriptor block (DDB) for VJoyD to implement this manually, and then check the version marked in the DDB. For more information on how this can be implemented, see the sample driver for an example. Notice that the version marked in the DDB isn't the same as the version marked in the version resource.

The process by which a minidriver registers its callbacks is extended significantly and it starts in DirectX 5.0.

Either VJoyD, as before, or an external owner (such as the HID stack) can load Minidrivers. When VJoyD loads a device, it requires the minidriver to register itself using the VJoyD VJOYD_Register_Device_Driver service. However, the minidriver may receive three system control messages, which should prompt it to register. The first is the SYS_DYNAMIC_DEVICE_INIT message, which the minidriver receives if the VxD isn't loaded before VJoyD loads it. This uses the same mechanism as the original interface used for registration. Because it's a fresh load of the VxD, any defined INIT sections are available. On receipt of this message, the VxD performs internal initialization and then registers with VJoyD.

If an application has already loaded minidriver (for example, if an application has loaded it to use a private IOCTL interface), it doesn't receive this message again when VJoyD loads it. In these circumstances, Windows 98 issues the SYS_DYNAMIC_DEVICE_REINIT message and a minidriver, in response, should register with VJoyD. Because this isn't a fresh load of the VxD, the INIT sections are no longer available. For minidrivers that doesn't run under Windows 98, VJoyD takes the lack of response to load a minidriver as that the VxD is already loaded. VJoyD issues the directed system control message BEGIN_RESERVED_PRIVATE_SYSTEM_CONTROL, to which the minidriver should register in response.

In addition to the load-time registration, VJoyD now accepts new types of registration when a driver detects a change in state of a device that it drives. Besides the callbacks, the DirectX 5.0 interface allows various control parameters and device descriptions to be set on registration. This includes the full description of the device (complete with the calibration information), which it can change to fit any other device that it detects.

The joystick minidriver callbacks for the DirectX 5.0 and later interface consist of control callbacks, a polling callback, and force feedback callbacks. To accommodate these changes, the VJoyD VJOYD_Register_Device_Driver service is overloaded so that EAX holds 0xFFFFFFFF to signal that the new registration is in use, and ECX holds a pointer to a structure that holds the parameters. The values of EBX and EDX are undefined and driver may assume that EBX returns from the call uncorrupted.

The following table shows a joystick minidriver registration sequence:

| &nbsp; | &nbsp; |
|--|--|
| mov | eax, 0ffffffffh |
| mov | ecx, offset32 RegData |
| VxDcall | VJOYD_Register_Device_Driver |

The **[VJREGDRVINFO](/previous-versions/windows/hardware/drivers/ff543581(v=vs.85))** structure is passed to the new registration.

The **dwFunction** member of the VJREGDRVINFO structure must be VJRT_LOADED; all other values are reserved. VJRT_LOADED is used in the new interface in the same way that the registration is used in the original interface. That is, to pass the callbacks to VJoyD in response to the minidriver being loaded.

The control callbacks and the poll callback are merged into a single table because all drivers must supply the control callbacks and few devices are output only. These callbacks are registered using the **[VJPOLLREG](/previous-versions/windows/hardware/drivers/ff543577(v=vs.85))** structure.

The **lpCfg** member of the VJPOLLREG structure points to a standard configuration manager callback, exactly like the CfgRoutine in the original interface. The major difference is that VJoyD calls the configuration manager callback as appropriate. VJoyD links drivers to the installed device nodes and calls this callback to inform the driver of configuration manager activity. Whereas the previous interface called all loaded drivers for each configuration manager callback, the DirectX 5.0 and later interface only calls the one driver it has linked to the device node that has changed. Also, because configuration manager activity may happen while the driver isn't loaded, VJoyD implements a primitive caching system so that if a device node has been started, the driver is informed of this device node when it's loaded.

Because drivers are always called for their resource allocations, they shouldn't check default ports to find the resources they need. Unfortunately, drivers that had to find some way to work with the previous interface still work in the old way. This means that while VJoyD only allocates a set of resources to a single driver, any old drivers that are loaded can still use ports that haven't been allocated to them. When resources have been allocated, the driver should perform any handshaking required with the device to determine the device state.

The **[Initialize](/previous-versions/ff541025(v=vs.85))** callback (pointed to by the **fpInitialize** member of the VJPOLLREG structure) replaces the *JoyId* callback in the previous interface. The main difference is that VJoyD passes back to the driver any device instance identification that the device passed to VJoyD during registration so the instances can be distinguished if the driver supports more than one device.

> [!NOTE]
> If you need to open registry keys, you should use the [VJOYD_OpenConfigKey_Service](/previous-versions/ff543545(v=vs.85)) and [VJOYD_OpenTypeKey_Service](/previous-versions/ff543549(v=vs.85)) macros instead of opening the registry keys directly. Using these service macros ensures that the correct registry branch is opened. In addition, the service macros will be supported in future versions of DirectInput when the underlying registry data may be structured differently.
