---
title: NDIS/WIFI verification
description: The NDIS/WIFI verification option determines whether an NDIS or WIFI driver correctly interacts with the Windows operating system kernel.
ms.assetid: EB553449-9460-403D-8ED2-343048C4B38C
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20NDIS/WIFI%20verification%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




