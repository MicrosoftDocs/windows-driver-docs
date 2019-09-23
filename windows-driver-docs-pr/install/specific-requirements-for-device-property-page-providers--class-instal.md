---
title: Requirements for Device Property Page Providers (Co-Installers)
description: Specific Requirements for Device Property Page Providers (Co-Installers)
ms.assetid: b57beaed-5e5f-499e-b973-532f33b7fb99
keywords:
- device property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED
- property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED
- custom property pages WDK device installations , DIF_ADDPROPERTYPAGE_ADVANCED
- DIF_ADDPROPERTYPAGE_ADVANCED
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specific Requirements for Device Property Page Providers (Co-Installers)





A [co-installer](writing-a-co-installer.md) that provides one or more custom device property pages must handle the [**DIF_ADDPROPERTYPAGE_ADVANCED**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-addpropertypage-advanced) device installation function (DIF) code. Device Manager issues this request when a user clicks on the **Properties** tab of a device in Device Manager or in Control Panel.

In response to this request, the installer provides information about each of its custom property pages, creates the pages, and adds the created pages to the list of dynamic property pages for the device. The installer does this by initializing and returning an SP_ADDPROPERTYPAGE_DATA structure for the class installation parameters of the request.

If the user changes any properties, Device Manager sends a [**DIF_PROPERTYCHANGE**](https://docs.microsoft.com/windows-hardware/drivers/install/dif-propertychange) DIF code to the installer after the installer sets the new parameters by calling [**SetupDiSetDeviceInstallParams**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdisetdeviceinstallparamsa).

For more information about how to create a custom device property page by a [co-installer](writing-a-co-installer.md), see [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

 

 





