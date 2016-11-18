---
title: Example 2 Basic Command
description: Example 2 Basic Command
ms.assetid: 5e66b7f4-5cf6-4bfc-b432-d531ac6ac53c
keywords: ["Tracefmt WDK , commands", "commands WDK Tracefmt"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%202:%20Basic%20Command%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




