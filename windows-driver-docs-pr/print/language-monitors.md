---
title: Language Monitors
author: windows-driver-content
description: Language Monitors
ms.assetid: 26ba1c22-390a-4187-b67a-3f3497964f8e
keywords: ["print monitors WDK , language monitors", "language monitors WDK print", "language monitors WDK print , about language monitors"]
---

# Language Monitors


## <a href="" id="ddk-language-monitors-gg"></a>


Language monitors are user-mode DLLs that serve two purposes:

-   They provide a full duplex communications path between the print spooler and bidirectional printers that are capable of providing software-accessible status information.

-   They add printer control information, such as commands defined by a printer job language, to the data stream.

Microsoft provides a language monitor, Pjlmon.dll, which supports [*printer job language (PJL)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-printer-job-language--pjl-), and provides bidirectional communication for PJL printers. This monitor is included in the Microsoft Windows Driver Kit (WDK) as the [sample language monitor](sample-language-monitor.md).

Customized language monitors can be written to support other job control languages, for unidirectional or bidirectional printers.

Language monitors are optional and only associated with a particular printer type if included in the printer's INF file, as described in [Installing a Print Monitor](installing-a-print-monitor.md).

If you clear **Enable bidirectional support** check box in the **Ports** tab of the printer properties dialog box, the spooler will not call the [**StartDocPort**](https://msdn.microsoft.com/library/windows/hardware/ff562710), [**WritePort**](https://msdn.microsoft.com/library/windows/hardware/ff563792), [**EndDocPort**](https://msdn.microsoft.com/library/windows/hardware/ff548742), [**GetPrinterDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff550506), [**ReadPort**](https://msdn.microsoft.com/library/windows/hardware/ff561909) functions of the language monitor. The spooler will continue to call the [**OpenPortEx**](https://msdn.microsoft.com/library/windows/hardware/ff559596), [**ClosePort**](https://msdn.microsoft.com/library/windows/hardware/ff545975), [**SendRecvBidiDataFromPort**](https://msdn.microsoft.com/library/windows/hardware/ff562071) functions even when **Enable bidirectional support** is cleared. The **Enable bidirectional support** check box does not affect the calls to the language monitor that are made when an application calls functions in the bidirectional communication API.

If a language monitor is associated with a printer, the language monitor receives the printer's data stream from the print processor, modifies it, and passes it to the printer's port monitor. For more information, see [Language and Port Monitor Interaction](language-and-port-monitor-interaction.md).

**Note**  
Language monitors should always implement the **SendRecvBidiDataFromPort** function and include the function's address in the *pfnSendRecvBidiDataFromPort* member of the [**MONITOR2**](https://msdn.microsoft.com/library/windows/hardware/ff557532) structure.

In the event that the language monitor does not support Bidi, or the request contains Bidi Schema values that the Language Monitor does not support, the Language Monitor should forward the calls to the Port Monitor's **SendRecvBidiDataFromPort** function.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Language%20Monitors%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


