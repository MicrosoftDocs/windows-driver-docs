---
title: Using PnP Hardware Profile Change Notification
author: windows-driver-content
description: Using PnP Hardware Profile Change Notification
ms.assetid: 341464e4-507d-43da-88a2-5bfecd2dd02a
keywords: ["notifications WDK PnP , hardware profile changes", "hardware profile change notifications WDK PnP", "EventCategoryHardwareProfileChange notification", "profile change notifications WDK PnP", "machine hardware profile change notifications WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using PnP Hardware Profile Change Notification


## <a href="" id="ddk-using-pnp-hardware-profile-change-notification-kg"></a>


A driver registers for **EventCategoryHardwareProfileChange** notification so the driver can be notified when the machine transitions from one hardware profile to another. For example, a driver can use this mechanism to be notified when a laptop is docked or undocked.

The following subsections discuss how to register for hardware profile change notification and how to handle hardware profile change events in a PnP notification callback routine:

[Registering for Hardware Profile Change Notification](registering-for-hardware-profile-change-notification.md)

[Handling Hardware Profile Change Events](handling-hardware-profile-change-events.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20PnP%20Hardware%20Profile%20Change%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


