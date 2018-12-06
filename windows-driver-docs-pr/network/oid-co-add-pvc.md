---
title: OID_CO_ADD_PVC
description: This topic describes the OID_CO_ADD_PVC object identifier (OID).
ms.assetid: 182d5bdb-9cfe-4e9c-a2cf-4d5440bfdb76
keywords:
- OID_CO_ADD_PVC
ms.date: 11/03/2017
ms.localizationpriority: medium
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

