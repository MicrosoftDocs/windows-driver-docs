---
title: Repudiation
author: windows-driver-content
description: Repudiation
ms.assetid: ccb50b6c-9e7d-4a90-a049-6c62b1b57376
keywords: ["threat models WDK file systems , repudiation", "security threat models WDK file systems , repudiation", "repudiation WDK file systems", "ownership WDK file systems", "denying performed operation WDK file systems"]
---

# Repudiation


## <span id="ddk_repudiation_if"></span><span id="DDK_REPUDIATION_IF"></span>


The concept of repudiation is that a user might perform a particular operation, and then subsequently deny having performed it. For most drivers this is an unusual type of issue. For a file system, however, logging is used to track operations (deletion of important files, for example) and ensure that there is a clear trail of operations. This provides a mechanism for ensuring against such repudiation.

Additionally, the operating system can assign ownership of objects to specific security identifiers. The ownership information cannot be changed without appropriate privileges (**SeTakeOwnershipPrivilege**) in order to ensure that ownership of specific objects can be tracked. Object ownership provides another form of protection against repudiation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Repudiation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


