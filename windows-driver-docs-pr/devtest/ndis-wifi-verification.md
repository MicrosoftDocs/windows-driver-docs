---
title: NDIS/WIFI verification
description: The NDIS/WIFI verification option determines whether an NDIS or WIFI driver correctly interacts with the Windows operating system kernel.
ms.assetid: EB553449-9460-403D-8ED2-343048C4B38C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS/WIFI verification


The NDIS/WIFI verification option determines whether an NDIS or WIFI driver correctly interacts with the Windows operating system kernel.

**Note**  This option is available starting with Windows 8.1.

 

The NDIS/WIFI verification option applies rules to verify that your driver correctly processes OIDs in various contexts and follows Microsoft recommended best practices.

When this option is active and Driver Verifier detects that the driver violates one of the NDIS or WIFI rules, Driver Verifier issues bug check 0xC4 (with Parameter 1 equal to the identifier of the specific compliance rule).

The list of verification rules includes the following:

[**NdisOidComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305115)

[**NdisOidDoubleComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305116)

[**NdisOidDoubleRequest**](https://msdn.microsoft.com/library/windows/hardware/dn305117)

[**NdisTimedDataHang**](https://msdn.microsoft.com/library/windows/hardware/dn305118)

[**NdisTimedDataSend**](https://msdn.microsoft.com/library/windows/hardware/dn305119)

[**NdisTimedOidComplete**](https://msdn.microsoft.com/library/windows/hardware/dn305120)

[**WlanAssociation**](https://msdn.microsoft.com/library/windows/hardware/dn305122)

[**WlanConnectionRoaming**](https://msdn.microsoft.com/library/windows/hardware/dn305123)

[**WlanDisassociation**](https://msdn.microsoft.com/library/windows/hardware/dn305124)

[**WlanTimedAssociation**](https://msdn.microsoft.com/library/windows/hardware/dn305125)

[**WlanTimedConnectionRoaming**](https://msdn.microsoft.com/library/windows/hardware/dn305126)

[**WlanTimedConnectRequest**](https://msdn.microsoft.com/library/windows/hardware/dn305127)

[**WlanTimedScan**](https://msdn.microsoft.com/library/windows/hardware/dn305129)

[**WlanTimedLinkQuality**](https://msdn.microsoft.com/library/windows/hardware/dn305128)

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the NDIS/WIFI verification feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the NDIS/WIFI verification option.

-   **At the command line**

    At the command line, NDIS/WIFI verification is represented by **verifier /flags 0x200000** (bit 21). To activate NDIS/WIFI verification, use a flag value of 0x200000 or add 0x200000 to the flag value. For example:

    ```
    verifier /flags 0x200000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **NDIS/WIFI verification**.
    5.  Restart the computer.

 

 





