---
title: Invariant MDL Checking for Stack
description: The Invariant MDL Checking for Stack option monitors how the driver handles invariant MDL buffers across the driver stack.
ms.assetid: AB27803A-6B3A-40FA-B962-79B0DA2F5FA9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Invariant MDL Checking for Stack


The Invariant MDL Checking for Stack option monitors how the driver handles invariant MDL buffers across the driver stack. Driver Verifier can detect illegal modification of invariant MDL buffers. To use this option, I/O Verification must be enabled on at least one driver.

**Note**  This option is available starting with Windows 8.

 

The Invariant MDL Checking for Stack option ensures that drivers follow the rules for invariant MDL buffers only at the point the request is leaving the driver stack.

The first time an IRP with invariant MDL is seen in the [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) routine, a unique signature is computed from the contents of the invariant MDL buffer and stored in an internal database. During completion of the IRP in the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine, if the IRP still carries an invariant MDL for which we recorded the signature, Driver Verifier validates that the buffer has not changed.

An invariant buffer, for the write request, cannot be modified throughout the entire lifetime of the IRP. For a read request, an invariant buffer cannot be modified on its dispatch path, so the comparison of buffer signature is done at the last call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

The Invariant MDL Checking for Stack option verifies MDL buffer invariance across the whole driver stack, without regard to what happens to the buffer as it passes through individual drivers in the stack. This option is global and cannot be enforced selectively on a per-driver basis. The Invariant MDL Checking for Stack option can only catch the violation, without being able to pinpoint the driver who violated the buffer invariance. To help pinpoint the faulty driver, use the [Invariant MDL Checking for Driver](invariant-mdl-checking-for-driver.md) option, which does the validation of invariance of buffer contents on every call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) DDIs.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Invariant MDL Checking for Stack feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. You must restart the computer to activate or deactivate the Invariant MDL Checking for Stack option. For more information, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

To activate the Invariant MDL Checking for Stack option, you must also activate [I/O Verification](i-o-verification.md).

-   **At the command line**

    At the command line, the Invariant MDL Checking for Stack is represented by **0x00002000** (Bit 13). To activate Invariant MDL Checking for Stack, use a flag value of 0x00002010 or add 0x00002010 to the flag value. This value activates I/O Verification (0x10) and Invariant MDL Checking for Stack (0x00002000). For example:

    ```
    verifier /flags 0x00002010 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**
    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next.**
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) [I/O Verification](i-o-verification.md) and Invariant MDL Checking for Stack.
    5.  Restart the computer.

 

 





