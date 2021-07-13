---
title: Percent of machines reporting successful firmware installation from ESRT
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of successful installs over attempts
ms.topic: article
ms.date: 06/23/2021
ms.localizationpriority: medium
---
 
# Percent of machines reporting successful firmware installation from ESRT

## Description

The measure aggregates telemetry from a 28-day sliding window into a ratio of successful installs over attempts. A successful installation is defined when the following events happen:

1. Firmware with device instance starting with UEFI is installed via drvinst.
2. Machine reboots and firmware is applied.
3. UEFI.sys reports a successful installation upon boot.

If the machine is reports a transient error (listed below) then it is not included in the population.

|Error Code|Value|
|----|----|
|3221225659| STATUS_NOT_SUPPORTED|
|3221226195| STATUS_POWER_STATE_INVALID|
|3221226206| STATUS_INSUFFICIENT_POWER|
|3221225506| STATUS_ACCESS_DENIED|
|3221225473| STATUS_UNSUCCESSFUL|
|3221225517| STATUS_NOT_COMMITTED|
|3221225560| STATUS_UNKNOWN_REVISION|
|3221225626| STATUS_INSUFFICIENT_RESOURCES|
|3221226194| STATUS_PNP_REBOOT_REQUIRED|
|3221225659| STATUS_NOT_SUPPORTED|
|3221226195| STATUS_POWER_STATE_INVALID|
|3221226206| STATUS_INSUFFICIENT_POWER|
|3221225862| STATUS_DEVICE_PROTOCOL_ERROR|
|3221226681| STATUS_UNSATISFIED_DEPENDENCIES|
|3221226029| STATUS_RETRY|

STATUS_INVALID_IMAGE_FORMAT is a result of the firmware returning invalid image format in the last attempt status of the [ESRT table](../bringup/esrt-table-definition.md). This code is returned from the firmware, saying that the new firmware itself has a error. Windows can't help because the capsule update process is entirely platform code and is done outside of the operating system.

The firmware team has open-sourced multiple ways to record information about why a firmware process may have failed such that the information can be retrieved on the next boot of the operating system. These are:

LastAttemptStatus:
- This works well if you're already using the FmpDevicePkg to build your firmware-based capsule drivers.
- [Fmp Dxe - Project Mu](https://microsoft.github.io/mu/dyn/mu_tiano_plus/FmpDevicePkg/FmpDxe/ReadMe/)
- [FmpDeviceSetImageWithStatus](https://github.com/tianocore/edk2/blob/5531fd48ded1271b8775725355ab83994e4bc77c/FmpDevicePkg/Include/Library/FmpDeviceLib.h#L578)

Mu WHEA Telemetry:
- This is an add-on to EDK2-based and Mu-based firmware that will handle telemetry reporting in a way that is automatically picked up by the operating system.
- [mu_plus/MsWheaPkg at release/202102 · microsoft/mu_plus · GitHub](https://github.com/microsoft/mu_plus/tree/release/202102/MsWheaPkg)

No matter what you choose, there is a cost to instrumenting systems to gather more information. Windows can't help because the capsule update process is entirely platform code and is done outside the operating system.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|>= 95%|
|**Measure ID**|23260700|

## Calculation

number of machines that were successful / 
number of machines that attempted a firmware device but excludes machines in a transient state