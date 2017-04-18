---
title: C28175
description: Warning C28175 The member of struct should not be accessed by a driver.
ms.assetid: 259a90d7-29ef-4a27-a921-8fff93b325bd
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28175


warning C28175: The member of struct should not be accessed by a driver

This warning indicates that a driver accessed an undocumented structure member that drivers should never access.

Drivers should never access the specified undocumented structure member. For most undocumented members of opaque or partially opaque structures, this prohibition is absolute. However, drivers may access certain undocumented structure members from within particular routines. For example, the driver may access the undocumented members of the partially opaque [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure only within a DRIVER\_INITIALIZE or DRIVER\_UNLOAD routine.

Sometimes the reason that this rule applies to a particular member is not immediately obvious. For example, one instance where this occurs is with the **NextDevice** member of **\_DEVICE\_OBJECT**. In this instance, a lock should be used to safely access this linked list, but that lock is not available to the driver. In this case, violating this rule causes infrequent but hard-to-diagnose failures. The proper way to access the related devices is to use the [**IoEnumerateDeviceObjectList**](https://msdn.microsoft.com/library/windows/hardware/ff548342) function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28175%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




