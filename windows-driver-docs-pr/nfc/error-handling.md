---
title: Error Handling
description: This topic discusses error handling requirements for NFC clients.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Error handling

This topic discusses error handling requirements for NFC clients.

- The NFC client driver is responsible for notifying the NFC CX if it encounters errors when performing write requests to the controller. The NFC CX upon receiving the error status will either perform retries, recovery, or enter an error state.

- The NFC client driver can report an error when completing a sequence call. Depending on the current state, the NFC CX will enter recovery or a enter an error state.

- When the NFCC encounters a crash, it is expected that it sends a CORE_RESET_NTF to the host. The NFC CX upon receiving the CORE_RESET_NTF will perform the appropriate recovery.

- When the client detects an unrecoverable error, it can notify the NFC CX to do a full driver restart through HostActionRestart or request it to unload the driver using HostActionUnload.

- If the NFC client needs to trigger a user mode crash (for example, detecting a memory corruption), it is expected that the NFC client driver uses the WDF verifier APIs to trigger a crash using bug check codes in the reserved range for NFC client driver (see NfcCxBugCodes.h for more info). Because process-sharing is enabled by default, it is important the NFC client driver uses this mechanism only when absolutely required, otherwise it might bring down other drivers in the WUDF driver host process.

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
