---
title: MbbAdapterGetSessionId
description: The MbbAdapterGetSessionId method retreives the data Session ID represented by the given NETADAPTER object.
ms.assetid: 17E57322-5161-49B5-9C85-86C771CB5B19
keywords:
- Mobile Broadband WDF Class Extension MbbAdapterGetSessionId, MBBCx MbbAdapterGetSessionId
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbAdapterGetSessionId

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MbbAdapterGetSessionId** method retreives the data Session ID represented by the given NETADAPTER object.

## Syntax

```C++
ULONG
MbbAdapterGetSessionId(
    _In_ NETADAPTER Adapter
);
```

## Parameters

*Adapter* [in]  
A handle to a NetAdapterCx NETADAPTER object previously created with a call to [**NetAdapterCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptercreate) and initialized with [**MbbAdapterInitialize**](mbbadaptergetsessionid.md).

## Return value

The data session's ID to the network interface represented by the NETADAPTER object.

## Remarks

The client driver must call [**MbbAdapterInitialize**](mbbadaptergetsessionid.md) first before calling this method. 

For more information, see [**Creating the NetAdapter interface for the PDP context/EPS bearer**](writing-an-mbbcx-client-driver.md#creating-the-netadapter-interface-for-the-pdp-contexteps-bearer).


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |