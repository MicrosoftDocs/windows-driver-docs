---
title: Opening and Closing an INF File
description: Opening and Closing an INF File
ms.assetid: da270688-4b8b-43b3-afdb-8f31d15ef50c
keywords: ["INF files WDK device installations , opening", "INF files WDK device installations , closing", "opening INF files", "closing INF files"]
---

# Opening and Closing an INF File


## <a href="" id="ddk-opening-and-closing-an-inf-file-dg"></a>


Before a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) can access the information in an INF file, it must open the file by calling [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409). This function returns a handle to the INF file.

If you do not know the name of the INF file that you have to open, use [**SetupGetInfFileList**](https://msdn.microsoft.com/library/windows/desktop/aa377381) to obtain a list of all the INF files in a directory.

Once an application opens an INF file, it can append additional INF files to the opened file that uses [**SetupOpenAppendInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377407). When subsequent [SetupAPI](setupapi.md) functions reference an open INF file, they will also be able to access any information that is stored in any appended files.

If no INF file is specified when calling [**SetupOpenAppendInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377407), this function appends the file specified by the **LayoutFile** entry in the [**INF Version section**](inf-version-section.md) of the INF file opened during the call to [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409).

When the information in the INF file is no longer needed, the application should call [**SetupCloseInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa376985) to release resources allocated during the call to [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Opening%20and%20Closing%20an%20INF%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




