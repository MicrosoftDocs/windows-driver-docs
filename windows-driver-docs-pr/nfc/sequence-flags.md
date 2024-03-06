---
title: Sequence Flags
description: The NFC CX defines the following constants for sequence events.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
topic_type:
- apiref
ms.topic: reference
api_name:
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_SKIP_CONFIG
- NFC_CX_SEQUENCE_PRE_INIT_FLAG_FORCE_CONFIG
- NFC_CX_SEQUENCE_INIT_COMPLETE_FLAG_REDO
- NFC_CX_SEQUENCE_PRE_NFCEE_DISC_FLAG_SKIP
- NFC_CX_SEQUENCE_PRE_SHUTDOWN_FLAG_SKIP_RESET
api_type:
- NA
ms.date: 01/11/2024
---

# Sequence flags

The NFC CX defines the following constants for sequence events.

### NFC_CX_SEQUENCE_PRE_INIT_FLAG_SKIP_CONFIG

0x00000001

This flag is used in the pre-init sequence to skip configuration updates after NCI initialization. Note this flag cannot be used with force configuration option.

### NFC_CX_SEQUENCE_PRE_INIT_FLAG_FORCE_CONFIG

0x00000002

This flag is used to force update configuration after NCI initialization. Typically, NFC CX only updates the configuration either if the controller doesn't support KEEP CONFIG or if the configuration has changed after a driver update. The driver persists the current configuration using a session ID.

### NFC_CX_SEQUENCE_INIT_COMPLETE_FLAG_REDO

0x00000001

This flag is used in init complete sequence to redo the initialization sequence. This is typically used if the client driver has performed a firmware download or updated hardware settings that require a reboot.

### NFC_CX_SEQUENCE_PRE_NFCEE_DISC_FLAG_SKIP

0x00000001

This flag is used during NFCEE pre-discovery sequence to skip performing the NFCEE discovery.

### NFC_CX_SEQUENCE_PRE_SHUTDOWN_FLAG_SKIP_RESET

0x00000001

This flag forces the NFC CX to not send an NCI reset during shutdown.

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
