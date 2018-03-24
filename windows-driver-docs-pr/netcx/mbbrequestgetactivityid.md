---
title: MbbRequestGetActivityId
description: 
ms.assetid: E6718686-A54A-42C2-BE1D-BA33AB9EE4F9
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetActivityId, MBBCx MbbRequestGetActivityId
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestGetActivityId

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
A handle to the framework object which represents a request from MbbCx framework, either to send a MBIM control message to the device, or receive a MBIM response message from the device.

## Return value
A GUID value.

Its purpose is similar to the *TransactionId* field of MBIM message header defined in MBIM specification. The MbbCx framework provides this value, so the client driver is not required to parse the MBIM message if some sorts of corrletion are needed. 

## Remarks
The MbbCx framework calls into the client driver to issue an MBIM message command, and later calls into the client again to retreive the response resulted from that command. The GUID value returned for both calls will be the same. The GUID value would change if a new command and response are requested.

Sometime the command and the response message maybe fragemented due to size limitation, in that case, all fragmented message will have the same GUID value.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |