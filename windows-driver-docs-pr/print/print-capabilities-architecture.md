---
title: Print capabilities architecture
description: Provides information about print capabilities architecture.
keywords:
- Print Capabilities WDK, architecture
ms.date: 09/07/2022
---

# Print capabilities architecture

The PrintCapabilities object is returned by the [**IPrintTicketProvider::GetPrintCapabilities**](/windows-hardware/drivers/ddi/prdrvcom/nf-prdrvcom-iprintticketprovider-getprintcapabilities) method of the print driver's implementation of the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface. XPSDrv print drivers must implement the IPrintTicketProvider interface in addition to the [**DrvDeviceCapabilities**](/windows-hardware/drivers/ddi/winddiui/nf-winddiui-drvdevicecapabilities) function.

You can modify older, GDI-based print drivers to provide a PrintCapabilities document directly but this modification is not required. The Windows Vista print subsystem creates an XML PrintCapabilities document for GDI-based drivers that do not add the ability to return one. The PrintCapabilities document that the Windows Vista print subsystem creates, however, includes only the limited set of parameters that the Microsoft Win32 function, **DeviceCapabilities** , supports. For a GDI-based print driver to provide a complete list of the printer's features and capabilities, it must include support for the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface.

The following list and diagram illustrate how the different types of print drivers can support the Print Capabilities technology:

**Unidrv or PScript5 print driver**  
The [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface has been added to Universal (Unidrv) and PostScript (PScript5) print drivers in Windows Vista.

**Unidrv or PScript5 print driver plug-in**  
Unidrv and Pscript5 print drivers that have custom features require plug-ins to add or remove the features and return an accurate PrintCapabilities document. The custom feature plug-ins for a Unidrv and a PScript5 print driver must support the [**IPrintOemPrintTicketProvider**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintoemprintticketprovider) interface.

**Monolithic GDI-based and XPSDrv print drivers**  
XPSDrv print drivers must support the [**IPrintTicketProvider**](/windows-hardware/drivers/ddi/prdrvcom/nn-prdrvcom-iprintticketprovider) interface. GDI-based, monolithic print drivers must support the **IPrintTicketProvider** interface to return printer capabilities and features that the Win32 function, **DeviceCapabilities**, does not provide.

![diagram illustrating the print capabilities support in print drivers.](images/ptpcarch1.gif)
