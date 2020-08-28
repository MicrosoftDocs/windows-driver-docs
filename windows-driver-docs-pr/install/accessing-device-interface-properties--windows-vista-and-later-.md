---
title: Accessing Device Interface Properties
description: Accessing Device Interface Properties
ms.assetid: 8a46816b-56c5-49e9-8250-9ede037ae2b5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Interface Properties


In Windows Vista and later versions of Windows, applications and installers can access [device interface properties](/previous-versions/ff541409(v=vs.85)) by calling the following SetupAPI functions:

-   [**SetupDiGetDeviceInterfacePropertyKeys**](/windows/desktop/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertykeys)

    The **SetupDiGetDeviceInterfacePropertyKeys** function retrieves an array of the device interface property keys that identify the device interface properties that are currently set for a device interface instance. For information about how to determine what properties are set for a device interface, see [Determining Which Properties are Set for a Device Interface](determining-which-properties-are-set-for-a-device-interface.md).

-   [**SetupDiGetDeviceInterfaceProperty**](/windows/desktop/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

    The **SetupDiGetDeviceInterfaceProperty** function [retrieves a device interface property](retrieving-a-device-interface-property-value.md) that is set for a device interface.

-   [**SetupDiSetDeviceInterfaceProperty**](/windows/desktop/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw)

    The **SetupDiSetDeviceInterfaceProperty** function [sets a device interface property](setting-a-device-interface-property-value.md) for a device interface.

For information about how to access device interface properties on Windows Server 2003, Windows XP, and Windows 2000, see Accessing Device Interface Properties.

 

