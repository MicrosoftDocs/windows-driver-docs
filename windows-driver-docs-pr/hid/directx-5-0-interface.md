---
title: DirectX 5.0 Interface
author: windows-driver-content
description: DirectX 5.0 Interface
ms.assetid: 416a9187-d64f-48a4-8868-fd5158d58a25
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

#  DirectX 5.0 Interface


## <a href="" id="ddk-the-directx-5-0-interface-di"></a>


VJoyD and any of its previous versions cannot recognize the DirectX 5.0, and later interfaces. So, it is imperative that a minidriver checks the version of VJoyD before it attempts to register. VJoyD does not support the standard version message. So, you must get the device descriptor block (DDB) for VJoyD to implement this manually, and then check the version marked in the DDB. For more information on how this can be implemented, see the sample driver for an example. Notice that the version marked in the DDB is not the same as the version marked in the version resource.

The process by which a minidriver registers its callbacks is extended significantly and it starts in DirectX 5.0.

Either VJoyD, as before, or an external owner (such as the HID stack) can load Minidrivers. When VJoyD loads a device, it requires the minidriver to register itself using the VJoyD VJOYD\_Register\_Device\_Driver service. However, the minidriver may receive three system control messages, which should prompt it to register. The first is the SYS\_DYNAMIC\_DEVICE\_INIT message, which the minidriver receives if the VxD is not loaded before VJoyD loads it. This uses the same mechanism as the original interface used for registration. Because it is a fresh load of the VxD, any defined INIT sections are available. On receipt of this message, the VxD performs internal initialization and then registers with VJoyD.

If an application has already loaded minidriver (for example, if an application has loaded it to use a private IOCTL interface), it does not receive this message again when VJoyD loads it. In these circumstances, Windows 98 issues the SYS\_DYNAMIC\_DEVICE\_REINIT message and a minidriver, in response, should register with VJoyD. Because this is not a fresh load of the VxD, the INIT sections are no longer available. For minidrivers that does not run under Windows 98, VJoyD takes the lack of response to load a minidriver as that the VxD is already loaded. VJoyD issues the directed system control message BEGIN\_RESERVED\_PRIVATE\_SYSTEM\_CONTROL, to which the minidriver should register in response.

In addition to the load-time registration, VJoyD now accepts new types of registration when a driver detects a change in state of a device that it drives. Besides the callbacks, the DirectX 5.0 interface allows various control parameters and device descriptions to be set on registration. This includes the full description of the device (complete with the calibration information), which it can change to fit any other device that it detects.

The joystick minidriver callbacks for the DirectX 5.0 and later interface consist of control callbacks, a polling callback, and force feedback callbacks. To accommodate these changes, the VJoyD VJOYD\_Register\_Device\_Driver service is overloaded so that EAX holds 0xFFFFFFFF to signal that the new registration is in use, and ECX holds a pointer to a structure that holds the parameters. The values of EBX and EDX are undefined and driver may assume that EBX returns from the call uncorrupted.

The following example shows a joystick minidriver registration sequence:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>mov</p></td>
<td><p>eax, 0ffffffffh</p></td>
</tr>
<tr class="even">
<td><p>mov</p></td>
<td><p>ecx, offset32 RegData</p></td>
</tr>
<tr class="odd">
<td><p>VxDcall</p></td>
<td><p>VJOYD_Register_Device_Driver</p></td>
</tr>
</tbody>
</table>

 

The [**VJREGDRVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff543581) structure is passed to the new registration.

The **dwFunction** member of the VJREGDRVINFO structure must be VJRT\_LOADED; all other values are reserved. VJRT\_LOADED is used in the new interface in the same way that the registration is used in the original interface, that is, to pass the callbacks to VJoyD in response to the minidriver being loaded.

The control callbacks and the poll callback are merged into a single table because all drivers must supply the control callbacks and very few devices are output only (and therefore do not need a poll callback). These callbacks are registered using the [**VJPOLLREG**](https://msdn.microsoft.com/library/windows/hardware/ff543577) structure.

The **lpCfg** member of the VJPOLLREG structure points to a standard configuration manager callback, exactly like the CfgRoutine in the original interface. The major difference is that VJoyD calls the configuration manager callback as appropriate. VJoyD links drivers to the installed device nodes and calls this callback to inform the driver of configuration manager activity. Whereas the previous interface called all loaded drivers for each configuration manager callback, the DirectX 5.0 and later interface only calls the one driver it has linked to the device node which has changed. Also, because configuration manager activity may happen while the driver is not loaded, VJoyD implements a primitive caching system so that if a device node has been started, the driver is informed of this device node when it is loaded.

Because drivers are always called for their resource allocations, they should not check default ports to find the resources they need. Unfortunately, drivers that had to find some way to work with the previous interface still work in the old way. This means that while VJoyD only allocates a set of resources to a single driver, any old drivers that are loaded can still use ports that have not been allocated to them. When resources have been allocated, the driver should perform any handshaking required with the device to determine the device state.

The [*Initialize*](https://msdn.microsoft.com/library/windows/hardware/ff541025) callback (pointed to by the **fpInitialize** member of the VJPOLLREG structure) replaces the *JoyId* callback in the previous interface. The main difference is that VJoyD passes back to the driver any device instance identification that the device passed to VJoyD during registration so the instances can be distinguished if the driver supports more than one device.

**Note**   If you need to open registry keys, you should use the [VJOYD\_OpenConfigKey\_Service](https://msdn.microsoft.com/library/windows/hardware/ff543545) and [VJOYD\_OpenTypeKey\_Service](https://msdn.microsoft.com/library/windows/hardware/ff543549) macros instead of opening the registry keys directly. Using these service macros ensures that the correct registry branch is opened. In addition, the service macros will be supported in future versions of DirectInput when the underlying registry data may be structured differently.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20%20DirectX%205.0%20Interface%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


