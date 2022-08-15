---
title: About storage filter drivers
description: Storage Filter Drivers
keywords:
- storage filter drivers WDK
- filter drivers WDK storage
- storage drivers WDK , filter drivers
- SFD WDK storage
ms.date: 03/24/2022
---

# About storage filter drivers

A storage filter driver (SFD) supports device-specific functionality not provided by a system-supplied [storage class driver](introduction-to-storage-class-drivers.md).

If a storage class driver already exists for a particular type of device, it might be unnecessary to write a driver for a new device of the same type. Each system-supplied storage class driver is designed to support peripheral devices of a given type and is tested against a number of vendors' devices. Thus, any system-supplied storage class driver might provide all the support another device of its type needs.

If an existing storage class driver does not fully support a new device of its type, a new driver can be written as an SFD layered over or under an existing system-supplied class driver. An SFD might transform data in read/write requests, define additional I/O control codes (IOCTLs) that enable a user application to take advantage of additional features of a particular device, or work around device-specific problems without requiring hardware-specific changes to the generic class or port drivers.

Unless a new device requires that every request be handled in a device-specific manner, a storage filter driver can be developed in far less time than a new storage class driver.
