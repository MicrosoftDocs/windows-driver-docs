---
title: Accessing Device Class Properties
description: Accessing Device Class Properties
ms.assetid: 51eef1f4-ca7d-46ab-a33f-be53de277541
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Class Properties


In Windows Vista and later versions of Windows, applications and installers can access [device setup class properties](https://msdn.microsoft.com/library/windows/hardware/ff542239) and [device interface class properties](https://msdn.microsoft.com/library/windows/hardware/ff541406) by calling the following SetupAPI functions:

-   [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091) and [**SetupDiGetClassPropertyKeysEx**](https://msdn.microsoft.com/library/windows/hardware/ff551093)

    The **SetupDiGetClassPropertyKeys** function retrieves an array of the class property keys that identify the class properties that are currently set for a device setup class or a device interface class on a local computer. The **SetupDiGetClassPropertyKeysEx** function performs the same operation on a local computer or a remote computer. For information about how to determine what properties are set for a device class, see [Determining Which Properties Are Set for a Device Class](determining-which-properties-are-set-for-a-device-class.md).

-   [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

    The **SetupDiGetClassProperty** function [retrieves a class property](retrieving-a-device-class-property-value.md) for a device setup class or a device interface class. The [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) function performs the same operation on a local computer as it does on a remote computer.

-   [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128)

    The **SetupDiSetClassProperty** function [sets a class property for a device setup class or a device interface class](setting-a-device-class-property-value.md). The [**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132) function performs the same operation on a local computer as it does on a remote computer.

For information about how to access device class properties on Windows Server 2003, Windows XP, and Windows 2000, see [Accessing Device Setup Class Properties](accessing-device-setup-class-properties.md) and [Accessing Device Interface Class Properties](accessing-device-interface-class-properties.md).

 

 





