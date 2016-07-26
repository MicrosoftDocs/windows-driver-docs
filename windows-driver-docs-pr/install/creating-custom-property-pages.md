---
title: Creating Custom Property Pages
description: Creating Custom Property Pages
ms.assetid: 2481450f-ebb2-40e3-8a42-eabaecc1c7e4
---

# Creating Custom Property Pages


When a [device property page provider](types-of-device-property-page-providers.md) handles a request to create a property page for its device or device class, the provider should take the following steps:

1.  Call [**SetupDiGetClassInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551083) to get the current class install parameters for the device. For example:

    ```
    SP_ADDPROPERTYPAGE_DATA AddPropertyPageData;
    :
    ZeroMemory(&amp;AddPropertyPageData, sizeof(SP_ADDPROPERTYPAGE_DATA));
    AddPropertyPageData.ClassInstallHeader.cbSize = sizeof(SP_CLASSINSTALL_HEADER);

    if (SetupDiGetClassInstallParams(DeviceInfoSet, DeviceInfoData,
         (PSP_CLASSINSTALL_HEADER)&amp;AddPropertyPageData,
         sizeof(SP_ADDPROPERTYPAGE_DATA), NULL )) {
    ...
    ```

    In this example, the code zero-initializes the structure in which the installation parameters of the device will be returned, and sets the size of the class install header in the **cbSize** field as required by **SetupDiGetClassInstallParams**. The class install header is the first member of each class install parameters structure.

2.  Make sure that the maximum number of dynamic pages for the device has not yet been met by using a statement such as the following:

    ```
    if (AddPropertyPageData.NumDynamicPages < 
        MAX_INSTALLWIZARD_DYNAPAGES)
     ...
    ```

    If the test fails, do not initialize or create the page. Instead, return NO\_ERROR.

3.  Allocate memory in which to save any device-specific data that will be needed later in the dialog box procedure and initialize this memory with the data. The provider must release this memory in its property page callback when the property page is destroyed.

    For providers that are [co-installers](writing-a-co-installer.md), this device-specific data must include the *DeviceInfoSet* and *DeviceInfoData* passed with the [**DIF\_ADDPROPERTYPAGE\_ADVANCED**](https://msdn.microsoft.com/library/windows/hardware/ff543656) device installation function (DIF) code.

    For example, a property page provider can define and use a structure as shown in the following example:

    ```
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

    -   In **dwFlags**, set the PSP\_USECALLBACK flag and any other flags that are required for the custom property page. The PSP\_USECALLBACK flag indicates that a callback function has been supplied.
    -   In **pfnCallback**, set a pointer to the callback function for the property page. In the callback, process the PSPCB\_RELEASE message and free the memory that was allocated in step 3.
    -   In **pfnDlgProc**, set a pointer to the dialog box procedure for the property page.
    -   In **lParam**, pass a pointer to the memory area that was allocated and initialized in step 3.
    -   Set other members as appropriate for the custom property page. See the Microsoft Windows SDK documentation for more information about the PROPSHEETPAGE structure.

5.  Call **CreatePropertySheetPage** to create the new page.

6.  Add the new page to the list of dynamic property pages in the **DynamicPages** member of the class install parameters and increment the **NumDynamicPages** member.

7.  Repeat steps 2 through 6 for each additional custom property page.

8.  Call [**SetupDiSetClassInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552122) to set the new class install parameters, which include the updated property page structure.

9.  Return NO\_ERROR.

Windows adds the newly created property pages to the property sheet for the device, and Device Manager makes Microsoft Win32 API calls to create the sheet. When the property page is displayed, the system calls the dialog box procedure that is specified in the PROPSHEETPAGE structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Creating%20Custom%20Property%20Pages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




