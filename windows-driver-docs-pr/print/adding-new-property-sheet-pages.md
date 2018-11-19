---
title: Adding New Property Sheet Pages
description: Adding New Property Sheet Pages
ms.assetid: ec4303e9-889c-41ee-8872-ddefdc906eb2
keywords:
- user interface plug-ins WDK print , property sheet pages
- UI plug-ins WDK print , property sheet pages
- property sheet pages WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding New Property Sheet Pages





If you want to add new pages to the property sheets provided by the printer interface to Unidrv or Pscript5, your UI plug-in must implement the following IPrintOemUI methods:

-   [**IPrintOemUI::DevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554165)

    Used to add to the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window, or when an application calls the PrinterProperties function (described in the Windows SDK documentation).

-   [**IPrintOemUI::DocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554173)

    Used to add pages to the document property sheet, which is displayed when a user selects the **Printer Preferences** menu item from the printer folder or a printer window, or when an application calls the DocumentProperties or AdvancedDocumentProperties functions (described in the Windows SDK documentation).

If you implement one of these methods, you will typically also supply a [**\_CPSUICALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff564313)-typed callback function to handle user modifications. This callback function must call [**IPrintOemDriverUI::DrvUpdateUISetting**](https://msdn.microsoft.com/library/windows/hardware/ff553115) to inform the driver when the value associated with a user interface setting has been modified, if the setting's value is stored in the driver's [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure or registry keys.

 

 




