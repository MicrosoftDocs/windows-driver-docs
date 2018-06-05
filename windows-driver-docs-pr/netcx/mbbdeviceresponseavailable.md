---
title: MbbDeviceResponseAvailable
description: A client driver calls the MbbDeviceResponseAvailable method when there is an MBIM control message ready from the device, as the response to a previous MBIM control message sent to the device from the MBBCx framework.

ms.assetid: A8BECE96-3845-4A9D-BA36-50A2666E52E1
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceResponseAvailable, MBBCx MbbDeviceResponseAvailable
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceResponseAvailable

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

A client driver calls the **MbbDeviceResponseAvailable** method when there is an MBIM control message ready from the device, as the response to a previous MBIM control message sent to the device from the MBBCx framework.

It can also call this method to notify the MBBCx framework of an unsolicited device event.

## Syntax

```C++
VOID
MbbDeviceResponseAvailable(
    _In_ WDFDEVICE Device
);
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

## Return value

This method does not return a value.

## Remarks

For more information, see [**Handling MBIM control messages**](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |