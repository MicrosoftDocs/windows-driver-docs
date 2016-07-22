---
title: General Requirements for Device Property Page Providers
description: General Requirements for Device Property Page Providers
ms.assetid: 91e93679-8c0c-43e7-a7d9-72bd0a464406
---

# General Requirements for Device Property Page Providers


To create device property pages, a provider must follow these general requirements in order for the property page to work correctly:

-   Handle the request to add a property page.

    For providers that are property page extension DLLs, this request is made through the **AddPropSheetPageProc** callback function. For more information, see [Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)](specific-requirements-for-device-property-page-providers--property-pag.md)

-   Create the property page by calling the **CreatePropertySheetPage** function. The provider passes the address of the initialized PROPSHEETPAGE structure in this call.

-   Supply a **PropSheetPageProc** callback function that handles PSPCB\_CREATE and PSPCB\_RELEASE messages if additional storage must be allocated and released for a property page.

-   Supply a dialog box procedure that handles Windows messages for each custom property page.
-   Initialize a PROPSHEETPAGE structure with (among other things) the addresses of the **PropSheetPageProc** callback function and dialog box procedure.

This section includes the following topics that provide more guidance about custom property pages:

[Creating Custom Property Pages](creating-custom-property-pages.md)

[Property Page Callback Function](property-page-callback-function.md)

[Handling Windows Messages for Property Pages](handling-windows-messages-for-property-pages.md)

[Sample Custom Property Page](sample-custom-property-page.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20General%20Requirements%20for%20Device%20Property%20Page%20Providers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




