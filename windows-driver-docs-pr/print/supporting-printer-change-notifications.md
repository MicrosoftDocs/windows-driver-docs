---
title: Support printer change notifications
description: Provides information about how to support printer change notifications.
keywords:
- print providers WDK, printer change notifications
- network print providers WDK, printer change notifications
- notifications WDK printer
- printer change notifications WDK
- events WDK printer
- print queues WDK, printer change notifications
ms.date: 09/08/2022
---

# Support printer change notifications

Applications can request notification of the occurrences of print queue events by calling the spooler's [**FindFirstPrinterChangeNotification**](/windows/win32/printdocs/findfirstprinterchangenotification), [**FindNextPrinterChangeNotification**](/windows/win32/printdocs/findnextprinterchangenotification), and [**FindClosePrinterChangeNotification**](/windows/win32/printdocs/findcloseprinterchangenotification) functions. If you think application writers will want to request event notification for print queues supported by your partial print provider, you must support event notification in your provider as follows:

- Provide a [**FindFirstPrinterChangeNotification**](/windows-hardware/drivers/ddi/winspool/nf-winspool-findfirstprinterchangenotification) function.

  The spooler calls this function to supply the print provider with the following information:

  - A set of flags indicating the types of printer events for which the application has requested notification.
  
  - A handle to the print queue for which notifications are being requested.
  
  - A list of types of information the application has requested to be supplied when an event occurs.

    The function must return a flag value that indicates whether the provider should be polled to determine if changes have occurred. Non-polled providers send signals to the client whenever changes occur. A provider that must be polled does not send signals to a client when changes occur. Instead, the spooler signals the client at regular intervals, whether changes have occurred or not.

    At the provider level, this function has different arguments than at the Win32 level.

- Keep track of all print queue events that the application specified when it called **FindFirstPrinterChangeNotification**.

    For a list of the types of notifications an application can request, and for a list of the types of information that can be used to describe an event, see the Win32 **FindFirstPrinterChangeNotification** function. Types of events for which an application might request notification include adding or deleting a print job or form. Types of information an application might request include job or form parameters.

    Print providers that are not polled must call [**PartialReplyPrinterChangeNotification**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-partialreplyprinterchangenotification) or [**ReplyPrinterChangeNotification**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-replyprinterchangenotification) when changes occur, to supply the spooler with information describing the changes. The **ReplyPrinterChangeNotification** function must be called at some point because it causes the spooler to signal the application, while the **PartialReplyPrinterChangeNotification** function does not. When the application receives a signal from **ReplyPrinterChangeNotification**, it is supposed to call **FindNextPrinterChangeNotification**. This latter function supplies the application with the event information that the spooler previously received from the print provider.

    Print providers that are polled should simply keep track of changes. The spooler signals the application at regular intervals. When the application receives a signal, it is supposed to call the spooler's **FindNextPrinterChangeNotification** function. For polled providers, this function calls the provider's **RefreshPrinterChangeNotification** function.

- Provide a [**RefreshPrinterChangeNotification**](/previous-versions/ff561930(v=vs.85)) function.

    This function must return the current state of all monitored print queue options, for the specified print queue. The spooler calls this function when an application calls **FindNextPrinterChangeNotification** with the PRINTER_NOTIFY_OPTIONS_REFRESH flag set.

    Applications are supposed to set this flag if a previous call to **FindNextPrinterChangeNotification** returns a PRINTER_NOTIFY_INFO structure with the PRINTER_NOTIFY_INFO_DISCARDED flag set. Both polled and nonpolled providers must support **RefreshPrinterChangeNotification**.

- Provide a **FindClosePrinterChangeNotification** function.
