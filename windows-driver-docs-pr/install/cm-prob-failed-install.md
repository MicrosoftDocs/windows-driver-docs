---
title: CM_PROB_FAILED_INSTALL
description: CM_PROB_FAILED_INSTALL
ms.assetid: d65f1f14-e455-4902-8168-38d8ae51f81f
keywords:
- CM_PROB_FAILED_INSTALL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CM_PROB_FAILED_INSTALL

This function is reserved for system use.

The device's drivers are not installed.

## Error Code

28

### Display Message

"The drivers for this device are not installed. (Code 28)"

### Recommended Resolution

Please visit the website of the company that manufactures the device and look for the most recent drivers for this device.


## For driver developers

The [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md) property on the device should indicate the failure code.

### 0xC0000490 - STATUS_PNP_NO_COMPAT_DRIVERS

PNP could not find a driver for the device.

1. Identify which driver you expected to be on the device. Is that driver on the system?
2. Does that driver actually match the device in question on the architecture being used and on the OS being used?

Examine the hardware and compatible IDs of the device in question and compare it to the ID(s) that the INF matches on. If there are not any exact string matches, the driver doesn't match.
Look for the [**Models sections**](inf-models-section.md) in the INF. Make sure that the **TargetOSVersion** part of the Models section name applies to the architecture and OS version you are running on.

### 0xC0000491 - STATUS_PNP_DRIVER_PACKAGE_NOT_FOUND

The INF that matched on the device uses Include/Needs and includes an INF that is not present.

### 0xC0000492 - STATUS_PNP_DRIVER_CONFIGURATION_NOT_FOUND

Can occur if Include/Needs is used improperly by the INF that matches on the device. For example, the INF specifies a section in Needs that does not exist in any INF that it specifies in an Include section.

### 0xC0000493 - STATUS_PNP_DRIVER_CONFIGURATION_INCOMPLETE

The INF that matched on the device has not been pre-configured and thus cannot be configured onto that device at this point for one or more of the following reasons:

1. The INF is not configurable, meaning it does not meet the [Universal INF requirements](using-a-universal-inf-file.md).
2. The INF belongs to a device setup class that is not configurable. In this case, the ClassGuid specified by the INF still depends on a class installer.
3. The INF belongs to a device setup class that is not boot critical. Because drivers belonging to the ClassGuid specified by the INF are not needed to boot the system, they may not be installed until user-mode is available.
4. The INF was added during runtime (as opposed to offline imaging) and has not been pre-configured yet. A possible scenario is that the INF was recently ownloaded from Windows Update and added to the driver store and is in the process of being installed on applicable devices. Devices may transiently pass through this problem state during installation.

### 0xC0000494 - STATUS_PNP_FUNCTION_DRIVER_REQUIRED

PnP requires that an INF that is installed on the device must have an [**AddService directive**](inf-addservice-directive.md) that sets an associated service (or function driver) or must use Include/Needs to reference a system-supplied driver that in turn sets an associated service on this device. To set an associated service, there must be an **AddService directive** for which the flag SPSVCINST_ASSOCSERVICE (0x00000002) is set.

### Upgrade to Windows 10

Before upgrade, the device has a driver and is working fine. After upgrade, it shows Code 28. This is frequently caused by the driver package being excluded from the migration.
