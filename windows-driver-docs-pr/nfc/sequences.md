---
title: NFC CX Driver Sequences
description: This topic describes NFC CX driver sequences.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Sequences

This topic describes NFC CX driver sequences.

| Sequence | Description |
|--|--|
| SequencePreInit | Invoked by CX during the idle to init state transition (that is, prior to start of initialization by NFC CX). No NCI commands including CORE_RESET_CMD has been sent to the NFC controller by NFC CX. In this sequence, the client can invoke any non-NCI command. NCI commands shouldn't be sent to the controller since neither CORE_RESET_CMD nor CORE_INIT_CMD has been sent to the controller. |
| SequenceInitComplete | Invoked by CX immediately after the completion of initialization of NFC CX which includes NCI reset, NCI initialization and configuration of the NFC controller. |
| SequencePreRfDiscStart | Invoked by CX prior to start of RF discovery i.e. through RF_DISCOVER_CMD. The client driver can use this opportunity to perform any related RF configuration including any optimizations to the discovery loop. |
| SequenceRfDiscStartComplete | Invoked by CX immediately after the start of RF discovery. Any configuration post-discovery start can be supported through this extensibility point. |
| SequencePreRfDiscStop | Invoked by CX prior to stopping the RF discovery loop. |
| SequenceRfDiscStopComplete | Invoked immediately after discovery loop is stopped. The client driver can use this extensibility point to enable any standby mode configuration. |
| SequencePreNfceeDisc | Invoked by CX prior to start of NFCEE discovery. The NFCEE discovery happens with the discovery loop deactivated. The client driver can use this sequence to enable any internal NFC-NFCEE interfaces which could have been disabled post-initialization for power optimizations. |
| SequenceNfceeDiscComplete | Invoked immediately post-NFCEE discovery operation. |
| SequencePreShutdown | Invoked prior to start of shutdown. |
| SequenceShutdownComplete | Invoked by CX after shutdown sequence is complete. The client driver can clean up any NCI state maintained. |
| SequencePreRecovery | Invoked by CX if it needs to perform a recovery sequence due to a fatal failure. The client driver can use this sequence to capture RAM dumps for diagnostic purposes. |
| SequenceRecoveryComplete | Invoked by the CX after the completion of the recovery sequence and when the driver is back to the work-state |

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
