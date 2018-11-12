---
title: dml_proc
description: The dml_proc extension displays a list of processes and provides links for obtaining more detailed information about processes.
ms.assetid: 35B5B2E7-07CE-4F44-819D-9B7C76273F9A
keywords: ["dml_proc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dml_proc
api_type:
- NA
ms.localizationpriority: medium
---

# !dml\_proc


The **!dml\_proc** extension displays a list of processes and provides links for obtaining more detailed information about processes.

```dbgcmd
!dml_proc
```

Remarks
-------

The following image shows a portion of the output displayed by **!dml\_proc**.

![screen shot of !dml\-proc output](images/dmlproc01.png)

In the preceding output, the process addresses are links that you can click to see more detailed information. For example, if you click **fffffa80\`04e2b700** (the address for mobsync.exe), you will see detailed information about the mobsync.exe process as shown in the following image.

![screen shot of process details](images/dmlproc02.png)

The preceding output, which describes an individual process, contains links that you can click to explore the process and its threads in more detail.

## <span id="see_also"></span>See also


[Debugger Markup Language Commands](debugger-markup-language-commands.md)

 

 






