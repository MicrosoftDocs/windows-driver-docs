---
title: Language Monitors
description: Language Monitors
keywords:
- print monitors WDK , language monitors
- language monitors WDK print
- language monitors WDK print , about language monitors
ms.date: 06/17/2020
---

# Language Monitors

Language monitors are user-mode DLLs that serve two purposes:

- They provide a full duplex communications path between the print spooler and bidirectional printers that are capable of providing software-accessible status information.

- They add printer control information, such as commands defined by a printer job language, to the data stream.

Microsoft provides a language monitor, Pjlmon.dll, which supports *printer job language (PJL)*, and provides bidirectional communication for PJL printers. For more information see, [Sample language monitor](sample-language-monitor.md).

Customized language monitors can be written to support other job control languages, for unidirectional or bidirectional printers.

Language monitors are optional and only associated with a particular printer type if included in the printer's INF file, as described in [Installing a Print Monitor](installing-a-print-monitor.md).

If you clear **Enable bidirectional support** check box in the **Ports** tab of the printer properties dialog box, the spooler will not call the [**StartDocPort**](/previous-versions/ff562710(v=vs.85)), [**WritePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-writeport), [**EndDocPort**](/previous-versions/ff548742(v=vs.85)), [**GetPrinterDataFromPort**](/previous-versions/ff550506(v=vs.85)), [**ReadPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-readport) functions of the language monitor. The spooler will continue to call the [**OpenPortEx**](/previous-versions/ff559596(v=vs.85)), [**ClosePort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-closeport), [**SendRecvBidiDataFromPort**](/previous-versions/ff562071(v=vs.85)) functions even when **Enable bidirectional support** is cleared. The **Enable bidirectional support** check box does not affect the calls to the language monitor that are made when an application calls functions in the bidirectional communication API.

If a language monitor is associated with a printer, the language monitor receives the printer's data stream from the print processor, modifies it, and passes it to the printer's port monitor. For more information, see [Language and Port Monitor Interaction](language-and-port-monitor-interaction.md).

> [!NOTE]
> Language monitors should always implement the **SendRecvBidiDataFromPort** function and include the function's address in the *pfnSendRecvBidiDataFromPort* member of the [**MONITOR2**](/windows-hardware/drivers/ddi/winsplp/ns-winsplp-_monitor2) structure.

In the event that the language monitor does not support Bidi, or the request contains Bidi Schema values that the Language Monitor does not support, the Language Monitor should forward the calls to the Port Monitor's **SendRecvBidiDataFromPort** function.
