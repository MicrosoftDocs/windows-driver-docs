---
title: WDK Build Output
description: By default, the WDK uses the intermediate directory $(IntDir) macro to specify the default build output directory.
ms.assetid: CD083755-9C9C-458A-9115-E63336C413B5
---

# WDK Build Output


By default, the WDK uses the intermediate directory **$(IntDir)** macro to specify the default build output directory.

The WDK defines the intermediate directory as **$(Platform)\\$(ConfigurationName)\\**. The **$(ConfigurationName)** macro includes the target version of Windows and the configuration type (Release or Debug), for example, x64\\Win8.1Release.

In this way, you can build different configurations side-by-side without losing the previous build for the other Windows target of the same binary. This approach is different than the intermediate directory that might be used if you were building a Windows Desktop application, which usually only includes the platform (x64, Win32) and the configuration type (Release, Debug) in the name.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WDK%20Build%20Output%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




