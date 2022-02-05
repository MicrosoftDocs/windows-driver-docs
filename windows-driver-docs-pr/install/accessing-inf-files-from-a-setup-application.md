---
title: Accessing INF Files from a Device Installation Application
description: Accessing INF Files from a Device Installation Application
keywords:
- INF files WDK device installations , device installation application operations
ms.date: 02/02/2022
---

# Accessing INF Files from a Device Installation Application

Most INF files are used by system class installers and other *device installation applications*. This section describes common operations that vendor-supplied device installation applications can perform on INF files by using the [general Setup functions](/previous-versions/ff544985(v=vs.85)). For complete information about how to use these functions, see the Windows SDK documentation.

## Opening and Closing an INF File

Before a *device installation application* can access the information in an INF file, it must open the file by calling [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea). This function returns a handle to the INF file.

If you do not know the name of the INF file that you have to open, use [**SetupGetInfFileList**](/windows/win32/api/setupapi/nf-setupapi-setupgetinffilelista) to obtain a list of all the INF files in a directory.

Once an application opens an INF file, it can append additional INF files to the opened file that uses [**SetupOpenAppendInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopenappendinffilea). When subsequent [SetupAPI](setupapi.md) functions reference an open INF file, they will also be able to access any information that is stored in any appended files.

If no INF file is specified when calling [**SetupOpenAppendInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopenappendinffilea), this function appends the file specified by the **LayoutFile** entry in the [**INF Version section**](inf-version-section.md) of the INF file opened during the call to [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea).

When the information in the INF file is no longer needed, the application should call [**SetupCloseInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupcloseinffile) to release resources allocated during the call to [**SetupOpenInfFile**](/windows/win32/api/setupapi/nf-setupapi-setupopeninffilea).

## Retrieving Information from an INF File

Once you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as [**SetupGetInfInformation**](/windows/win32/api/setupapi/nf-setupapi-setupgetinfinformationa), [**SetupQueryInfFileInformation**](/windows/win32/api/setupapi/nf-setupapi-setupqueryinffileinformationa), and [**SetupQueryInfVersionInformation**](/windows/win32/api/setupapi/nf-setupapi-setupqueryinfversioninformationa) retrieve information about the specified INF file.

Other functions, such as [**SetupGetSourceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupgetsourceinfoa) and [**SetupGetTargetPath**](/windows/win32/api/setupapi/nf-setupapi-setupgettargetpatha), obtain information about the source files and target directories.

Functions such as [**SetupGetLineText**](/windows/win32/api/setupapi/nf-setupapi-setupgetlinetexta) and [**SetupGetStringField**](/windows/win32/api/setupapi/nf-setupapi-setupgetstringfielda) enable you to directly access information that is stored in a line or field of an INF file. These functions are used internally by the higher-level [SetupAPI](setupapi.md) functions but are available if you have to directly access information at the line or field level.