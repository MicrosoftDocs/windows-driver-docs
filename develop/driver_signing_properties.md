Driver Signing Properties
==============================================================================

When a project is selected in Solution Explorer, the **Properties** dialog under the **Driver Signing** node, displays two sections of properties:

<span id="Under_General_"></span><span id="under_general_"></span><span id="UNDER_GENERAL_"></span>Under General:
-----------------------------------------------------------------------------------------------------------------

**Sign Mode**

-   **Test Sign** - Microsoft Visual Studio should sign the driver with the test certificate specified in **Test Certificate** (default). If no certificate is specified in **Test Certificate** then Visual Studio will create one for the driver. **Note**: Windows requires all 64-bit drivers to be signed.
-   **Production Sign** - Visual Studio should sign the driver with the production certificate specified in **Production Certificate**.
-   **Off** - Visual Studio should not sign the driver with any certificate.

**Test Certificate**

-   *Blank* - No test certificate is selected (default).
-   **&lt;Edit...&gt;** - Selects the certificate to use when **Sign Mode** is set to **Test Sign**.

**Production Certificate**

-   *Blank* - No production certificate is selected (default).
-   **&lt;Edit...&gt;** - Selects the certificate to use when **Sign Mode** is set to **Production Sign**.

**TimeStampServer**

-   **Verisign** - Use Verisign to time stamp the driver (default).
-   **GlobalSign** - Use Globalsign to time stamp the driver.
-   **None** - Do not time stamp the driver.

**Disable Warnings**

-   **No** - Display warnings when signing the driver (default).
-   **Yes** - Do not display warnings when signing the driver.

**Enable Diagnostic Verbosity**

-   **No** - Do not display diagnostic verbosity when signing the driver (default).
-   **Yes** - Display diagnostic verbosity when signing the driver.

**File Digest Algorithm**

-   *Blank* - No file digest algorithm is selected (default).
-   **&lt;Edit...&gt;** - Select the file digest algorithm to use when signing the driver.

<span id="Under_Command_Line_"></span><span id="under_command_line_"></span><span id="UNDER_COMMAND_LINE_"></span>Under Command Line:
-------------------------------------------------------------------------------------------------------------------------------------

**Additional Options**

-   Additional options to specify when signing the driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Driver%20Signing%20Properties%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


