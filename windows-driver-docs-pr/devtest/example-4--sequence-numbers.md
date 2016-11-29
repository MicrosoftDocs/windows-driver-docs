---
title: Example 4 Sequence Numbers
description: Example 4 Sequence Numbers
ms.assetid: 5b498267-c495-4a25-abb9-aa83a51559e1
keywords: ["Tracefmt WDK , sequence numbers", "sequence numbers WDK Tracefmt"]
---

# Example 4: Sequence Numbers


The following command includes the local or global sequence number of the message in the output file. If sequence numbers were not generated, the sequence field contains zeros.

```
tracefmt mytrace.etl -p c:\tracing -o mytrace.txt -seq
```

This command formats messages from the mytrace.etl log file by using a TMF file in the c:\\tracing directory. It writes the formatted messages to the mytrace.txt file. The command uses the **-seq** parameter to direct Tracefmt to include sequence numbers in the output file.

An excerpt of the output file appears as follows:

```
[0]0AF4.0C64::07/25/2003-13:55:39.998 00004ea4 [tracedrv]IOCTL = 1
[0]0AF4.0C64::07/25/2003-13:55:39.998 000047d0 [tracedrv]Hello, 1 Hi
[0]0AF4.0C64::07/25/2003-13:55:39.998 63966c89 [tracedrv]Hello, 2 Hi
...
```

**Note**   If you view a trace message file on a computer running Windows XP, the display might show trace messages that are out of sequence trace messages. To correct this problem, you can use the sequence number option when you start the trace session and view the trace using Tracefmt. You can then view the trace with Traceview and sort according to sequence number. You can also view the trace on a computer running Windows Server 2003 or later versions of Windows.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%204:%20Sequence%20Numbers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




