---
title: "!logexts.logd"
description: "The !logexts.logd extension disables logging."
keywords: ["!logexts.logd Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.logd
api_type:
- NA
---

# !logexts.logd

The **!logexts.logd** extension disables logging.

```dbgcmd
    !logexts.logd 
```

## DLL

Logexts.dll


## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

This will cause all API hooks to be removed in an effort to allow the program to run freely. COM hooks are not removed, because they cannot be re-enabled at will.

