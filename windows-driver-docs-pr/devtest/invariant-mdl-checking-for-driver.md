---
title: Invariant MDL Checking for Driver
description: The Invariant MDL Checking for Driver option monitors how the driver handles invariant MDL buffers on a per-driver basis.
ms.assetid: 2FA69B7C-3EF4-4660-84D4-5108C97E395F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Invariant MDL Checking for Driver


The Invariant MDL Checking for Driver option monitors how the driver handles invariant MDL buffers on a per-driver basis. This option detects illegal modification of invariant MDL buffers. To use this option, you must enable I/O Verification on at least one driver.

**Note**  This option is available starting with Windows 8.

 

The Invariant MDL Checking for Driver option performs a more intensive form of the invariant MDL checking than the [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md) option. When the Invariant MDL Checking for Driver is active, buffer invariance is validated across every call to the [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routines.

Every time a new invariant MDL buffer is seen with an IRP, Driver Verifier computes a signature for the buffer contents and stores it in its internal database. When Driver Verifier encounters an invariant MDL buffer that it has seen earlier, it will validate that the contents of buffer has not changed, by comparing the signature in the database with the signature computed over current invariant MDL buffer contents.

This option is global and cannot be enforced selectively some drivers.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Invariant MDL Checking for Driver feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the Invariant MDL Checking for Driver option.

To activate the [Invariant MDL Checking for Stack](invariant-mdl-checking-for-stack.md) option, you must also activate [I/O Verification](i-o-verification.md).

-   **At the command line**

    At the command line, the Invariant MDL Checking for Driver is represented by **verifier /flags 0x00004000** (Bit 14). To activate Invariant MDL Checking for Driver, use a flag value of 0x00004010 or add 0x00004010 to the flag value. This value activates I/O Verification (0x10) and the Invariant MDL Checking for Driver (0x00004000). For example:

    ```
    verifier /flags 0x00004010 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**
    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next.**
    3.  Select **Select individual settings from a full list**.
    4.  Select (check)[I/O Verification](i-o-verification.md) and Invariant MDL Checking for Driver.
    5.  Restart the computer.

 

 





