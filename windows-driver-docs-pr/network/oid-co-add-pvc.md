---
title: OID_CO_ADD_PVC
author: windows-driver-content
description: This topic describes the OID_CO_ADD_PVC object identifier (OID).
ms.assetid: 182d5bdb-9cfe-4e9c-a2cf-4d5440bfdb76
keywords:
- OID_CO_ADD_PVC
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_ADD_PVC

The OID_CO_ADD_PVC OID is sent by a client to a call manager to add a permanent virtual connection (PVC) to the call manager's list of configured PVCs. The PVC is formatted as a CO_PVC structure, defined as follows:

```c++
typedef struct _CO_PVC {
    NDIS_HANDLE             NdisAfHandle;
    CO_SPECIFIC_PARAMETERS  PvcParameters;
} CO_PVC, *PCO_PVC;
```

The members of this structure contain the following information:

**NdisAfHandle**  
Specifies the NDIS-supplied handle returned by [NdisClOpenAddressFamilyEx](https://msdn.microsoft.com/library/windows/hardware/ff561639).

**PvcParameters**  
A formatted [CO_SPECIFIC_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff545396) structure. This structure contains protocol-specific parameters that describe the PVC.

A PVC is configured manually by an administrator. A client that monitors such activity notifies a call manager of a newly configured PVC by sending this OID to the call manager. Other clients can then use the newly-configured PVC.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")