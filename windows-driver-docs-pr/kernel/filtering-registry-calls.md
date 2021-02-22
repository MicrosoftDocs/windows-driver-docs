---
title: Filtering Registry Calls
description: Filtering Registry Calls
keywords: ["filtering registry calls WDK kernel", "registry filtering drivers WDK kernel", "RegistryCallback", "filtering registry calls WDK kernel , about filtering registry calls", "registry filtering drivers WDK kernel , about filtering registry calls"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Filtering Registry Calls


A *registry filtering driver* is any kernel-mode driver that filters registry calls, such as the driver component of an antivirus software package. The configuration manager, which implements the registry, allows registry filtering drivers to filter any thread's calls to registry functions. Filtering of registry calls was first supported in Microsoft Windows XP.

On Windows XP, a registry filtering driver can call [**CmRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallback) to register a [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine and [**CmUnRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmunregistercallback) to unregister the callback routine. The *RegistryCallback* routine receives notifications of each registry operation before the configuration manager processes the operation. A set of **REG\_*XXX*\_KEY\_INFORMATION** data structures contain information about each registry operation. The *RegistryCallback* routine can block a registry operation. The callback routine also receives notifications when the configuration manager has finished creating or opening a registry key.

Windows Server 2003 provides additional completion notifications.

Windows Vista provides the following additional registry filtering capabilities:

-   Registry filtering drivers can be layered in a driver stack, and each driver in the stack can filter a registry operation.

-   The **CmRegisterCallback** routine is replaced by the [**CmRegisterCallbackEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex) routine.

-   Drivers can completely process a registry operation (or redirect the requested operation to a different operation) and prevent the configuration manager from handling the operation.

-   Drivers can assign context information to individual registry operations or key objects.

-   Drivers can modify a registry operation's output parameters and return value.

-   Additional members have been added to all **REG\_*XXX*\_KEY\_INFORMATION** data structures.

-   Drivers receive notifications of additional registry operations.

For a list of the registry operations that a driver can filter on each version of Windows, see [**REG\_NOTIFY\_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_reg_notify_class).

To learn more about filtering registry calls, see the following topics:

[Registering for Notifications](registering-for-notifications.md)

[Handling Notifications](handling-notifications.md)

[Supporting Layered Registry Filtering Drivers](supporting-layered-registry-filtering-drivers.md)

[Specifying Context Information](specifying-context-information.md)

[Obtaining Additional Registry Information](obtaining-additional-registry-information.md)

[Invalid Key Object Pointers in Registry Notifications](invalid-key-object-pointers-in-registry-notifications.md)

[Filtering Registry Operations on Application Hives](filtering-registry-operations-on-application-hives.md)

 

