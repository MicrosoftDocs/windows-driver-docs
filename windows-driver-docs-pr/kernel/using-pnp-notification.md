---
title: Using PnP Notification
description: Using PnP Notification
keywords: ["notifications WDK PnP"]
ms.date: 03/05/2025
ms.topic: concept-article
---

# Using PnP Notification

In a PnP environment, drivers and applications need to react to changes in the configuration of devices on the machine. For example, an application needs to know when a device of interest has been added to the machine and a driver needs to know when a change occurs on a particular device.

The PnP manager provides a mechanism for drivers and applications to be notified when certain PnP events occur. This section describes how to use PnP notification in kernel-mode code. Writers of user-mode applications should see the Microsoft Windows SDK documentation for information about the [**CM_Register_Notification**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) function and related functions.

 

 




