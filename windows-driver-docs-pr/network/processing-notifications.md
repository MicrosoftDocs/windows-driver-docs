---
title: Processing Notifications
description: Processing Notifications
ms.assetid: f3e97d23-b463-4c3b-822d-b911f6fbe00e
keywords:
- notify objects WDK networking , processing notifications
- network notify objects WDK , processing notifications
- notifications WDK networking , processing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Notifications





The network configuration subsystem sends notifications to notify objects at the following intervals:

-   During networking setup--including operating system installation, installing networking capability on an operating system that did not previously support networking, upgrading the operating system, or uninstalling networking features

-   During network configuration--including adding, removing, enabling, and disabling network components, changing network components, and changing how the network configuration subsystem binds network components together

-   After an application directs the subsystem to display the properties of network components that own notify objects

To process notifications, a notify object performs the following general sequence of operations:

1.  When the notify object is loaded, it reads the system registry to form a model of the current network configuration in its internal data structures.

2.  After the network configuration subsystem sends notifications to the notify object about networking changes that the notify object previously requested, the notify object modifies its internal data structures to keep track of those changes.

3.  When the network configuration subsystem is done sending notifications to the notify object, the subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to commit the changes to the system registry.

**Note**  The notifications mentioned in the preceding sequence can also include a call to the notify object's [**INetCfgComponentControl::CancelChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547728) method in which case the notify object should revert back to the original network configuration.
Before modifying the original network configuration, the notify object should make two copies of the configuration. The notify object can modify one copy to include changes and leave the other copy in the original condition. The notify object can use the unmodified copy when reverting back to the original network configuration.

 

 

 





