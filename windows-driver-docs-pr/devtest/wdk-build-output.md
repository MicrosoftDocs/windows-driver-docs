---
title: WDK Build Output
description: By default, the WDK uses the intermediate directory $(IntDir) macro to specify the default build output directory.
ms.assetid: CD083755-9C9C-458A-9115-E63336C413B5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDK Build Output


By default, the WDK uses the intermediate directory **$(IntDir)** macro to specify the default build output directory.

The WDK defines the intermediate directory as **$(Platform)\\$(ConfigurationName)\\**. The **$(ConfigurationName)** macro includes the target version of Windows and the configuration type (Release or Debug), for example, x64\\Win8.1Release.

In this way, you can build different configurations side-by-side without losing the previous build for the other Windows target of the same binary. This approach is different than the intermediate directory that might be used if you were building a Windows Desktop application, which usually only includes the platform (x64, Win32) and the configuration type (Release, Debug) in the name.

 

 





