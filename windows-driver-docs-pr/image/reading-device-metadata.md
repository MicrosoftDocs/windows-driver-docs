---
title: Reading Device Metadata
description: Reading Device Metadata
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# Reading Device Metadata

WIA minidrivers for web services scanners must read the following device metadata properties at run time:

**PKEY\_PNPX\_ServiceId**

This property is needed to initialize the [**WIA\_DPS\_SERVICE\_ID**](./wia-dps-service-id.md) WIA property.

**PKEY\_PNPX\_GlobalIdentity**

This property initializes the [**WIA\_DPS\_GLOBAL\_IDENTITY**](./wia-dps-global-identity.md) WIA property.

**PKEY\_PNPX\_ID**

This property initializes the [**WIA\_DPS\_DEVICE\_ID**](./wia-dps-device-id.md) device property.

> [!NOTE]
> Accessed directly or indirectly by using [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname)

The minidrivers might also read other properties, including the following:

**PKEY\_PNPX\_FIRMWARE\_VERSION**

This property initializes the [**WIA\_DPA\_FIRMWARE\_VERSION**](./wia-dpa-firmware-version.md) WIA property.

> [!NOTE]
> Minidrivers that use *WSDScan.sys* can also retrieve the PNPX ID value by calling [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname); the returned device path is the current PKEY\_PNPX\_ID.

For a description of these PKEY\_PNPX\_*Xxx* properties, see the [PNP-X Implementer's Guide (DOC download)](https://go.microsoft.com/fwlink/p/?linkid=242570).

The following code examples show how to open a Property Store for the current Function Instance object that is obtained as described in the previous section and how to read device properties from the store:

[Code Example for Opening a Property Store](code-example-for-opening-a-property-store.md)

[Code Example for Reading Device Properties](code-example-for-reading-device-properties.md)

[Code Example for Initializing Device Properties](code-example-for-initializing-device-properties.md)
