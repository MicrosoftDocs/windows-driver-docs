---
title: Accessing Device Instance Properties
description: Accessing Device Instance Properties
ms.assetid: b571201a-e765-45d0-993b-5855041b4697
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Instance Properties


In Windows Vista and later versions of Windows, applications and installers can access [device instance properties](https://msdn.microsoft.com/library/windows/hardware/ff541334) by calling the following SetupAPI functions:

-   [**SetupDiGetDevicePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551965)

    The **SetupDiGetDevicePropertyKeys** function retrieves an array of the device property keys that identify the device properties that are currently set for a device instance. For information about how to determine what properties are set for a device, see [Determining Which Properties Are Set for a Device Instance](determining-which-properties-are-set-for-a-device-instance.md).

-   [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

    The **SetupDiGetDeviceProperty** function [retrieves a device property that is set for a device instance](retrieving-a-device-instance-property-value.md).

-   [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

    The **SetupDiSetDeviceProperty** function [sets a device property for a device instance](setting-a-device-instance-property-value.md).

For information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000, see [Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md).

 

 





