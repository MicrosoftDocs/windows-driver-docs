---
title: Retrieving Information from an INF File
description: Retrieving Information from an INF File
ms.assetid: 4174357f-bca3-43b8-8ad6-331b9accd905
keywords: ["INF files WDK device installations , retrieving information", "retrieving INF file information", "status information WDK INF files"]
---

# Retrieving Information from an INF File


## <a href="" id="ddk-retrieving-information-from-an-inf-file-dg"></a>


Once you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as [**SetupGetInfInformation**](https://msdn.microsoft.com/library/windows/desktop/aa377383), [**SetupQueryInfFileInformation**](https://msdn.microsoft.com/library/windows/desktop/aa377416), and [**SetupQueryInfVersionInformation**](https://msdn.microsoft.com/library/windows/desktop/aa377418) retrieve information about the specified INF file.

Other functions, such as [**SetupGetSourceInfo**](https://msdn.microsoft.com/library/windows/desktop/aa377392) and [**SetupGetTargetPath**](https://msdn.microsoft.com/library/windows/desktop/aa377394), obtain information about the source files and target directories.

Functions such as [**SetupGetLineText**](https://msdn.microsoft.com/library/windows/desktop/aa377388) and [**SetupGetStringField**](https://msdn.microsoft.com/library/windows/desktop/aa377393) enable you to directly access information that is stored in a line or field of an INF file. These functions are used internally by the higher-level [SetupAPI](setupapi.md) functions but are available if you have to directly access information at the line or field level.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Retrieving%20Information%20from%20an%20INF%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




