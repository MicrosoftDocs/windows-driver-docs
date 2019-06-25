---
title: Reading Device Metadata
description: Reading Device Metadata
ms.assetid: 402de9de-8bfe-4cc2-9b8e-06e0ad925eb1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading Device Metadata


WIA minidrivers for web services scanners must read the following device metadata properties at run time:

<a href="" id="pkey-pnpx-serviceid"></a>**PKEY\_PNPX\_ServiceId**  
This property is needed to initialize the [**WIA\_DPS\_SERVICE\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-service-id) WIA property.

<a href="" id="pkey-pnpx-globalidentity"></a>**PKEY\_PNPX\_GlobalIdentity**  
This property initializes the [**WIA\_DPS\_GLOBAL\_IDENTITY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-global-identity) WIA property.

<a href="" id="pkey-pnpx-id--directly-or-indirectly-by-using-istidevicecontrol--getmydeviceportname-"></a>**PKEY\_PNPX\_ID** (directly or indirectly by using [**IStiDeviceControl::GetMyDevicePortName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname))  
This property initializes the [**WIA\_DPS\_DEVICE\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dps-device-id) device property.

The minidrivers might also read other properties, including the following:

<a href="" id="pkey-pnpx-firmware-version"></a>**PKEY\_PNPX\_FIRMWARE\_VERSION**  
This property initializes the [**WIA\_DPA\_FIRMWARE\_VERSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-dpa-firmware-version) WIA property.

**Note**   Minidrivers that use *WSDScan.sys* can also retrieve the PNPX ID value by calling [**IStiDeviceControl::GetMyDevicePortName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname); the returned device path is the current PKEY\_PNPX\_ID.

 

For a description of these PKEY\_PNPX\_*Xxx* properties, see the [PNP-X Implementer's Guide](https://go.microsoft.com/fwlink/p/?linkid=242570).

The following code examples show how to open a Property Store for the current Function Instance object that is obtained as described in the previous section and how to read device properties from the store:

[Code Example for Opening a Property Store](code-example-for-opening-a-property-store.md)

[Code Example for Reading Device Properties](code-example-for-reading-device-properties.md)

[Code Example for Initializing Device Properties](code-example-for-initializing-device-properties.md)

 

 




