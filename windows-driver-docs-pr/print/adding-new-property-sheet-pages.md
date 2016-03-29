---
title: Adding New Property Sheet Pages
description: Adding New Property Sheet Pages
ms.assetid: ec4303e9-889c-41ee-8872-ddefdc906eb2
keywords: ["user interface plug-ins WDK print , property sheet pages", "UI plug-ins WDK print , property sheet pages", "property sheet pages WDK print"]
---

# Adding New Property Sheet Pages


## <a href="" id="ddk-adding-new-property-sheet-pages-gg"></a>


If you want to add new pages to the property sheets provided by the printer interface to Unidrv or Pscript5, your UI plug-in must implement the following IPrintOemUI methods:

-   [**IPrintOemUI::DevicePropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554165)

    Used to add to the printer property sheet, which is displayed when a user selects the **Properties** menu item from the printer folder or a printer window, or when an application calls the PrinterProperties function (described in the Windows SDK documentation).

-   [**IPrintOemUI::DocumentPropertySheets**](https://msdn.microsoft.com/library/windows/hardware/ff554173)

    Used to add pages to the document property sheet, which is displayed when a user selects the **Printer Preferences** menu item from the printer folder or a printer window, or when an application calls the DocumentProperties or AdvancedDocumentProperties functions (described in the Windows SDK documentation).

If you implement one of these methods, you will typically also supply a [**\_CPSUICALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff564313)-typed callback function to handle user modifications. This callback function must call [**IPrintOemDriverUI::DrvUpdateUISetting**](https://msdn.microsoft.com/library/windows/hardware/ff553115) to inform the driver when the value associated with a user interface setting has been modified, if the setting's value is stored in the driver's [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure or registry keys.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Adding%20New%20Property%20Sheet%20Pages%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




