---
title: Detecting Driver Load Errors
description: Detecting Driver Load Errors
ms.assetid: 1233aa87-067e-4f58-add5-3737f8ddd358
keywords: ["driver load errors WDK driver signing", "errors WDK driver signing", "detecting driver loaded", "load errors WDK driver signing", "status information WDK driver signing"]
---

# Detecting Driver Load Errors


To detect whether a driver loaded, check the status of the device in Device Manager. If the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) blocks a driver from loading because the driver is not correctly signed, the device status message will indicate that Windows could not load the driver and that the driver might be corrupted or missing. If this occurs, you can use [Code Integrity diagnostic system log events](code-integrity-diagnostic-system-log-events.md) to further diagnose the problem.

The following screen shot shows the type of device status message that indicates that Windows could not load a driver for a device and that the driver might be corrupted or missing.

![screen shot of an unsigned driver error message](images/signing-driver-load-error-message.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Detecting%20Driver%20Load%20Errors%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




