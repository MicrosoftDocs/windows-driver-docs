---
title: MbbDeviceInitialize
description: 
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

This method initilizes the newly created NETADAPTER to MbbCx

## Syntax

```C++
NTSTATUS
MbbDeviceInitialize(
    _In_ NETADAPTER Adapter
);
```

## Parameters

*Adapter* [in]  
A handle to a NetAdapterCx NETADAPTER object previously created by NetAdapterCreate.

## Return value
This method might return failure in low resource situation

## Remarks
The client driver must calls this method from whithin EvtMbbDeviceCreateAdapter. For more information, see [**Creating the NetAdapter interface for the PDP context/EPS bearer**](writing-an-mbbcx-client-driver.md#creating-the-netadapter-interface-for-the-pdp-contexteps-bearer).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |