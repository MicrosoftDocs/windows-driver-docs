---
title: MbbDeviceDisarmWake
description: 
ms.assetid: 268B5938-8845-4496-BABB-C84BA6B796B5
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceDisarmWake, MBBCx MbbDeviceDisarmWake
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceDisarmWake

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MbbDeviceDisarmWake** method is called by client drivers to disarm their device wakeup using MBIM messages.

## Syntax

```C++
VOID
MbbDeviceDisarmWake(
    _In_ WDFDEVICE Device
);
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

## Return value

This method does not return a value.

## Remarks

This is an optional method for client drivers that want to disarm their device wakeup using MBIM messages. If a client driver does not use MBIM messages for wakeup, it can instead use the NETPOWERSETINGS object [like other types of NetAdapterCx client drivers](https://docs.microsoft.com/windows-hardware/drivers/netcx/configuring-power-management).

This method must be called either from [*EvtDeviceDisarmWakeFromS0*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0) or [*EvtDeviceDisarmWakeFromSx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx).

For more information, see [Power management of the MBB device](writing-an-mbbcx-client-driver.md#power-management-of-the-mbb-device).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |