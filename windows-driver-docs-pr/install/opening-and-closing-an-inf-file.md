---
title: Opening and Closing an INF File
description: Opening and Closing an INF File
ms.assetid: da270688-4b8b-43b3-afdb-8f31d15ef50c
keywords:
- INF files WDK device installations , opening
- INF files WDK device installations , closing
- opening INF files
- closing INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening and Closing an INF File





Before a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) can access the information in an INF file, it must open the file by calling [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409). This function returns a handle to the INF file.

If you do not know the name of the INF file that you have to open, use [**SetupGetInfFileList**](https://msdn.microsoft.com/library/windows/desktop/aa377381) to obtain a list of all the INF files in a directory.

Once an application opens an INF file, it can append additional INF files to the opened file that uses [**SetupOpenAppendInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377407). When subsequent [SetupAPI](setupapi.md) functions reference an open INF file, they will also be able to access any information that is stored in any appended files.

If no INF file is specified when calling [**SetupOpenAppendInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377407), this function appends the file specified by the **LayoutFile** entry in the [**INF Version section**](inf-version-section.md) of the INF file opened during the call to [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409).

When the information in the INF file is no longer needed, the application should call [**SetupCloseInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa376985) to release resources allocated during the call to [**SetupOpenInfFile**](https://msdn.microsoft.com/library/windows/desktop/aa377409).

 

 





