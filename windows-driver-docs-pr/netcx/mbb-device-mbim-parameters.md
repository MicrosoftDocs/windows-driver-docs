---
title: MBB_DEVICE_MBIM_PARAMETERS
description: The client driver uses the MBB_DEVICE_MBIM_PARAMETERS structure to describe its MBIM specification-related parameters to the MBBCx framework.
ms.assetid: 90DDEB14-17EB-4B6A-B88E-257AAB2586DC
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_MBIM_PARAMETERS, MBBCx MBB_DEVICE_MBIM_PARAMETERS
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MBB_DEVICE_MBIM_PARAMETERS

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver uses the **MBB_DEVICE_MBIM_PARAMETERS** structure to describe its MBIM specification-related parameters to the MBBCx framework.

## Syntax

```C++
typedef struct _MBB_DEVICE_MBIM_PARAMETERS
{
    ULONG Size;

    MBB_MBIM_VERSION Version;
    ULONG MaximumFragmentSize;
} MBB_DEVICE_MBIM_PARAMETERS, *PMBB_DEVICE_MBIM_PARAMETERS;
```

## Members

**Size**  
The size of the **MBB_DEVICE_MBIM_PARAMETERS** structure, in bytes.

**Version**  
An [**MBB_MBIM_VERSION**](mbb-mbim-version.md) value that defines the version of the MBIM specification that the client driver supports. The value of this field must be **MBB_MBIM_VERSION1_0_ERRATA**.

> [!IMPORTANT]
> The client driver and device must support the MBIM specification Rev 1.0 Errata-1.

**MaximumFragmentSize**  
The maximum size of MBIM control messages that the client driver can support.

The MBBCx framework uses the value of this field to determine if it needs to fragment the MBIM message when it later calls into the client driver's [*EvtMbbDeviceSendMbimFragment*](evt-mbb-device-send-mbim-fragment.md) callback function to issue commands.

## Remarks

Call [**MBB_DEVICE_MBIM_PARAMETERS_INIT**](mbb-device-mbim-parameters-init.md) to intialize this structure.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
