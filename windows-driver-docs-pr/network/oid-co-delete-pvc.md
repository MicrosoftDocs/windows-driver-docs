---
title: OID_CO_DELETE_PVC
ms.topic: reference
description: This topic describes the OID_CO_DELETE_PVC object identifier (OID).
keywords:
- OID_CO_DELETE_PVC
ms.date: 11/03/2017
---

# OID_CO_DELETE_PVC

The OID_CO_DELETE_PVC OID is sent by a client to a call manager to delete a permanent virtual connection (PVC) from the call manager's list of configured PVCs. The PVC is formatted as a CO_PVC structure, defined as follows:

```c++
typedef struct _CO_PVC {
    NDIS_HANDLE             NdisAfHandle;
    CO_SPECIFIC_PARAMETERS  PvcParameters;
} CO_PVC, *PCO_PVC;
``` 

The members of this structure contain the following information:

**NdisAfHandle**  
Specifies the NDIS-supplied handle returned by [NdisClOpenAddressFamilyEx](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclopenaddressfamilyex).

**PvcParameters**  
A formatted [CO_SPECIFIC_PARAMETERS](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisclopenaddressfamilyex) structure. This structure contains protocol-specific parameters that describe the PVC.

A PVC is removed manually by an administrator. A client that monitors such activity notifies a call manager of a PVC that has been removed by sending this OID to the call manager.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)
