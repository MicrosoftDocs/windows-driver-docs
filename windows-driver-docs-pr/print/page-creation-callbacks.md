---
title: Page Creation Callbacks
author: windows-driver-content
description: Page Creation Callbacks
MS-HAID:
- 'cpsui\_24224479-1b57-4293-b191-fc990941e6f4.xml'
- 'print.page\_creation\_callbacks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ec514d17-415e-417b-bb29-b37be43c3cf6
keywords: ["callback functions WDK CPSUI", "Common Property Sheet User Interface WDK print , callbacks", "CPSUI WDK print , callbacks", "property sheet pages WDK print , callbacks", "page creation callbacks WDK CPSUI", "CommonPropertySheetUI"]
---

# Page Creation Callbacks


## <a href="" id="ddk-page-creation-callbacks-gg"></a>


When an application makes an initial call into CPSUI's entry point function ([**CommonPropertySheetUI**](https://msdn.microsoft.com/library/windows/hardware/ff546148)), it must include the address of a [**PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff559812)-typed callback function. This callback function is responsible for describing property sheet pages and sending these descriptions to CPSUI for creation.

CPSUI's **CommonPropertySheetUI** function immediately calls back to the PFNPROPSHEETUI-typed function, supplying the address of a [**PROPSHEETUI\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff561767) structure. The application can then call CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function, supplying page descriptions that CPSUI can use to create the pages, as illustrated in the following diagram:

![diagram illustrating application-cpsui communication](images/comprop.png)

For more information, see [Methods for Specifying Pages](methods-for-specifying-pages.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Page%20Creation%20Callbacks%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


