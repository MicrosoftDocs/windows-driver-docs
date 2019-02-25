---
title: Overview of Device Setup Classes
description: Overview of Device Setup Classes
ms.assetid: 318ec3f4-f2c2-437c-a767-494ac240cb89
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Device Setup Classes


To facilitate device installation, devices that are set up and configured in the same manner are grouped into a device setup class. For example, SCSI media changer devices are grouped into the MediumChanger device setup class. The device setup class defines the class installer and class co-installers that are involved in installing the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For example, a camera vendor does not have to define a new setup class because cameras fall under the Image setup class. Similarly, uninterruptible power supply (UPS) devices fall under the Battery class.

There is a GUID associated with each device setup class. System-defined setup class GUIDs are defined in *Devguid.h* and typically have symbolic names of the form GUID_DEVCLASS_*Xxx*.

The device setup class GUID defines the **..\\CurrentControlSet\\Control\\Class\\**<em>ClassGuid</em> registry key under which to create a new subkey for any particular device of a standard setup class.

 

 





