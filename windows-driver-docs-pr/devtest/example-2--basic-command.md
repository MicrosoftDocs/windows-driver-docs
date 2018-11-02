---
title: Example 2 Basic Command
description: Example 2 Basic Command
ms.assetid: 5e66b7f4-5cf6-4bfc-b432-d531ac6ac53c
keywords:
- Tracefmt WDK , commands
- commands WDK Tracefmt
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 2: Basic Command


The syntax of the basic command used to start Tracefmt is as follows:

```
tracefmt EtlFile -p TMFPath -o OutputFile
```

For example,

```
tracefmt mytrace.etl -p c:\tracing -o mytrace.txt
```

This command uses the EtlFile parameter to specify the trace log file, mytrace.etl. It uses the **-p** parameter to indicate the directory in which the TMF file is stored, and the **-o** parameter to specify an alternate name for the output file.

In response, Tracefmt formats the trace messages in the mytrace.etl trace log file by using a TMF file in the c:\\tracing directory. It creates an output file named mytrace.txt and a summary file named mytrace.txt.sum.

 

 





