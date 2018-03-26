---
title: MbbDeviceInitConfig
description: The MBBDeviceInitConfig method initializes MBBCx device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.
ms.assetid: 6BB95F5C-0EB2-4006-9C18-C82B4FA40032
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceInitConfig, MBBCx MbbDeviceInitConfig
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceInitConfig

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MBBDeviceInitConfig** method initializes MBBCx device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.

## Syntax

```C++
NTSTATUS
MbbDeviceInitConfig(
    _Inout_ PWDFDEVICE_INIT DeviceInit
);
```

## Parameters

*DeviceInit* [in, out]  
A pointer to a **WDFDEVICE_INIT** object that the client received in its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) routine.

## Return value

Returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

## Remarks

The client driver calls this method in its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback after it calls [**NetAdapterDeviceInitConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdeviceinitconfig), but before it calls [*WdfDeviceCreate*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

For more information, see [**Initialize the device**](writing-an-mbbcx-client-driver.md#initialize-the-device).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |