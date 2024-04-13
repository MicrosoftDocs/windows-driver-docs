---
title: "!logexts.logo"
description: "The !logexts.logo extension sets or displays the Logger output options."
keywords: ["!logexts.logo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- logexts.logo
api_type:
- NA
---

# !logexts.logo


The **!logexts.logo** extension sets or displays the Logger output options.

```dbgcmd
!logexts.logo {e|d} {d|t|v} 
!logexts.logo 
```

## Parameters

<span id="_______e_d"></span><span id="_______E_D"></span> **e|d**  
Specifies whether to enable (e) or disable (d) the indicated output type.

<span id="_______d_t_v"></span><span id="_______D_T_V"></span> **d|t|v**  
Specifies the output type. Three types of Logger output are possible: messages sent directly to the debugger (d), a text file (t), or a verbose .lgv file (v).

## DLL

Logexts.dll

 

## Additional Information

For more information, see [Logger and LogViewer](../debugger/logger-and-logviewer.md).

## Remarks

If **!logexts.logo** is used without any parameters, then the current logging status, the output directory, and the current settings for the debugger, text file, and verbose log are displayed:

```dbgcmd
0:000> !logo
Logging currently enabled.

Output directory: MyLogs\LogExts\

Output settings:
  Debugger            Disabled
  Text file           Enabled
  Verbose log         Enabled
```

In the previous example, the output directory is a relative path, so it is located relative to the directory in which the debuggers were started.

To disable verbose logging, you would use the following command:

```dbgcmd
0:000> !logo d v
  Debugger            Disabled
  Text file           Enabled
  Verbose log         Disabled
```

Text file and .lgv files will be placed in the current output directory. To read an .lgv file, use LogViewer.

