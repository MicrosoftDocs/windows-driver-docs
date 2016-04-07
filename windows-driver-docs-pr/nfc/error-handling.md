---
title: Error handling
author: windows-driver-content
description: This topic discusses error handling requirements for NFC clients.
ms.assetid: 52376A1F-9ADD-4297-ADF9-A1EBF5714316
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# Error handling


This topic discusses error handling requirements for NFC clients.

-   The NFC client driver is responsible for notifying the NFC CX if it encounters errors when performing write requests to the controller. The NFC CX upon receiving the error status will either perform retries, recovery, or enter an error state.

-   The NFC client driver can report an error when completing a sequence call. Depending on the current state, the NFC CX will enter recovery or a enter an error state.

-   When the NFCC encounters a crash, it is expected that it sends a CORE\_RESET\_NTF to the host. The NFC CX upon receiving the CORE\_RESET\_NTF will perform the appropriate recovery.

-   When the client detects an unrecoverable error, it can notify the NFC CX to do a full driver restart through HostActionRestart or request it to unload the driver using HostActionUnload.

-   If the NFC client needs to trigger a user mode crash (for example, detecting a memory corruption), it is expected that the NFC client driver uses the WDF verifier APIs to trigger a crash using bug check codes in the reserved range for NFC client driver (see NfcCxBugCodes.h for more info). Because process-sharing is enabled by default, it is important the NFC client driver uses this mechanism only when absolutely required, otherwise it might bring down other drivers in the WUDF driver host process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Error%20handling%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




