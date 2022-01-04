---
title: Opening and Closing an INF File
description: Opening and Closing an INF File
keywords:
- INF files WDK device installations , opening
- INF files WDK device installations , closing
- opening INF files
- closing INF files
ms.date: 04/20/2017
---

# Opening and Closing an INF File





Before a *device installation application* can access the information in an INF file, it must open the file by calling [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea). This function returns a handle to the INF file.

If you do not know the name of the INF file that you have to open, use [**SetupGetInfFileList**](/windows/win32/api/setupapi/nf-setupapi-setupgetinffilelista) to obtain a list of all the INF files in a directory.

Once an application opens an INF file, it can append additional INF files to the opened file that uses [**SetupOpenAppendInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopenappendinffilea). When subsequent [SetupAPI](setupapi.md) functions reference an open INF file, they will also be able to access any information that is stored in any appended files.

If no INF file is specified when calling [**SetupOpenAppendInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopenappendinffilea), this function appends the file specified by the **LayoutFile** entry in the [**INF Version section**](inf-version-section.md) of the INF file opened during the call to [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea).

When the information in the INF file is no longer needed, the application should call [**SetupCloseInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupcloseinffile) to release resources allocated during the call to [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea).

 

