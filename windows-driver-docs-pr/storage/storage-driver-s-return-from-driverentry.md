---
title: Storage Driver's Return from DriverEntry
description: Storage Driver's Return from DriverEntry
keywords:
- return values WDK SCSI
- ScsiPortInitialize
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# Storage Driver's Return from DriverEntry

When [**ScsiPortInitialize**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportinitialize) returns control, the [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) routine propagates the return value of **ScsiPortInitialize** when **DriverEntry** itself returns control.

If a miniport driver calls **ScsiPortInitialize** more than once, its **DriverEntry** routine *must propagate thelowest value* returned by **ScsiPortInitialize**. A miniport driver writer cannot make any assumptions about the values returned by **ScsiPortInitialize**.
