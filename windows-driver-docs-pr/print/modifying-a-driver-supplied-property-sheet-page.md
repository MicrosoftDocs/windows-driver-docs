---
title: Modifying a Driver-Supplied Property Sheet Page
description: Modifying a Driver-Supplied Property Sheet Page
keywords:
- user interface plug-ins WDK print , property sheet pages
- UI plug-ins WDK print , property sheet pages
- property sheet pages WDK print
- option items WDK UI plug-in
- customized option items WDK UI plug-in
ms.date: 01/27/2023
---

# Modifying a Driver-Supplied Property Sheet Page

[!include[Print Support Apps](../includes/print-support-apps.md)]

A UI plug-in can modify Unidrv-supplied or Pscript5-supplied property sheet pages by implementing the [**IPrintOemUI::CommonUIProp**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-commonuiprop) method and a callback function.

The UI plug-in uses the **IPrintOemUI::CommonUIProp** method to specify a set of option items that [CPSUI](common-property-sheet-user-interface.md) can add, remove, or replace within either the printer property sheet's **Device Settings** page or the document property sheet's **Layout**, **Paper/Quality**, and **Advanced** pages.

The callback function, of type [**OEMCUIPCALLBACK**](/windows-hardware/drivers/ddi/printoem/nc-printoem-oemcuipcallback), is used to process user modifications to customized option items.

### <a href="" id="ddk-adding-option-items-gg"></a>Adding Option Items

Your UI plug-in must describe new option items by placing them in an array of [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) structures supplied by the driver. The driver's printer interface DLL calls the UI plug-in's [**IPrintOemUI::CommonUIProp**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-commonuiprop) method twice. The first time the method is called, it should return the number of OPTITEM structures required. The driver allocates space for an OPTITEM array and describes the array in an [**OEMCUIPPARAM**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_oemcuipparam) structure. The driver calls **IPrintOemUI::CommonUIProp** again, supplying the address of the OEMCUIPPARAM structure, so the method can load the OPTITEM structures with option descriptions.

### <a href="" id="ddk-removing-option-items-gg"></a>Removing Option Items

To remove an option from a property sheet page that is supplied by Unidrv or Pscript5, your UI plug-in's [**IPrintOemUI::CommonUIProp**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-commonuiprop) method can traverse the array of [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) structures pointed to by the [**OEMCUIPPARAM**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_oemcuipparam) structure. For each option that you would like to remove from the property sheet, you can set the OPTITEM structure's OPTIF\_HIDE flag. (Note that this does not actually remove the option; it hides the option from the user so that the user cannot change its default value.)

### <a href="" id="ddk-replacing-option-items-gg"></a>Replacing Option Items

To replace an option in a property sheet page that is supplied by Unidrv or Pscript, you should follow the instructions shown under the preceding **Removing Option Items** section to remove the existing option item, and then follow the instructions under the preceding **Adding Option Items** section to create a new option item to replace the old one.

### <a href="" id="ddk-handling-modifications-to-customized-option-values-gg"></a>Handling Modifications to Customized Option Values

In order to process user modifications to customized option items, you must provide at least one callback function. You can either specify a single callback function that handles options for both the document property sheet and the printer property sheet, or you can specify a separate function for each. These callbacks are of type [**OEMCUIPCALLBACK**](/windows-hardware/drivers/ddi/printoem/nc-printoem-oemcuipcallback).

A callback function is specified by placing its address in an [**OEMCUIPPARAM**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_oemcuipparam) structure. The UI plug-in receives the address of this structure as input to its [**IPrintOemUI::CommonUIProp**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemui-commonuiprop) method.

When a user opens the printer property sheet or document property sheet and modifies options, [CPSUI](common-property-sheet-user-interface.md) calls the printer driver's printer interface DLL. This DLL processes option values contained in its own [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) structures. Then for each UI plug-in, the printer interface DLL calls the OEMCUIPCALLBACK-typed callback function that was previously specified by **IPrintOemUI::CommonUIProp**.
