---
title: MbbDeviceInitialize
description: The MbbDeviceInitialize method initializes a newly created NETADAPTER object for MBBCx.
ms.assetid: DDB50DBD-B52D-4212-99CC-167E2014B29E
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceInitialize, MBBCx MbbDeviceInitialize
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceInitialize

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MbbDeviceInitialize** method initializes a newly created NETADAPTER object for MBBCx.

## Syntax

```C++
NTSTATUS
MbbDeviceInitialize(
    _In_ NETADAPTER Adapter
);
```

## Parameters

*Adapter* [in]  
A handle to a NetAdapterCx NETADAPTER object obtained in a previous call to [**NetAdapterCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptercreate).

## Return value

Returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate NTSTATUS error code.

This method might return failure in low resource situations.

## Remarks

The client driver must call this method from within [*EvtMbbDeviceCreateAdapter*](evt-mbb-device-create-adapter.md). 

For more information, see [**Creating the NetAdapter interface for the PDP context/EPS bearer**](writing-an-mbbcx-client-driver.md#creating-the-netadapter-interface-for-the-pdp-contexteps-bearer).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |