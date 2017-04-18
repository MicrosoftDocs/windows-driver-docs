---
title: VM switch verification
description: The VM switch verification option monitors filter drivers (extensible switch extensions) that run inside the Hyper-V Extensible Switch. Use this option to catch errors that occur in send or receive operations within the extensible switch.
ms.assetid: 629C0C70-D6C6-4977-A36B-6BD6EEC14FE8
---

# VM switch verification


The VM switch verification option monitors filter drivers (*extensible switch extensions*) that run inside the [Hyper-V Extensible Switch](https://msdn.microsoft.com/library/windows/hardware/hh598161). Use this option to catch errors that occur in send or receive operations within the extensible switch.

**Note**  This option is available starting with Windows 8.1.

 

When this option is active, Driver Verifier will issue [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION) if the extensible switch extension fails to properly call Hyper-V extensible switch handler functions.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the VM switch verification feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the Power Framework Delay Fuzzing option.

-   **At the command line**

    At the command line, the VM switch verification is represented by **verifier /flags 0x01000000** (Bit 24). To activate Power Framework Delay Fuzzing, use a flag value of 0x01000000 or add 0x01000000 to the flag value. For example:

    ```
    verifier /flags 0x01000000  /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **VM switch verification**.
    5.  Restart the computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20VM%20switch%20verification%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




