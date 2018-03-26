---
title: MBB_DEVICE_MBIM_PARAMETERS
description: 
ms.assetid: 90DDEB14-17EB-4B6A-B88E-257AAB2586DC
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_MBIM_PARAMETERS, MBBCx MBB_DEVICE_MBIM_PARAMETERS
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_DEVICE_MBIM_PARAMETERS

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver uses this structure to describe its MBIM specification related parameters to the MbbCx framework

## Syntax

```C++
typedef enum _MBB_MBIM_VERSION {
    MBB_MBIM_VERSION1_0 = 0,
    MBB_MBIM_VERSION1_0_ERRATA,
} MBB_MBIM_VERSION;

typedef struct _MBB_DEVICE_MBIM_PARAMETERS
{
    ULONG Size;

    MBB_MBIM_VERSION Version;
    ULONG MaximumFragmentSize;
} MBB_DEVICE_MBIM_PARAMETERS, *PMBB_DEVICE_MBIM_PARAMETERS;
```

## Members

**Size**  
Size of the **MBB_DEVICE_MBIM_PARAMETERS** structure

**Version**  
The version of MBIM specification that the client driver supports. The value of this field must be *MBB_MBIM_VERSION1_0_ERRATA*.

The client driver and device must support MBIM specification Rev 1.0 Errata-1

**MaximumFragmentSize**  
The maximum size of the MBIM control message the client driver can support.

The MbbCx framework uses the value of this field to determine if it needs to fragment the MBIM message when later it calls into the client driver's [**EvtMbbDeviceSendMbimFragment**](evt-mbb-device-send-mbim-fragment.md) callback functions to issue command.  

## Remarks
Call [**MBB_DEVICE_MBIM_PARAMETERS_INIT**](mbb-device-mbim-parameters-init.md) to intialize this structure.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |