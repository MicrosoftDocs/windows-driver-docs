---
title: Reading Device Metadata
description: Reading Device Metadata
ms.date: 08/13/2021
ms.localizationpriority: medium
---

# Reading Device Metadata

WIA minidrivers for web services scanners must read the following device metadata properties at run time:

**PKEY_PNPX_ServiceId**
This property is needed to initialize the [**WIA_DPS_SERVICE_ID**](./wia-dps-service-id.md) WIA property.

**PKEY_PNPX_GlobalIdentity**
This property initializes the [**WIA_DPS_GLOBAL_IDENTITY**](./wia-dps-global-identity.md) WIA property.

**PKEY_PNPX_ID**
This property initializes the [**WIA_DPS_DEVICE_ID**](./wia-dps-device-id.md) device property.

> [!NOTE]
> Accessed directly or indirectly by using [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname)

The minidrivers might also read other properties, including the following:

**PKEY_PNPX_FIRMWARE_VERSION**
This property initializes the [**WIA_DPA_FIRMWARE_VERSION**](./wia-dpa-firmware-version.md) WIA property.

> [!NOTE]
> Minidrivers that use *WSDScan.sys* can also retrieve the PNPX ID value by calling [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname); the returned device path is the current PKEY_PNPX_ID.

For a description of these PKEY_PNPX_*Xxx* properties, see the [PNP-X Implementer's Guide (DOC download)](https://download.microsoft.com/download/5/D/6/5D6EAF2B-7DDF-476B-93DC-7CF0072878E6/PnP-X_imp.doc).

The following code examples show how to open a Property Store for the current Function Instance object that is obtained as described in the previous section and how to read device properties from the store:

[Code Example for Opening a Property Store](code-example-for-opening-a-property-store.md)

[Code Example for Reading Device Properties](code-example-for-reading-device-properties.md)

[Code Example for Initializing Device Properties](code-example-for-initializing-device-properties.md)
