---
title: Print Driver Plug-in Support
author: windows-driver-content
description: Print Driver Plug-in Support
MS-HAID:
- 'drvarch\_13be4750-d40f-455e-97e2-8c49d239f688.xml'
- 'print.print\_driver\_plug\_in\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fa072fc9-66da-46c2-a270-6f604860aaff
keywords: ["Print Capabilities WDK , plug-ins", "IPrintOemPrintTicketProvider"]
---

# Print Driver Plug-in Support


Print driver plug-ins that provide additional or modified functionality to minidriver-based print drivers must support the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174) to provide complete and correct Print Capabilities support in a Unidrv or PScript5-based print driver. If a plug-in supports **IPrintOemPrintTicketProvider**, the plug-in will gain the ability to edit the PrintTicket document and modify the configuration user interface (UI). But support for this interface also requires considerably more development effort than just editing a GPD or PPD file.

Plug-ins that do not support the **IPrintOemPrintTicketProvider** interface are limited to their existing [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) support, so some functions that the plug-in provides might not be included in the PrintTicket or PrintCapabilities documents.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Driver%20Plug-in%20Support%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


