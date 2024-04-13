---
title: "!minipkd.help"
description: "The !minipkd.help extension displays help text for the Minipkd.dll extension commands."
keywords: ["minipkd.help Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- minipkd.help
api_type:
- NA
---

# !minipkd.help


The **!minipkd.help** extension displays help text for the Minipkd.dll extension commands.

```dbgcmd
!minipkd.help 
```

## DLL

Minipkd.dll

 
## Additional Information

For more information, see [SCSI Miniport Debugging](../debugger/scsi-miniport-debugging.md).

## Remarks

If an error message similar to the following appears, it indicates that the symbol path is incorrect and does not point to the correct version of the Scsiport.sys symbols.

```dbgcmd
minipkd error (0) <path> ... \minipkd\minipkd.c @ line 435
```

Use the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command to display the current path and change the path. Use the [**.reload (Reload Module)**](-reload--reload-module-.md) command to reload symbols from the current path.

