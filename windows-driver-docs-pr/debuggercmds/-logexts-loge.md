---
title: "!logexts.loge"
description: "The !logexts.loge extension enables logging. If logging has not been initialized, it will be initialized and enabled."
keywords: ["!logexts.loge Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.loge
api_type:
- NA
---

# !logexts.loge


The **!logexts.loge** extension enables logging. If logging has not been initialized, it will be initialized and enabled.

```dbgcmd
    !logexts.loge [OutputDirectory] 
```

## Parameters


<span id="_______OutputDirectory______"></span><span id="_______outputdirectory______"></span><span id="_______OUTPUTDIRECTORY______"></span> *OutputDirectory*   
Specifies the directory to use for output. If *OutputDirectory* is specified, it must exist -- the debugger will not create it. If a relative path is specified, it will be relative to the directory from which the debugger was started. If *OutputDirectory* is omitted, the path to the Desktop will be used. The debugger will create a LogExts subdirectory of *OutputDirectory*, and all Logger output will be placed in this subdirectory.

## DLL

Logexts.dll

 

## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

If Logger has not yet been injected into the target application by the [**!logexts.logi**](-logexts-logi.md) extension, the **!logexts.loge** extension will inject Logger into the target and then enable logging.

If [**!logexts.logi**](-logexts-logi.md) has already been run, you cannot include *OutputDirectory*, because the output directory will have already been set.

