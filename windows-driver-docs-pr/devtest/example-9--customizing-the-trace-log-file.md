---
title: Example 9 Customizing the Trace Log File
description: Example 9 Customizing the Trace Log File
ms.assetid: b65b4d15-f058-425a-b2b2-b040265d48ac
keywords: ["trace logs WDK", "logs WDK tracing", "custom trace logs WDK", "event trace logs WDK"]
---

# Example 9: Customizing the Trace Log File


## <span id="ddk_customizing_the_trace_log_file_tools"></span><span id="DDK_CUSTOMIZING_THE_TRACE_LOG_FILE_TOOLS"></span>


The commands in this example demonstrate different methods for customizing the event trace log file that Tracelog produces.

**Circular file.** The following command starts a trace log session with a circular log file. It uses the **-cir** parameter to specify a circular log file with a maximum size of 2 MB.

If you omit the maximum file size value (in this case, **2**), Tracelog ignores the parameter and starts a session with a sequential trace log file.

```
tracelog -start MyTrace -guid MyProvider.guid -f testtrace.etl -cir 2
```

**Preallocated file.** The following command starts a trace log session with a preallocated file. In this case, the file was preallocated to make sure that its large size could be accommodated before the trace session started.

This command uses the **-seq** parameter to specify a sequential event trace log file with a maximum file size of 128 MB and it uses the **-prealloc** parameter to request a preallocated file. Sequential files are the default, but the **-seq** parameter was used to specify a maximum file size, which is required for preallocated files. The **-cir** parameter can also be used to specify a maximum files size for **-prealloc**, if circular files are preferred.

```
tracelog -start MyTrace -guid MyProvider.guid -f testtrace.etl -seq 128 -prealloc
```

**Multiple files.** The following command starts a trace log session that generates a series of smaller, sequential event trace log files, instead of one large file.

The command uses the **-newfile** parameter with a maximum file size value of 1 to start a new trace log file whenever the current log file reaches 1 MB. Also, the file name specified by the **-f** parameter includes the characters **%d**, as is required when using **-newfile**. The system substitutes a file counter value for **%d** when it creates each file.

```
tracelog -start MyTrace −guid MyProvider.guid -f testtrace%d.etl -newfile 1
```

The resulting 1 MB files are numbered in the order that they are created, for example testtrace1.etl.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%209:%20Customizing%20the%20Trace%20Log%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




