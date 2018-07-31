---
title: MbbDeviceInitialize
description: The MbbDeviceInitialize method registers the client driver's MBB-specific callback functions.
ms.assetid: C5319566-7A3D-475F-A38C-9EAC9C40495A
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceInitialize, MBBCx MbbDeviceInitialize
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MbbDeviceInitialize

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MbbDeviceInitialize** method registers the client driver's MBB-specific callback functions.

## Syntax

```C++
NTSTATUS
MbbDeviceInitialize(
    _In_ WDFDEVICE Device,
    _In_ PMBB_DEVICE_CONFIG Config
);
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*Config* [in]  
A pointer to a client driver-allocated and initialized [**MBB_DEVICE_CONFIG**](mbb-device-config.md) structure.

## Return value

Returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

This method might return failure in low resource situations.

## Remarks

The client driver must call this method after it calls [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate) from within [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add). 

For more information, see [**Initialize the device**](writing-an-mbbcx-client-driver.md#initialize-the-device).


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
