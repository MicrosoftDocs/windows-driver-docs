---
title: Invariant MDL Checking for Driver
description: The Invariant MDL Checking for Driver option monitors how the driver handles invariant MDL buffers on a per-driver basis.
ms.assetid: 2FA69B7C-3EF4-4660-84D4-5108C97E395F
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Invariant%20MDL%20Checking%20for%20Driver%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




