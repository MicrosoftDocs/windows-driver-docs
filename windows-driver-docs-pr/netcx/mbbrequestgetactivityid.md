---
title: MbbRequestGetActivityId
description: 
ms.assetid: E6718686-A54A-42C2-BE1D-BA33AB9EE4F9
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetCorrelationId, MBBCx MbbRequestGetCorrelationId
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestGetCorrelationId

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver can use this method to correlate a pair of send and receive requests that exchanges MBIM control message between the MbbCx framework and the client driver

## Syntax

```C++
LPCGUID
MbbRequestGetActivityId(
    _In_ MBBREQUEST Request
);
```

## Parameters

*Request* [in]  
A handle to the framework object which represents a request from MbbCx framework, either to send a MBIM control command message to the device, or receive a MBIM control response message from the device.

## Return value
A GUID value.

Its purpose is similar to the *TransactionId* field of MBIM message header defined in MBIM specification. The MbbCx framework provides this value, so the client driver is not required to parse the MBIM message if some sorts of corrletions are needed. 

## Remarks
The MbbCx framework calls into the client driver to issue an MBIM command message, and later calls into the client driver again to retreive the response message for that command. The GUID value returned for both calls will be the same, and it would only change if a new pair of command and response are requested.

Sometime the pair of the command and response message may get fragemented due to size limitation, in that case, all fragmented from the same pair will have the same GUID value.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |