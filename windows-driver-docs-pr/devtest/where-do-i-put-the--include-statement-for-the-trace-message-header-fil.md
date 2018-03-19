---
title: Where do I put the #include statement for the trace message header file
description: Where do I put the #include statement for the trace message header file
ms.assetid: 5d8a2bb7-efe1-4cf2-9424-b63d4f17805e
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Where do I put the \#include statement for the trace message header file?


The **\#include** statement for the [trace message header file](trace-message-header-file.md) must appear in the source file after the definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro and before any WPP macro calls.

If you are using a project-wide header file, put the **\#include** statement for the trace message header file after the **\#include** statement for the project-wide header file.

 

 





