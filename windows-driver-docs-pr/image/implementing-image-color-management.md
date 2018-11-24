---
title: Implementing Image Color Management
description: Implementing Image Color Management
ms.assetid: b3184a8b-4f32-4cb0-8f68-777d85110142
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing Image Color Management





WIA relies on the Image Color Management (ICM) system provided in Microsoft Windows. ICM is described in the Microsoft Windows SDK documentation.

For best application compatibility, all minidrivers are expected to return data in the sRGB color space. If a device natively produces data in a different color space, the minidriver should use the ICM functions to map its output to sRGB. Some applications implement ICM and may want to retrieve data in the native color space. Minidrivers can allow this functionality by specifying the native color space in the setup information (INF) file and specifying a valid value of 1 for the [**WIA\_IPA\_APP\_COLOR\_MAPPING**](https://msdn.microsoft.com/library/windows/hardware/ff551521) property.

When the application sets the property to 1, the minidriver should stop mapping to sRGB and allow the application to handle the mapping. The application uses the current value of the [**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551571) property as the profile for the data from the device. The user sets the property using system dialogs and it should not be changed by the minidriver.

 

 




