---
title: OpenPrinter
author: windows-driver-content
description: OpenPrinter
MS-HAID:
- 'drvarch\_c29d5085-f77d-416d-acfd-a799d0c08663.xml'
- 'print.openprinter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8bbb46a8-2bba-4d15-a2e2-4770b52d2505
keywords: ["OpenPrinter"]
---

# OpenPrinter


When a print queue is opened (by using the `OpenPrinter` function), the print driver is loaded and the following methods of the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375) are called in this order:

1.  [**IPrintTicketProvider::GetSupportedVersions**](https://msdn.microsoft.com/library/windows/hardware/ff554371)

2.  [**IPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff554354)

3.  [**IPrintTicketProvider::QueryDeviceNamespace**](https://msdn.microsoft.com/library/windows/hardware/ff554378)

The methods of the **IPrintTicketProvider** interface in a Unidrv or PScript5 print driver call the **IPrintOemPrintTicketProvider** methods of the each plug-in hosted by the driver. The following illustration and list show how these calls are made when `OpenPrinter` is called.

![diagram illustrating the openprinter calling sequence](images/ptpcopen-uml.gif)

1.  For each plug-in, call [**IPrintOemPrintTicketProvider::GetSupportedVersions**](https://msdn.microsoft.com/library/windows/hardware/ff553170).

2.  For each plug-in, call [**IPrintOemPrintTicketProvider::BindPrinter**](https://msdn.microsoft.com/library/windows/hardware/ff553151).

3.  For each plug-in, call [**IPrintOemPrintTicketProvider::QueryDeviceDefaultNamespace**](https://msdn.microsoft.com/library/windows/hardware/ff553180).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OpenPrinter%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


