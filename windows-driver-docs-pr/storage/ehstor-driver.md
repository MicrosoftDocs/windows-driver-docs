---
title: Enhanced Storage class driver
description: Learn more about ehstorclass.sys
keywords:
- Enhanced storage class driver, WDK
- ehstorclass.sys, WDK
ms.date: 03/24/2022
---

# Enhanced Storage class driver

The Enhanced Storage class driver (*ehstorclass.sys*) is a system-supplied lower disk filter driver that detects Enhanced Storage functionality using the [IEEE 1667 standard](https://standards.ieee.org/ieee/1667/6801/), and surfaces a separate management stack for each detected functionality. Currently, the functionality implemented in *ehstorclass* relates to security as defined by the [Trusted Computing Group (TCG) Opal specification](https://trustedcomputinggroup.org/resource/storage-work-group-storage-security-subsystem-class-opal).

One of *ehstorclass*'s Enhanced Storage capabilities is the ability to manage device-level security. Clients can use this functionality to enable and manage storage device built-in encryption and access control as defined by the IEEE 1667 standard.

A client sends IOCTLs defined in [ehstorioctl.h](/windows-hardware/drivers/ddi/ehstorioctl) to the *ehstorclass* driver for handling. Each enhanced storage function driver (that handles a silo) has its own specific set of IOCTLs. For the built-in security function, the IOCTLs are defined in [*ehstorbandmgmt.h*](/windows-hardware/drivers/ddi/ehstorbandmgmt/).

See [Enhanced Storage](/previous-versions/windows/desktop/enstor/enhanced-storage-portal) for more information.
