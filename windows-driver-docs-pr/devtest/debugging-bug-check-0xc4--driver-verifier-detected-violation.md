---
title: Debugging Bug Check 0xC4 DRIVER\_VERIFIER\_DETECTED\_VIOLATION
description: If Driver Verifier detects a violation, it generates a bug check to stop the computer.
ms.assetid: 4B957C57-9095-4C81-9EBC-C92C620C5824
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Debugging%20Bug%20Check%200xC4:%20DRIVER_VERIFIER_DETECTED_VIOLATION%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




