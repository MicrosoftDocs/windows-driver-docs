---
title: Using PnP Hardware Profile Change Notification
description: Using PnP Hardware Profile Change Notification
ms.assetid: 341464e4-507d-43da-88a2-5bfecd2dd02a
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "machine hardware profile change notifications WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using PnP Hardware Profile Change Notification





A driver registers for **EventCategoryHardwareProfileChange** notification so the driver can be notified when the machine transitions from one hardware profile to another. For example, a driver can use this mechanism to be notified when a laptop is docked or undocked.

The following subsections discuss how to register for hardware profile change notification and how to handle hardware profile change events in a PnP notification callback routine:

[Registering for Hardware Profile Change Notification](registering-for-hardware-profile-change-notification.md)

[Handling Hardware Profile Change Events](handling-hardware-profile-change-events.md)

 

 




