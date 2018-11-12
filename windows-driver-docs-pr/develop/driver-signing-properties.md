---
ms.assetid: A1DE1065-9D8F-405F-9807-5F0D3BE6F0AC
title: Driver Signing Properties
description: 
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Signing Properties

When a project is selected in Solution Explorer, the **Properties** dialog under the **Driver Signing** node, displays two sections of properties:

## <span id="Under_General_"></span><span id="under_general_"></span><span id="UNDER_GENERAL_"></span>Under General:


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

## <span id="Under_Command_Line_"></span><span id="under_command_line_"></span><span id="UNDER_COMMAND_LINE_"></span>Under Command Line:


**Additional Options**

-   Additional options to specify when signing the driver.

 

 





