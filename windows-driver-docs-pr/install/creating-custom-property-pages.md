---
title: Creating Custom Property Pages
description: Creating Custom Property Pages
ms.assetid: 2481450f-ebb2-40e3-8a42-eabaecc1c7e4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Custom Property Pages


When a [device property page provider](types-of-device-property-page-providers.md) handles a request to create a property page for its device or device class, the provider should take the following steps:

1.  Call [**SetupDiGetClassInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551083) to get the current class install parameters for the device. For example:

    ```cpp
    SP_ADDPROPERTYPAGE_DATA AddPropertyPageData;
    :
    ZeroMemory(&AddPropertyPageData, sizeof(SP_ADDPROPERTYPAGE_DATA));
    AddPropertyPageData.ClassInstallHeader.cbSize = sizeof(SP_CLASSINSTALL_HEADER);

    if (SetupDiGetClassInstallParams(DeviceInfoSet, DeviceInfoData,
         (PSP_CLASSINSTALL_HEADER)&AddPropertyPageData,
         sizeof(SP_ADDPROPERTYPAGE_DATA), NULL )) {
    ...
    ```

    In this example, the code zero-initializes the structure in which the installation parameters of the device will be returned, and sets the size of the class install header in the **cbSize** field as required by **SetupDiGetClassInstallParams**. The class install header is the first member of each class install parameters structure.

2.  Make sure that the maximum number of dynamic pages for the device has not yet been met by using a statement such as the following:

    ```cpp
    if (AddPropertyPageData.NumDynamicPages < 
        MAX_INSTALLWIZARD_DYNAPAGES)
     ...
    ```

    If the test fails, do not initialize or create the page. Instead, return NO_ERROR.

3.  Allocate memory in which to save any device-specific data that will be needed later in the dialog box procedure and initialize this memory with the data. The provider must release this memory in its property page callback when the property page is destroyed.

    For providers that are [co-installers](writing-a-co-installer.md), this device-specific data must include the *DeviceInfoSet* and *DeviceInfoData* passed with the [**DIF_ADDPROPERTYPAGE_ADVANCED**](https://msdn.microsoft.com/library/windows/hardware/ff543656) device installation function (DIF) code.

    For example, a property page provider can define and use a structure as shown in the following example:

    ```cpp
    typedef struct _TEST_PROP_PAGE_DATA {
        HDEVINFO DeviceInfoSet;
        PSP_DEVINFO_DATA DeviceInfoData;
    } TEST_PROP_PAGE_DATA, *PTEST_PROP_PAGE_DATA;
    ...
    PTEST_PROP_PAGE_DATA     pMyPropPageData;
    ...
    pMyPropPageData = HeapAlloc(GetProcessHeap(), 0, sizeof(TESTPROP_PAGE_DATA));
    ```

4.  Initialize a PROPSHEETPAGE structure with information about the custom property page:

    -   In **dwFlags**, set the PSP_USECALLBACK flag and any other flags that are required for the custom property page. The PSP_USECALLBACK flag indicates that a callback function has been supplied.
    -   In **pfnCallback**, set a pointer to the callback function for the property page. In the callback, process the PSPCB_RELEASE message and free the memory that was allocated in step 3.
    -   In **pfnDlgProc**, set a pointer to the dialog box procedure for the property page.
    -   In **lParam**, pass a pointer to the memory area that was allocated and initialized in step 3.
    -   Set other members as appropriate for the custom property page. See the Microsoft Windows SDK documentation for more information about the PROPSHEETPAGE structure.

5.  Call **CreatePropertySheetPage** to create the new page.

6.  Add the new page to the list of dynamic property pages in the **DynamicPages** member of the class install parameters and increment the **NumDynamicPages** member.

7.  Repeat steps 2 through 6 for each additional custom property page.

8.  Call [**SetupDiSetClassInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552122) to set the new class install parameters, which include the updated property page structure.

9.  Return NO_ERROR.

Windows adds the newly created property pages to the property sheet for the device, and Device Manager makes Microsoft Win32 API calls to create the sheet. When the property page is displayed, the system calls the dialog box procedure that is specified in the PROPSHEETPAGE structure.

 

 





