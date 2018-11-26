---
title: Creating Your Property Sheet
description: Creating Your Property Sheet
ms.assetid: 04fa34fd-86d6-4017-a6da-9882d65674e3
keywords: ["property sheets WDK DirectInput , creating", "game controllers WDK DirectInput , property sheet creation", "control panels WDK DirectInput , property sheet creation", "sample property sheet applications WDK DirectInput", "custom property sheets WDK DirectInput", "templates WDK DirectInput"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Creating Your Property Sheet





This example demonstrates many aspects of DirectInput and provides a good starting point for your own custom property sheet.

### To create your own property sheet:

Creating a custom property sheet from scratch is a relatively simple process.

1.  Create a GUID to identify your property page:
    -   Using the GuidGen tool (which is included in the Microsoft Windows SDK), create a GUID for your property page (only one, no matter how many pages). Define this in your application-specific include file. It should look something like:
        ```cpp
        
        ```

    -   Create the required DllGetClassObject and DllCanUnloadNow.
    -   Create an implementation for the COM ClassFactory defined in Dicpl.h.
    -   Create the implementation for the **IDIGamgeCntrlPropSheet** interface.
    -   Using Regedit, add your defined GUID to the My Computer\\HKEY\_CLASSES\_ROOT\\CLSID key. Then add the keys InProcHandler32 and InProcServer32 to your key.
    -   Modify the (default) entry of the InProcServer32 entry to point to the location of your property sheet DLL. An example would be: "C:\\my\_device\\my\_propertysheet.dll". This example shows a ProgID entry. This is not necessary, but is often used to store information about the module residing at that GUID.

2.  Create dialog templates and dialog procedures as you would for any Windows application.

    **Note**   You may want to write a test container for your property sheets as a window that launches your pages as independent dialog boxes. At this point, you could also convert any existing control panel you might have to the DirectInput control panel.

     

3.  Populate the [**DIGCPAGEINFO**](https://msdn.microsoft.com/library/windows/hardware/ff538484) and [**DIGCSHEETINFO**](https://msdn.microsoft.com/library/windows/hardware/ff538492) structures and return that information in your implementations of [**IDIGameCntrlPropSheet::GetPageInfo**](https://msdn.microsoft.com/library/windows/hardware/ff540026) and [**IDIGameCntrlPropSheet::GetSheetInfo**](https://msdn.microsoft.com/library/windows/hardware/ff540029) respectively.

The generation of the property sheet pages is done through the **PropertySheet** function. All behaviors of this function are inherent in the property sheet pages. For example, the property sheet page reflects the largest dialog template that it receives. If the user creates one page and its associated template is very small, this reflects directly on the size of the resulting dialog.

Dialog templates are also important to remember when considering visual alignment and the centering of controls on a page. For example, consider a case in which the user creates two pages that contain items specified to be centered on the page. One item to be centered is 200 dialog units (DLUs) in width; the other is 100 units. In such a case, the latter item is not centered on the page. Instead, the control is centered to its template and additional white space (or gray, as it may be) is added to the width of the more narrow page. You should create dialog templates of the same size, even if you are not using it all. (For more information about the **PropertySheet** function, see the Microsoft Win32 SDK.)

 

 




