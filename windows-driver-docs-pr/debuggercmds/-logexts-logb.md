---
title: "!logexts.logb"
description: "The !logexts.logb extension displays or flushes the output buffer."
keywords: ["!logexts.logb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.logb
api_type:
- NA
---

# !logexts.logb


The **!logexts.logb** extension displays or flushes the output buffer.

```dbgcmd
!logexts.logb p 
!logexts.logb f 
```

## Parameters

<span id="_______p______"></span><span id="_______P______"></span> **p**   
Causes the contents of the output buffer to be displayed in the debugger.

<span id="_______f"></span><span id="_______F"></span> **f**  
Flushes the output buffer to the disk.

## DLL

Logexts.dll

## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

As a performance consideration, log output is flushed to disk only when the output buffer is full. By default, the buffer is 2144 bytes.

The **!logexts.logb p** extension displays the contents of the buffer in the debugger.

The **!logexts.logb f** extension flushes the buffer to the log files. Because the buffer memory is managed by the target application, the automatic writing of the buffer to disk will not occur if there is an access violation or some other nonrecoverable error in the target application. In such cases, you should use this command to manually flush the buffer to the disk. Otherwise, the most recently-logged APIs might not appear in the log files.

