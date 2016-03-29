---
title: GetPrintCapabilities
description: The IPrintTicketProvider GetPrintCapabilities routine must return a valid PrintCapabilities document.
ms.assetid: 9c9bd387-5ea2-4758-a967-190a711cd8c3
keywords: ["GetPrintCapabilities"]
---

# GetPrintCapabilities


The [**IPrintTicketProvider::GetPrintCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554365) routine must return a valid PrintCapabilities document. For a basic implementation, the document can be very simple however the print driver cannot support any features in a Print Ticket that are not exposed in the PrintCapabilities document. As you add print ticket support to your print driver, you will need to return to this routine and add those features to the PrintCapabilities document.

The system does not provide any default PrintCapabilities document even for the features that the system provides through the DEVMODE-to-PrintTicket conversion. The print driver must create and return the corresponding PrintCapabilities document.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GetPrintCapabilities%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




