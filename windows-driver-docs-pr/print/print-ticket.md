---
title: Print Ticket
author: windows-driver-content
description: Print Ticket
MS-HAID:
- 'drvarch\_2b614815-7693-445c-8aeb-9c9243c12524.xml'
- 'print.print\_ticket'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dd18d0ef-c1f7-4a35-a420-2da102fb07f4
keywords: ["PrintTicket documents WDK", "Print Tickets WDK , PrintTicket documents", "document descriptions WDK print", "print jobs WDK , Print Tickets", "jobs WDK print , Print Tickets"]
---

# Print Ticket


A PrintTicket document is an XML document that describes how a document or document part is to be printed. A PrintTicket document can be associated with a print job, a document, or a page within a document. The PrintTicket document can be added to an XPS Document as a PrintTicket part and saved with document contents in a file. A PrintTicket document can also be added to a document as the application spools the document for printing.

Conversion functions enable you to Print Tickets use in Microsoft Win32 applications. Functions are available to convert Print Tickets to [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structures and DEVMODEW structures back to Print Tickets.

This section contains the following topics:

[Print Ticket Organization](print-ticket-organization.md)

[Print Ticket Compatibility with Win 32 Applications](print-ticket-compatibility-with-win-32-applications.md)

[Print Ticket Processing in the Print Driver](print-ticket-processing-in-the-print-driver.md)

[Print Ticket Support in Unidrv and PScript5 Print Drivers](print-ticket-support-in-unidrv-and-pscript5-print-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


