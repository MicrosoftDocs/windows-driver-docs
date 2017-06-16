---
title: Obtaining Additional Registry Information
author: windows-driver-content
description: Obtaining Additional Registry Information
ms.assetid: 989acf63-3bb1-4d9a-a7a8-3eea1e2bc68a
keywords: ["filtering registry calls WDK kernel , additional information to obtain", "registry filtering drivers WDK kernel , additional information to obtain"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Obtaining Additional Registry Information


Registry filtering drivers that run on Windows Vista and later operating system versions can obtain the following additional information about registry operations:

-   Object identifiers and names

    The [**CmCallbackGetKeyObjectIDEx**](https://msdn.microsoft.com/library/windows/hardware/jj215789) routine retrieves the registry key identifier and object name that are associated with a specified registry key object.

-   Transaction objects

    The [**CmGetBoundTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff541905) routine returns a pointer to the transaction object that represents the [transaction](using-kernel-transaction-manager.md), if any, that is associated with a registry key object.

-   Version information

    The [**CmGetCallbackVersion**](https://msdn.microsoft.com/library/windows/hardware/ff541912) routine retrieves the major and minor version numbers for the current version of the configuration manager's registry callback feature.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Obtaining%20Additional%20Registry%20Information%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


