---
title: "!logexts.logi"
description: "The !logexts.logi extension initializes logging by injecting Logger into the target application."
keywords: ["!logexts.logi Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.logi
api_type:
- NA
---

# !logexts.logi


The **!logexts.logi** extension initializes logging by injecting Logger into the target application.

```dbgcmd
    !logexts.logi [OutputDirectory] 
```

## Parameters

<span id="_______OutputDirectory______"></span><span id="_______outputdirectory______"></span><span id="_______OUTPUTDIRECTORY______"></span> *OutputDirectory*   
Specifies the directory to use for output. If *OutputDirectory* is specified, it must exist -- the debugger will not create it. If a relative path is specified, it will be relative to the directory from which the debugger was started. If *OutputDirectory* is omitted, the path to the Desktop will be used. The debugger will create a LogExts subdirectory of *OutputDirectory*, and all Logger output will be placed in this subdirectory.

## DLL

Logexts.dll

 

## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

This command initializes logging, but does not actually enable it. Logging can be enabled with the [**!logexts.loge**](-logexts-loge.md) command.

