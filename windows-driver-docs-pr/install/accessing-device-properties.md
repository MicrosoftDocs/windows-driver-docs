---
title: Accessing device properties
description: Provides information about accessing device properties.
keywords:
- device properties WDK device installations , accessing
- accessing device properties WDK device installations
ms.date: 08/15/2022
---

# Accessing device properties

You must not discover or change [device properties](device-properties.md) by directly accessing registry keys. Registry keys do not contain required information to discover or change device properties. In addition, the location, format, and meaning of these keys might change between different versions of Windows.

The [SetupAPI](setupapi.md) and [configuration manager](/windows/win32/api/cfgmgr32/) functions provide consistent behavior and enforce access permissions to protect device properties. To safely access device properties, follow these guidelines:

- For user-mode applications, follow these steps:

    1. For information about accessing device instance properties on Windows Vista and later versions of Windows, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

        Starting with Windows Vista, some device properties are reserved by the operating system. For more information, see [Rules for Modifying Device Properties](modifying-device-properties.md).

    1. For information about accessing device instance properties on Windows 2000, Windows XP, and Windows Server 2003, see [Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md).

- For kernel-mode drivers, follow these steps:

    1. On Windows Vista and later versions of Windows, use [**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata) and [**IoSetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata) to access device properties.

    1. On Windows 2000, Windows XP, and Windows Server 2003, use [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty) to access device properties.
