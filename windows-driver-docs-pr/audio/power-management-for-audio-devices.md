---
Description: Power Management for Audio Devices
MS-HAID: 'audio.power\_management\_for\_audio\_devices'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Power Management for Audio Devices
---

# Power Management for Audio Devices


## <span id="power_management_for_audio_devices"></span><span id="POWER_MANAGEMENT_FOR_AUDIO_DEVICES"></span>


The PortCls system driver handles all power-management IRPs (see [Handling Power IRPs](kernel.handling_power_irps)) on behalf of audio adapter drivers. PortCls manages the power state of an audio device by making calls through the adapter driver's [IAdapterPowerManagement](audio.iadapterpowermanagement) and [IPowerNotify](audio.ipowernotify) interfaces. Both interfaces are optional. The adapter driver for a device that can change its power state in response to requests from PortCls should expose an IAdapterPowerManagement interface. A miniport object that requires advance warning of an impending power-down should expose an IPowerNotify interface.

In Windows Server 2003 SP1, Windows XP SP2, and later, PortCls uses timers to determine when to power down audio devices that have remained inactive for some specified time-out interval. PortCls provides default values for the time-out intervals and the target power state when a time-out occurs. Hardware vendors can optionally override these defaults with their own driver-specific values.

This section discusses the following topics:

[Implementing IAdapterPowerManagement](implementing-iadapterpowermanagement.md)

[Implementing IPowerNotify](implementing-ipowernotify.md)

[Audio Device Class Inactivity Timer Implementation](audio-device-class-inactivity-timer-implementation.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Power%20Management%20for%20Audio%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


