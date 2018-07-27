---
title: MbbRequestGetActivityId
description: Client drivers can call the MbbRequestGetCorrelationId method to correlate a pair of send and receive requests that exchange MBIM control messages between the MBBCx framework and the client driver.
ms.assetid: E6718686-A54A-42C2-BE1D-BA33AB9EE4F9
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetCorrelationId, MBBCx MbbRequestGetCorrelationId
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MbbRequestGetCorrelationId

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

Client drivers can call the **MbbRequestGetCorrelationId** method to correlate a pair of send and receive requests that exchange MBIM control messages between the MBBCx framework and the client driver.

## Syntax

```C++
LPCGUID
MbbRequestGetActivityId(
    _In_ MBBREQUEST Request
);
```

## Parameters

*Request* [in]  
A handle to the framework object that represents a request from the MBBCx framework, either to send a MBIM control command message to the device or to receive an MBIM control response message from the device.

## Return value

A GUID value.

The GUID's purpose is similar to the *TransactionId* field of the MBIM message header defined in the MBIM specification. The MBBCx framework provides this value, so the client driver is not required to parse the MBIM message if some sort of correlation is needed. 

## Remarks

The MBBCx framework calls into the client driver to issue an MBIM command message, and later calls into the client driver again to retreive the response message for that command. The GUID value returned for both calls will be the same, and it would only change if a new command and response message pair is requested.

Sometimes, the command and response message pair may get fragemented due to size limitations. In that case, all fragments from the same pair will have the same GUID value.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
