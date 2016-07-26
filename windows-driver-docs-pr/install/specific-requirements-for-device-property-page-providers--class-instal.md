---
title: Specific Requirements for Device Property Page Providers (Co-Installers)
description: Specific Requirements for Device Property Page Providers (Co-Installers)
ms.assetid: b57beaed-5e5f-499e-b973-532f33b7fb99
keywords: ["device property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED", "property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED", "custom property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED", "DIF_ADDPROPERTYPAGE_ADVANCED"]
---

# Specific Requirements for Device Property Page Providers (Co-Installers)


## <a href="" id="ddk-handling-dif-addpropertypage-advanced-requests-dg"></a>


A [co-installer](writing-a-co-installer.md) that provides one or more custom device property pages must handle the [**DIF\_ADDPROPERTYPAGE\_ADVANCED**](https://msdn.microsoft.com/library/windows/hardware/ff543656) device installation function (DIF) code. Device Manager issues this request when a user clicks on the **Properties** tab of a device in Device Manager or in Control Panel.

In response to this request, the installer provides information about each of its custom property pages, creates the pages, and adds the created pages to the list of dynamic property pages for the device. The installer does this by initializing and returning an SP\_ADDPROPERTYPAGE\_DATA structure for the class installation parameters of the request.

If the user changes any properties, Device Manager sends a [**DIF\_PROPERTYCHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff543712) DIF code to the installer after the installer sets the new parameters by calling [**SetupDiSetDeviceInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff552141).

For more information about how to create a custom device property page by a [co-installer](writing-a-co-installer.md), see [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Specific%20Requirements%20for%20Device%20Property%20Page%20Providers%20%28Co-Installers%29%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




