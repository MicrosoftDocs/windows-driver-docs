---
title: Print Ticket Merging
author: windows-driver-content
description: Print Ticket Merging
ms.assetid: 2d9cf4d3-5c73-4355-b5e0-effcfb7102cc
keywords: ["XPSDrv printer drivers WDK , render modules", "render modules WDK XPSDrv , Print Tickets", "Print Tickets WDK , XPSDrv printer drivers", "merging Print Ticket objects"]
---

# Print Ticket Merging


The PrintTicket objects processed in the Print Driver have a hierarchical relationship based on the document part they are associated with. The following diagram illustrates the relationship of these parts within an XPS Document.

![diagram illustrating document parts in an xps document](images/ptpcxps1.gif)

Each of the Print Ticket levels in the hierarchy has a different scope. The print driver filter modules that use the Print Ticket information must maintain that scope as the Print Ticket objects are read from the document stream. The following diagram illustrates how this can be done in a print driver filter module.

![diagram illustrating how the different print ticket levels are logically merged ](images/ptpcxps2.gif)

As the document parts are read by the filter, the Print Ticket objects are read, merged and validated and cached by the filter for configuring how the filter will process each document part. The previous diagram illustrates how the different Print Ticket levels are logically merged and the pseudo code below illustrates how this merge might be implemented.

```
class Filter
{
 PrintTicket Saved_FDS_PT;
 PrintTicket Saved_FD_PT;

 ProcessFDS(pIFixedDocumentSequence)
    {
 Saved_FDS_PT = pIFixedDocumentSequence->GetPrintTicket();

        // continue processing the FixedDocumentSequence part
    }

 ProcessFD(pIFixedDocument)
    {
 Saved_FD_PT->Release();

        temp = pIFixedDocument->GetPrintTicket();

 Saved_FD_PT = PrintTicketMergeAndValidate(
 Saved_FDS_PT, temp);

        // continue processing the FixedDocument part
    }

 ProcessPage(IFixedPage)
    {
        temp = pIFixedPage->GetPrintTicket();

 PagePT = PrintTicketMergeAndValidate(Saved_FD_PT, temp);

        // continue processing the FixedPage part
    }

 PrintTicket PrintTicketMergeAndValidate(
 ParentPT,
 PartPT)
    {
        // Entries in the Part PrintTicket 
        // take precedence over the corresponding entries 
        // in the Parent PrintTicket
    }
};
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20Merging%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


