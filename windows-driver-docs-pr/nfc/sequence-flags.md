---
title: Sequence flags
description: The NFC CX defines the following constants for sequence events.
ms.assetid: AC6CE286-52F7-4FC9-9F38-CD10C1413A90
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
topic_type:
- apiref
api_name:
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_SKIP_CONFIG
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_FORCE_CONFIG
- NFC_CX_SEQUENCE_INIT_COMPLETE_FLAG_REDO
- NFC_CX_SEQUENCE_PRE_NFCEE_DISC_FLAG_SKIP
- NFC_CX_SEQUENCE_PRE_SHUTDOWN_FLAG_SKIP_RESET
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sequence flags


The NFC CX defines the following constants for sequence events.


### NFC\_CX\_SEQUENCE\_PRE\_INIT\_FLAG\_SKIP\_CONFIG

0x00000001

This flag is used in the pre-init sequence to skip configuration updates after NCI initialization. Note this flag cannot be used with force configuration option.

### NFC\_CX\_SEQUENCE\_PRE\_INIT\_FLAG\_FORCE\_CONFIG

0x00000002

This flag is used to force update configuration after NCI initialization. Typically, NFC CX only updates the configuration either if the controller doesn’t support KEEP CONFIG or if the configuration has changed after a driver update. The driver persists the current configuration using a session ID.

### NFC\_CX\_SEQUENCE\_INIT\_COMPLETE\_FLAG\_REDO

0x00000001

This flag is used in init complete sequence to redo the initialization sequence. This is typically used if the client driver has performed a firmware download or updated hardware settings that require a reboot.

### NFC\_CX\_SEQUENCE\_PRE\_NFCEE\_DISC\_FLAG\_SKIP

0x00000001

This flag is used during NFCEE pre-discovery sequence to skip performing the NFCEE discovery.

### NFC\_CX\_SEQUENCE\_PRE\_SHUTDOWN\_FLAG\_SKIP\_RESET

0x00000001

This flag forces the NFC CX to not send an NCI reset during shutdown.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

