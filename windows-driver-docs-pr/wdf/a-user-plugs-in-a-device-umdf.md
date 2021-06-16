---
title: A User Plugs in a Device (UMDF 1)
description: A User Plugs in a Device
keywords:
- power management scenarios WDK UMDF , plugging in a device
- plugging in a device scenario WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A User Plugs in a Device (UMDF 1)


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

When a user plugs in a device, the framework calls a UMDF driver's PnP and Power Management callback methods in the following sequence, starting from the Device Arrived state at the bottom of the figure:

![device enumeration and startup sequence for a umdf driver.](images/umdf-powerup-sequence.png)

The framework begins by calling the driver’s [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback so that the driver can create a device callback object and a framework device object to represent the device. The framework continues calling the driver’s callback routines by progressing up through the sequence until the device is operational.

The framework proceeds through this sequence for each UMDF function or filter driver that supports the device, one driver at a time, starting with the driver that is lowest in the driver stack.

