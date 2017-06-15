---
title: Filtering Registry Calls
author: windows-driver-content
description: Filtering Registry Calls
MS-HAID:
- 'Other\_c567470e-ac06-4a6a-9482-abeb071dddba.xml'
- 'kernel.filtering\_registry\_calls'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6b35c3a0-4ece-4101-b348-e71f5cccf0c8
keywords: ["filtering registry calls WDK kernel", "registry filtering drivers WDK kernel", "RegistryCallback", "filtering registry calls WDK kernel , about filtering registry calls", "registry filtering drivers WDK kernel , about filtering registry calls"]
---

# Filtering Registry Calls


A *registry filtering driver* is any kernel-mode driver that filters registry calls, such as the driver component of an antivirus software package. The configuration manager, which implements the registry, allows registry filtering drivers to filter any thread's calls to registry functions. Filtering of registry calls was first supported in Microsoft Windows XP.

On Windows XP, a registry filtering driver can call [**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918) to register a [*RegistryCallback*](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine and [**CmUnRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541928) to unregister the callback routine. The *RegistryCallback* routine receives notifications of each registry operation before the configuration manager processes the operation. A set of **REG\_*XXX*\_KEY\_INFORMATION** data structures contain information about each registry operation. The *RegistryCallback* routine can block a registry operation. The callback routine also receives notifications when the configuration manager has finished creating or opening a registry key.

Windows Server 2003 provides additional completion notifications.

Windows Vista provides the following additional registry filtering capabilities:

-   Registry filtering drivers can be layered in a driver stack, and each driver in the stack can filter a registry operation.

-   The **CmRegisterCallback** routine is replaced by the [**CmRegisterCallbackEx**](https://msdn.microsoft.com/library/windows/hardware/ff541921) routine.

-   Drivers can completely process a registry operation (or redirect the requested operation to a different operation) and prevent the configuration manager from handling the operation.

-   Drivers can assign context information to individual registry operations or key objects.

-   Drivers can modify a registry operation's output parameters and return value.

-   Additional members have been added to all **REG\_*XXX*\_KEY\_INFORMATION** data structures.

-   Drivers receive notifications of additional registry operations.

For a list of the registry operations that a driver can filter on each version of Windows, see [**REG\_NOTIFY\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560950).

To learn more about filtering registry calls, see the following topics:

[Registering for Notifications](registering-for-notifications.md)

[Handling Notifications](handling-notifications.md)

[Supporting Layered Registry Filtering Drivers](supporting-layered-registry-filtering-drivers.md)

[Specifying Context Information](specifying-context-information.md)

[Obtaining Additional Registry Information](obtaining-additional-registry-information.md)

[Invalid Key Object Pointers in Registry Notifications](invalid-key-object-pointers-in-registry-notifications.md)

[Filtering Registry Operations on Application Hives](filtering-registry-operations-on-application-hives.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Filtering%20Registry%20Calls%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


