---
title: Invariant MDL Checking for Stack
description: The Invariant MDL Checking for Stack option monitors how the driver handles invariant MDL buffers across the driver stack.
ms.assetid: AB27803A-6B3A-40FA-B962-79B0DA2F5FA9
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Invariant%20MDL%20Checking%20for%20Stack%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




