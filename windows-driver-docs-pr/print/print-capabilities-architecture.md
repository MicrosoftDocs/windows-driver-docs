---
title: Print Capabilities Architecture
description: Print Capabilities Architecture
ms.assetid: d19438ca-8c88-4835-8445-2799387e0912
keywords: ["Print Capabilities WDK , architecture"]
---

# Print Capabilities Architecture


The PrintCapabilities object is returned by the [**IPrintTicketProvider::GetPrintCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff554365) method of the print driver's implementation of the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375). XPSDrv print drivers must implement the IPrintTicketProvider interface in addition to the [**DrvDeviceCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff548539) function.

You can modify older, GDI-based print drivers to provide a PrintCapabilities document directly but this modification is not required. The Windows Vista print subsystem creates an XML PrintCapabilities document for GDI-based drivers that do not add the ability to return one. The PrintCapabilities document that the Windows Vista print subsystem creates, however, includes only the limited set of parameters that the Microsoft Win32 function, **DeviceCapabilities** , supports. For a GDI-based print driver to provide a complete list of the printer's features and capabilities, it must include support for the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375).

The following list and diagram illustrate how the different types of print drivers can support the Print Capabilities technology:

<a href="" id="unidrv-or-pscript5-print-driver"></a>Unidrv or PScript5 print driver  
The [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375) has been added to Universal (Unidrv) and PostScript (PScript5) print drivers in Windows Vista.

<a href="" id="unidrv-or-pscript5-print-driver-plug-in"></a>Unidrv or PScript5 print driver plug-in  
Unidrv and Pscript5 print drivers that have custom features require plug-ins to add or remove the features and return an accurate PrintCapabilities document. The custom feature plug-ins for a Unidrv and a PScript5 print driver must support the [IPrintOemPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff553174).

<a href="" id="-monolithic-gdi-based-and-xpsdrv-print-drivers"></a> Monolithic GDI-based and XPSDrv print drivers  
XPSDrv print drivers must support the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375). GDI-based, monolithic print drivers must support the IPrintTicketProvider interface to return printer capabilities and features that the Win32 function, **DeviceCapabilities**, does not provide.

![diagram illustrating the print capabilities support in print drivers](images/ptpcarch1.gif)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Capabilities%20Architecture%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




