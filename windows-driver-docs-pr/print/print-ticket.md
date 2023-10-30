---
title: Print Ticket
description: Print Ticket
keywords:
- PrintTicket documents WDK
- Print Tickets WDK , PrintTicket documents
- document descriptions WDK print
- print jobs WDK , Print Tickets
- jobs WDK print , Print Tickets
ms.date: 01/30/2023
---

# Print Ticket

[!include[Print Support Apps](../includes/print-support-apps.md)]

A PrintTicket document is an XML document that describes how a document or document part is to be printed. A PrintTicket document can be associated with a print job, a document, or a page within a document. The PrintTicket document can be added to an XPS Document as a PrintTicket part and saved with document contents in a file. A PrintTicket document can also be added to a document as the application spools the document for printing.

Conversion functions enable you to Print Tickets use in Microsoft Win32 applications. Functions are available to convert Print Tickets to [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structures and DEVMODEW structures back to Print Tickets.

This section contains the following topics:

[Print Ticket Organization](print-ticket-organization.md)

[Print Ticket Compatibility with Win 32 Applications](print-ticket-compatibility-with-win-32-applications.md)

[Print Ticket Processing in the Print Driver](print-ticket-processing-in-the-print-driver.md)

[Print Ticket Support in Unidrv and PScript5 Print Drivers](print-ticket-support-in-unidrv-and-pscript5-print-drivers.md)
