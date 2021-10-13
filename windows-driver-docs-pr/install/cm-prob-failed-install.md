---
title: CM_PROB_FAILED_INSTALL
description: CM_PROB_FAILED_INSTALL
keywords:
- CM_PROB_FAILED_INSTALL
ms.date: 02/28/2020
ms.localizationpriority: medium
---

# Code 28 - CM_PROB_FAILED_INSTALL

This Device Manager error message indicates that the device's drivers are not installed.

## Error Code

28

### Display Message

"The drivers for this device are not installed. (Code 28)"

### Recommended Resolution

Please visit the website of the company that manufactures the device and look for the most recent drivers for this device.


## For driver developers

The [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device should indicate the failure code.

### 0xC0000490 - STATUS_PNP_NO_COMPAT_DRIVERS

PnP could not find a compatible driver for the device. This failure is often referred to as a DNF (driver not found) problem.

Examine the hardware IDs and compatible IDs of the device in question and compare to the hardware ID(s) that the INF specifies under the [**Models sections**](inf-models-section.md).  Also make sure that the **TargetOSVersion** part of the Models section name applies to the architecture and OS version you are running on.

### 0xC0000491 - STATUS_PNP_DRIVER_PACKAGE_NOT_FOUND

This code indicates a missing driver package dependency.

Specifically, the INF that matched on the device uses **Include** entries in the [INF DDInstall section](inf-ddinstall-section.md) to specify a Microsoft-supplied INF that is not present in this version of Windows.

### 0xC0000492 - STATUS_PNP_DRIVER_CONFIGURATION_NOT_FOUND

This code also indicates a missing driver package dependency.

In this case, the INF that matched on the device uses **Needs** entries in the [INF DDInstall section](inf-ddinstall-section.md) to specify a section that does not exist in any Microsoft-supplied INF referenced by an **Include** directive.

### 0xC0000494 - STATUS_PNP_FUNCTION_DRIVER_REQUIRED

This failure occurs when the INF does not specify an associated function driver service.

Verify that either:

1. The INF file for the device being installed contains an [**AddService directive**](inf-addservice-directive.md) that sets an associated service or function driver using the flag SPSVCINST_ASSOCSERVICE (0x00000002).
2. The INF file specifies **Include** or **Needs** entries in a [INF DDInstall Section](inf-ddinstall-section.md) that reference a system-supplied driver that in turn sets an associated service on the device.

### Upgrade to Windows 10

Before upgrade, the device has a driver and is working fine. After upgrade, it shows Code 28. This is frequently caused by the driver package being excluded from the migration.
