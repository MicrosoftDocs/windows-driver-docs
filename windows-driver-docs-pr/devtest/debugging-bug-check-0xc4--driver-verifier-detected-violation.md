---
title: Debugging Bug Check 0xC4 DRIVER_VERIFIER_DETECTED_VIOLATION
description: If Driver Verifier detects a violation, it generates a bug check to stop the computer.
ms.assetid: 4B957C57-9095-4C81-9EBC-C92C620C5824
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION


If [Driver Verifier](driver-verifier.md) detects a violation, it generates a bug check to stop the computer. This is to provide you with the most information possible for debugging the issue. One of the more frequent bug checks Driver Verifier generates is [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187). This section describes some example strategies for debugging these violations.

When [Driver Verifier](driver-verifier.md) issues a [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), it uses the parameter 1 value (or subcode) to specify the specific cause of the violation. **Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION** detects over 200 violations.

## <span id="in_this_section"></span>In this section


-   [Debugging memory leaks - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x62](debugging-memory-leaks---driver-verifier-detected-violation--c4---0x62.md)
-   [Debugging deadlocks - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x1001](debugging-deadlocks---driver-verifier-detected-violation--c4---0x1001.md)
-   [Debugging DDI Compliance bugs - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x20002 - 0x20022](debugging-ddi-compliance-bugs----driver-verifier-detected-violation--c4---0x000200--.md)
-   [Debugging NDIS/WiFi time-out errors - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4)](debugging-ndis-wifi-timeouts---driver-verifier-detected-violation--c4---0x92003--etc-.md)

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


-   Run [Driver Verifier](driver-verifier.md) on a computer reserved for testing.
-   Enable kernel-debugging on the test computer.

For more information see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) and [Handling a Bug Check When Driver Verifier is Enabled](https://msdn.microsoft.com/library/windows/hardware/hh450984).

 

 





