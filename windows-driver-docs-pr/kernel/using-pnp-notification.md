---
title: Using PnP Notification
description: Using PnP Notification
ms.assetid: cc6c9106-37b3-473c-bbd2-89701d698fdf
keywords: ["notifications WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using PnP Notification





In a PnP environment, drivers and applications need to react to changes in the configuration of devices on the machine. For example, an application needs to know when a device of interest has been added to the machine and a driver needs to know when a change occurs on a particular device.

The PnP manager provides a mechanism for drivers and applications to be notified when certain PnP events occur. This section describes how to use PnP notification in kernel-mode code. Writers of user-mode applications should see the Microsoft Windows SDK documentation For information about the **RegisterDeviceNotification** function and related functions.

 

 




