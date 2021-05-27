---
title: Power Management for Audio Devices
description: Power Management for Audio Devices
keywords:
- audio drivers WDK , power management
- audio miniport drivers WDK , power management
- miniport drivers WDK audio , power management
- power management WDK audio
- port class drivers WDK audio
- PortCls WDK audio , power management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management for Audio Devices


## <span id="power_management_for_audio_devices"></span><span id="POWER_MANAGEMENT_FOR_AUDIO_DEVICES"></span>


The PortCls system driver handles all power-management IRPs (see [Handling Power IRPs](../kernel/handling-power-irps.md)) on behalf of audio adapter drivers. PortCls manages the power state of an audio device by making calls through the adapter driver's [IAdapterPowerManagement](/windows-hardware/drivers/ddi/portcls/nn-portcls-iadapterpowermanagement) and [IPowerNotify](/windows-hardware/drivers/ddi/portcls/nn-portcls-ipowernotify) interfaces. Both interfaces are optional. The adapter driver for a device that can change its power state in response to requests from PortCls should expose an IAdapterPowerManagement interface. A miniport object that requires advance warning of an impending power-down should expose an IPowerNotify interface.

In Windows Server 2003 SP1, Windows XP SP2, and later, PortCls uses timers to determine when to power down audio devices that have remained inactive for some specified time-out interval. PortCls provides default values for the time-out intervals and the target power state when a time-out occurs. Hardware vendors can optionally override these defaults with their own driver-specific values.

This section discusses the following topics:

[Implementing IAdapterPowerManagement](implementing-iadapterpowermanagement.md)

[Implementing IPowerNotify](implementing-ipowernotify.md)

[Audio Device Class Inactivity Timer Implementation](audio-device-class-inactivity-timer-implementation.md)

 

