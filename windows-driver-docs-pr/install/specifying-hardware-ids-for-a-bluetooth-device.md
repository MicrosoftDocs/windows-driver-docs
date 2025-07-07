---
title: Specifying Hardware IDs for a Bluetooth Device
description: Specifying Hardware IDs for a Bluetooth device
ms.date: 06/19/2025
ms.topic: concept-article
---

# Specifying Hardware IDs for a Bluetooth device

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

To specify [hardware IDs](hardware-ids.md) for a Bluetooth device within a device metadata package, the device must support the Device Identification (DID) Profile. Otherwise, the operating system cannot select and load the most appropriate device metadata package for the Bluetooth device. We highly recommend that all Bluetooth devices support the DID profile.

For more information about the DID Profile, refer to the [Bluetooth Device Identification Profile specification version 1.3](https://go.microsoft.com/fwlink/p/?linkid=145536).

For information about supporting Bluetooth Low Energy (LE) Device IDs, refer to the [Device Information Service version 1.1](https://go.microsoft.com/fwlink/p/?linkid=242771).
