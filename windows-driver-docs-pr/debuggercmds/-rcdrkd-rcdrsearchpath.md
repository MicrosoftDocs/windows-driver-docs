---
title: "!rcdrkd.rcdrsearchpath"
description: "The !rcdrkd.rcdrsearchpath extension sets the search path for trace message format (TMF) and trace message control (TMC) files."
keywords: ["!rcdrkd.rcdrsearchpath Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rcdrkd.rcdrsearchpath
api_type:
- NA
---

# !rcdrkd.rcdrsearchpath

The **!rcdrkd.rcdrsearchpath** extension sets the search path for trace message format (TMF) and trace message control (TMC) files.

```dbgcmd
!rcdrkd.rcdrsearchpath FilePath
```

## Parameters

<span id="_______FilePath______"></span><span id="_______filepath______"></span><span id="_______FILEPATH______"></span> *FilePath*   
Path to the format files.

## DLL

Rcdrkd.dll

## Remarks

The search path set by this command takes precedence over the search path specified in the TRACE\_FORMAT\_SEARCH\_PATH environment variable.

## See also

[RCDRKD Extensions](rcdrkd-extensions.md)

