---
title: Creating Your Property Sheet
author: windows-driver-content
description: Creating Your Property Sheet
MS-HAID:
- 'di\_0b4f22e3-71ca-4c72-b4fa-2db3c053562a.xml'
- 'hid.creating\_your\_property\_sheet'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 04fa34fd-86d6-4017-a6da-9882d65674e3
keywords: ["property sheets WDK DirectInput , creating", "game controllers WDK DirectInput , property sheet creation", "control panels WDK DirectInput , property sheet creation", "sample property sheet applications WDK DirectInput", "custom property sheets WDK DirectInput", "templates WDK DirectInput"]
---

# Creating Your Property Sheet


## <a href="" id="ddk-creating-your-property-sheet-di"></a>


This example demonstrates many aspects of DirectInput and provides a good starting point for your own custom property sheet.

### To create your own property sheet:

Creating a custom property sheet from scratch is a relatively simple process.

1.  Create a GUID to identify your property page:
    -   Using the GuidGen tool (which is included in the Microsoft Windows SDK), create a GUID for your property page (only one, no matter how many pages). Define this in your application-specific include file. It should look something like:
        ```
        
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Creating%20Your%20Property%20Sheet%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


