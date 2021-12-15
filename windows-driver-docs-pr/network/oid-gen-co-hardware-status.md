---
title: OID_GEN_CO_HARDWARE_STATUS
description: This topic describes the OID_GEN_CO_HARDWARE_STATUS object identifier (OID).
keywords:
- OID_GEN_CO_HARDWARE_STATUS
ms.date: 11/02/2017
---

# OID_GEN_CO_HARDWARE_STATUS

The OID_GEN_CO_HARDWARE_STATUS OID specifies the current hardware status of the underlying NIC, as one of the following NDIS_HARDWARE_STATUS-type values:

**NdisHardwareStatusReady**  
Available and capable of sending and receiving data over the wire.

**NdisHardwareStatusInitializing**  
Initializing.

**NdisHardwareStatusReset**  
Resetting.

**NdisHardwareStatusClosing**  
Closing.

**NdisHardwareStatusNotReady**  
Not ready.

## Requirements

**Version**: Windows Vista and later
**Header**: Ntddndis.h (include Ndis.h)

