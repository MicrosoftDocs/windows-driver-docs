---
title: Modifying a Driver-Supplied Property Sheet Page
author: windows-driver-content
description: Modifying a Driver-Supplied Property Sheet Page
ms.assetid: 98338017-96a0-414c-9b80-bcb98eff61e5
keywords: ["user interface plug-ins WDK print , property sheet pages", "UI plug-ins WDK print , property sheet pages", "property sheet pages WDK print", "option items WDK UI plug-in", "customized option items WDK UI plug-in"]
---

# Modifying a Driver-Supplied Property Sheet Page


## <a href="" id="ddk-modifying-a-driver-supplied-property-sheet-page-gg"></a>


A UI plug-in can modify Unidrv-supplied or Pscript5-supplied property sheet pages by implementing the [**IPrintOemUI::CommonUIProp**](https://msdn.microsoft.com/library/windows/hardware/ff554159) method and a callback function.

The UI plug-in uses the **IPrintOemUI::CommonUIProp** method to specify a set of option items that [CPSUI](common-property-sheet-user-interface.md) can add, remove, or replace within either the printer property sheet's **Device Settings** page or the document property sheet's **Layout**, **Paper/Quality**, and **Advanced** pages.

The callback function, of type [**OEMCUIPCALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557650), is used to process user modifications to customized option items.

### <a href="" id="ddk-adding-option-items-gg"></a>Adding Option Items

Your UI plug-in must describe new option items by placing them in an array of [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structures supplied by the driver. The driver's printer interface DLL calls the UI plug-in's [**IPrintOemUI::CommonUIProp**](https://msdn.microsoft.com/library/windows/hardware/ff554159) method twice. The first time the method is called, it should return the number of OPTITEM structures required. The driver allocates space for an OPTITEM array and describes the array in an [**OEMCUIPPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff557653) structure. The driver calls **IPrintOemUI::CommonUIProp** again, supplying the address of the OEMCUIPPARAM structure, so the method can load the OPTITEM structures with option descriptions.

### <a href="" id="ddk-removing-option-items-gg"></a>Removing Option Items

To remove an option from a property sheet page that is supplied by Unidrv or Pscript5, your UI plug-in's [**IPrintOemUI::CommonUIProp**](https://msdn.microsoft.com/library/windows/hardware/ff554159) method can traverse the array of [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structures pointed to by the [**OEMCUIPPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff557653) structure. For each option that you would like to remove from the property sheet, you can set the OPTITEM structure's OPTIF\_HIDE flag. (Note that this does not actually remove the option; it hides the option from the user so that the user cannot change its default value.)

### <a href="" id="ddk-replacing-option-items-gg"></a>Replacing Option Items

To replace an option in a property sheet page that is supplied by Unidrv or Pscript, you should follow the instructions shown under the preceding **Removing Option Items** section to remove the existing option item, and then follow the instructions under the preceding **Adding Option Items** section to create a new option item to replace the old one.

### <a href="" id="ddk-handling-modifications-to-customized-option-values-gg"></a>Handling Modifications to Customized Option Values

In order to process user modifications to customized option items, you must provide at least one callback function. You can either specify a single callback function that handles options for both the document property sheet and the printer property sheet, or you can specify a separate function for each. These callbacks are of type [**OEMCUIPCALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff557650).

A callback function is specified by placing its address in an [**OEMCUIPPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff557653) structure. The UI plug-in receives the address of this structure as input to its [**IPrintOemUI::CommonUIProp**](https://msdn.microsoft.com/library/windows/hardware/ff554159) method.

When a user opens the printer property sheet or document property sheet and modifies options, [CPSUI](common-property-sheet-user-interface.md) calls the printer driver's printer interface DLL. This DLL processes option values contained in its own [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structures. Then for each UI plug-in, the printer interface DLL calls the OEMCUIPCALLBACK-typed callback function that was previously specified by **IPrintOemUI::CommonUIProp**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Modifying%20a%20Driver-Supplied%20Property%20Sheet%20Page%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


