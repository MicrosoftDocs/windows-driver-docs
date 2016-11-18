---
title: Setting Up LogConfig Entries
author: windows-driver-content
description: Setting Up LogConfig Entries
MS-HAID:
- 'di\_eba02a28-72bf-4c12-9b72-f060f4e32894.xml'
- 'hid.setting\_up\_logconfig\_entries'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d8317009-f8d0-4020-83b1-4cdf6366a642
keywords: ["INF files WDK joysticks , LogConfig entries", "LogConfig entries WDK joysticks"]
---

# Setting Up LogConfig Entries


## <a href="" id="ddk-setting-up-logconfig-entries-di"></a>


Devices requiring system resources such as input/output (I/O) ports use a LogConfig entry in the install section to specify which configurations they can use. Some devices do not use resources of their own. Instead, they use another driver, such as the serial port driver, to communicate with the device. The DirectX 3.0 VJoyD differs from previous versions in its handling of analog game port I/O port requirements. Older versions worked only if at least one device had been configured with either one or two I/O port allocations with ports in the standard game port range 0x200 to 0x20f. (In addition, the second I/O range had to be a single port.) The newer VJoyD works if no game ports are configured to allow systems that have no game ports to use devices operated through minidrivers. (The second I/O range can now be more than one port.)

Devices using ports in the range 0x200 to 0x20f are interpreted to be analog game ports by VJoyD, and may therefore be considered conflicting devices by the configuration manager. Any other sets of game port I/O ports are ignored; if a machine has game ports on two cards, only the ports on one card are polled. If the device needs to use a standard game port in a nonstandard way, things get even more interesting. Requesting the standard ports in LogConfig entries of the installation section for the device can work, but it usually results in a lot of reconfiguring and rebooting to swap joysticks. An alternative is to share the resources with VJoyD by using any set of I/O ranges passed through the configuration manager callback that fit the game port criteria. As long as the user does not configure joysticks to both the standard analog driver and the OEM driver, then run an application that tries to poll them both, this works well enough.

In DirectX 3.0, changes were implemented to allow an OEM VxD to be called in place of the standard analog polling by setting the JOY\_HWS\_ISGAMEPORTDRIVER flag. Control Panel allows such a device to be set up as a global driver, meaning that it, rather than the internal analog polling, gets called for any joysticks that have no minidriver associated with them. This ensures that VJoyD does not interfere with the polling of the OEM device.

If the first four devices during boot are all handled by minidrivers (which may be an OEM global driver), VJoyD does not check for -- and is not able to use -- any game ports, even if these devices are no longer handled by minidrivers. If VJoyD cannot use its ports (or if no game ports exist), returning JOY\_OEMPOLLRC\_YOUPOLL to a poll request does not cause the standard polling to be used. Reconfiguring back to devices using this polling takes effect only after the game port resources have been reallocated (probably not until a reboot).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Setting%20Up%20LogConfig%20Entries%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


