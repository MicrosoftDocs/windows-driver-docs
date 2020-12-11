---
title: Adding New Property Sheet Pages
description: Adding New Property Sheet Pages
keywords:
- user interface plug-ins WDK print , property sheet pages
- UI plug-ins WDK print , property sheet pages
- property sheet pages WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding New Property Sheet Pages





If you want to add new pages to the property sheets provided by the printer interface to Unidrv or Pscript5, your UI plug-in must implement the following IPrintOemUI methods:

-   [**IPrintOemUI::DevicePropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-devicepropertysheets)

    Used to add to the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window, or when an application calls the PrinterProperties function (described in the Windows SDK documentation).

-   [**IPrintOemUI::DocumentPropertySheets**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-documentpropertysheets)

    Used to add pages to the document property sheet, which is displayed when a user selects the **Printer Preferences** menu item from the printer folder or a printer window, or when an application calls the DocumentProperties or AdvancedDocumentProperties functions (described in the Windows SDK documentation).

If you implement one of these methods, you will typically also supply a [**\_CPSUICALLBACK**](/windows-hardware/drivers/ddi/compstui/nc-compstui-_cpsuicallback)-typed callback function to handle user modifications. This callback function must call [**IPrintOemDriverUI::DrvUpdateUISetting**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupdateuisetting) to inform the driver when the value associated with a user interface setting has been modified, if the setting's value is stored in the driver's [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure or registry keys.

 

