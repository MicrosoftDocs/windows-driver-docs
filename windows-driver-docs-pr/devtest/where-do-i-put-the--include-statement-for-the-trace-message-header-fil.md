---
title: Where do I Put the Include Statement for the Trace Message Header File
description: Where do I put the include statement for the trace message header file
ms.date: 04/20/2017
---

# Where do I put the \#include statement for the trace message header file?


The **\#include** statement for the [trace message header file](trace-message-header-file.md) must appear in the source file after the definition of the [WPP\_CONTROL\_GUIDS](/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro and before any WPP macro calls.

If you are using a project-wide header file, put the **\#include** statement for the trace message header file after the **\#include** statement for the project-wide header file.

 

