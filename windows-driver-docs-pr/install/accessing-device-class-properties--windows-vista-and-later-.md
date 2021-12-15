---
title: Accessing Device Class Properties
description: Accessing Device Class Properties
ms.date: 04/20/2017
---

# Accessing Device Class Properties


In Windows Vista and later versions of Windows, applications and installers can access [device setup class properties](/previous-versions/ff542239(v=vs.85)) and [device interface class properties](/previous-versions/ff541406(v=vs.85)) by calling the following SetupAPI functions:

-   [**SetupDiGetClassPropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeys) and [**SetupDiGetClassPropertyKeysEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeysexw)

    The **SetupDiGetClassPropertyKeys** function retrieves an array of the class property keys that identify the class properties that are currently set for a device setup class or a device interface class on a local computer. The **SetupDiGetClassPropertyKeysEx** function performs the same operation on a local computer or a remote computer. For information about how to determine what properties are set for a device class, see [Determining Which Properties Are Set for a Device Class](determining-which-properties-are-set-for-a-device-class.md).

-   [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

    The **SetupDiGetClassProperty** function [retrieves a class property](retrieving-a-device-class-property-value.md) for a device setup class or a device interface class. The [**SetupDiGetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw) function performs the same operation on a local computer as it does on a remote computer.

-   [**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw)

    The **SetupDiSetClassProperty** function [sets a class property for a device setup class or a device interface class](setting-a-device-class-property-value.md). The [**SetupDiSetClassPropertyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyexw) function performs the same operation on a local computer as it does on a remote computer.

For information about how to access device class properties on Windows Server 2003, Windows XP, and Windows 2000, see [Accessing Device Setup Class Properties](accessing-device-setup-class-properties.md) and [Accessing Device Interface Class Properties](accessing-device-interface-class-properties.md).

 

