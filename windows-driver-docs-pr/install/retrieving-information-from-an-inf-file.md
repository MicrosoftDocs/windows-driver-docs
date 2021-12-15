---
title: Retrieving Information from an INF File
description: Retrieving Information from an INF File
keywords:
- INF files WDK device installations , retrieving information
- retrieving INF file information
- status information WDK INF files
ms.date: 04/20/2017
---

# Retrieving Information from an INF File





Once you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as [**SetupGetInfInformation**](/windows/win32/api/setupapi/nf-setupapi-setupgetinfinformationa), [**SetupQueryInfFileInformation**](/windows/win32/api/setupapi/nf-setupapi-setupqueryinffileinformationa), and [**SetupQueryInfVersionInformation**](/windows/win32/api/setupapi/nf-setupapi-setupqueryinfversioninformationa) retrieve information about the specified INF file.

Other functions, such as [**SetupGetSourceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupgetsourceinfoa) and [**SetupGetTargetPath**](/windows/win32/api/setupapi/nf-setupapi-setupgettargetpatha), obtain information about the source files and target directories.

Functions such as [**SetupGetLineText**](/windows/win32/api/setupapi/nf-setupapi-setupgetlinetexta) and [**SetupGetStringField**](/windows/win32/api/setupapi/nf-setupapi-setupgetstringfielda) enable you to directly access information that is stored in a line or field of an INF file. These functions are used internally by the higher-level [SetupAPI](setupapi.md) functions but are available if you have to directly access information at the line or field level.

 

