---
title: Accessing Device Instance Properties
description: Accessing Device Instance Properties
ms.date: 04/20/2017
---

# Accessing Device Instance Properties


In Windows Vista and later versions of Windows, applications and installers can access [device instance properties](/previous-versions/ff541334(v=vs.85)) by calling the following SetupAPI functions:

-   [**SetupDiGetDevicePropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys)

    The **SetupDiGetDevicePropertyKeys** function retrieves an array of the device property keys that identify the device properties that are currently set for a device instance. For information about how to determine what properties are set for a device, see [Determining Which Properties Are Set for a Device Instance](determining-which-properties-are-set-for-a-device-instance.md).

-   [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

    The **SetupDiGetDeviceProperty** function [retrieves a device property that is set for a device instance](retrieving-a-device-instance-property-value.md).

-   [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)

    The **SetupDiSetDeviceProperty** function [sets a device property for a device instance](setting-a-device-instance-property-value.md).
    
> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/). See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

For information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000, see [Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md).

 

