---
title: Bug Checks from KMDF Drivers
author: windows-driver-content
description: Bug Checks from KMDF Drivers
ms.assetid: 4fde9586-3455-4692-8eeb-bbf64c0a437e
keywords: ["debugging drivers WDK KMDF , bug checks", "bug check WDK KMDF", "verifying KMDF code", "KMDF bug checks WDK", "WDF_VIOLATION"]
---

# Bug Checks from KMDF Drivers


The framework checks for several types of errors from framework-based drivers. If one of these errors occurs, the framework creates a WDF\_VIOLATION bug check.

For information about the types of driver errors that the framework checks for, see [**WDF\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff557235).

Your driver can create a bug check by calling [**WdfVerifierKeBugCheck**](https://msdn.microsoft.com/library/windows/hardware/ff551166).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Bug%20Checks%20from%20KMDF%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




