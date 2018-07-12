---
title: EVT_MBB_DEVICE_CREATE_ADAPTER
description: The EvtMbbDeviceCreateAdapter callback function is implemented by the client driver to create a NETADAPTER object for a data session.
ms.assetid: 42F04BBD-22B5-45B2-A158-FE52E07104CD
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_CREATE_ADAPTER, MBBCx EVT_MBB_DEVICE_CREATE_ADAPTER
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EVT_MBB_DEVICE_CREATE_ADAPTER

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The *EvtMbbDeviceCreateAdapter* callback function is implemented by the client driver to create a NETADAPTER object for a data session.

## Syntax

```C++
EVT_MBB_DEVICE_CREATE_ADAPTER EvtMbbDeviceCreateAdapter;

NTSTATUS
EvtMbbDeviceCreateAdapter(
    _In_ WDFDEVICE Device,
    _In_ PNETADAPTER_INIT AdapterInit
)
{ ... }

typedef EVT_MBB_DEVICE_CREATE_ADAPTER *PFN_MBB_DEVICE_CREATE_ADAPTER;
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*AdapterInit* [in]  
A NETADAPTER_INIT object that describes the initialization information for the NETADAPTER.

## Return value

This callback function returns STATUS_SUCCESS if the operation was successful. Otherwise, it returns an appropriate NTSTATUS error code.

## Remarks

In this callback, the client driver creates a NETADAPTER object that is used by MBBCx to represent the network interface for a data session. MBBCx invokes this callback function at least once to establish the primary PDP context/default EPS bearer, then it might invoke it more times, once for every data session to be established.

For more information and a code example, see [Creating the NetAdapter interface for the PDP context/EPS bearer](writing-an-mbbcx-client-driver.md#creating-the-netadapter-interface-for-the-pdp-contexteps-bearer).


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |