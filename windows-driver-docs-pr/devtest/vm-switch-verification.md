---
title: VM switch verification
description: The VM switch verification option monitors filter drivers (extensible switch extensions) that run inside the Hyper-V Extensible Switch. Use this option to catch errors that occur in send or receive operations within the extensible switch.
ms.assetid: 629C0C70-D6C6-4977-A36B-6BD6EEC14FE8
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





