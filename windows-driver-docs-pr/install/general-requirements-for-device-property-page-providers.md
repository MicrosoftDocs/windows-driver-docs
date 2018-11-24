---
title: General Requirements for Device Property Page Providers
description: General Requirements for Device Property Page Providers
ms.assetid: 91e93679-8c0c-43e7-a7d9-72bd0a464406
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Requirements for Device Property Page Providers


To create device property pages, a provider must follow these general requirements in order for the property page to work correctly:

-   Handle the request to add a property page.

    For providers that are property page extension DLLs, this request is made through the **AddPropSheetPageProc** callback function. For more information, see [Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)](specific-requirements-for-device-property-page-providers--property-pag.md)

-   Create the property page by calling the **CreatePropertySheetPage** function. The provider passes the address of the initialized PROPSHEETPAGE structure in this call.

-   Supply a **PropSheetPageProc** callback function that handles PSPCB_CREATE and PSPCB_RELEASE messages if additional storage must be allocated and released for a property page.

-   Supply a dialog box procedure that handles Windows messages for each custom property page.
-   Initialize a PROPSHEETPAGE structure with (among other things) the addresses of the **PropSheetPageProc** callback function and dialog box procedure.

This section includes the following topics that provide more guidance about custom property pages:

[Creating Custom Property Pages](creating-custom-property-pages.md)

[Property Page Callback Function](property-page-callback-function.md)

[Handling Windows Messages for Property Pages](handling-windows-messages-for-property-pages.md)

[Sample Custom Property Page](sample-custom-property-page.md)

 

 





