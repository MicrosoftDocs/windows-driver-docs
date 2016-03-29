---
title: Print Ticket Organization
description: Print Ticket Organization
ms.assetid: 3e30eb53-2f62-469d-a27c-dc256df37126
keywords: ["Print Tickets WDK , organization", "hierarchy WDK Print Ticket"]
---

# Print Ticket Organization


A PrintTicket document can contain commands that apply to different parts of a document. A Print Ticket document can contain one of the following content levels that are ranked according to their specificity:

-   The high-level job (job-level Print Ticket)

-   The documents in the job (document-level Print Ticket)

-   The pages in the document (page-level Print Ticket)

The job-level Print Ticket is the most general, followed by the document-level Print Ticket, and finally the page-level Print Ticket, which is the most specific. The elements of the Print Schema Framework that apply to these levels are prefixed with "Job", "Document", or "Page" accordingly. The Print Ticket hierarchy corresponds to the hierarchy of XPS Document parts.

The hierarchical nature of Print Tickets enables elements in lower-level Print Tickets to override corresponding elements of higher-level Print Tickets. Before you can use PrintTickets, they must be merged with the PrintTicket objects of higher levels in the document that apply to obtain the effective Print Ticket for a specific document part. This merge is performed before the effective Print Ticket is required for processing, such as in a print driver.

The following figure shows the relationships among the different levels of PrintTicket documents and how this merge is performed.

![print ticket hierarchy](images/ptpcmerge1.gif)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20Organization%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




