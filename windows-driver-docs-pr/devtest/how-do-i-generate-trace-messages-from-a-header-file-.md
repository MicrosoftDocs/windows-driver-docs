---
title: How do I generate trace messages from a header file
description: How do I generate trace messages from a header file
ms.assetid: 00b97f26-90e2-4efe-8bba-e3ffe7ba90ea
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I generate trace messages from a header file?


To generate trace messages from source files with file name extensions other than .c, .c++, .cpp, and .cxx, add the **-ext** parameter to the RUN\_WPP macro that invokes the Windows software trace preprocessor.

For example, to generate traces from .c and .h files, use the following statement:

```
RUN_WPP=$(SOURCES) -km -ext:.c.h
```
Be sure that the .h files that tracewpp needs to scan are included in `$(SOURCES)`, or add them on the command line.  
For example:

```
RUN_WPP=$(SOURCES) tracedrv.h -km -ext:.c.h
```
Do *not* include the .h file that is specified with the -scan: option as a configuration data file, such as `trace.h`.

The **-ext** parameter specifies the file types that WPP recognizes as source files. WPP ignores files with a different file name extension. By default, WPP recognizes only .c, .c++, .cpp, and .cxx files.

In versions of Windows prior to Windows Vista because the values of this parameter are case-sensitive, you must list all cases. For example:

```
RUN_WPP=$(SOURCES) -km -ext:.c.C.h.H
```

Also, if the header file has the same name as another source file, add the **-preserveext** parameter to the RUN\_WPP macro. For example:

```
RUN_WPP=$(SOURCES) -km -ext:.c.C.h.H  -preserveext:.c.h
```

The **-preserveext** parameter preserves the specified file name extensions when creating the names of [trace message header](trace-message-header-file.md) (.tmh) files. This parameter prevents WPP from creating multiple TMH files with the same name. By default, WPP uses only the .tmh file name extension, such as tracedrv.tmh. With the **-preserveext** parameter, the files are instead named tracedrv.c.tmh and tracedrv.h.tmh.

For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).

 

 





