---
title: Code integrity checks
description: Code integrity checks for Driver Verifier
ms.assetid: ad6c4762-354d-446d-bcda-a2e99c37c589
keywords:
- Code integrity checks for Driver Verifier
ms.date: 09/14/2017 
ms.localizationpriority: medium
---

# Code integrity checking

[Device Guard](https://blogs.msdn.microsoft.com/windows_hardware_certification/2015/05/22/driver-compatibility-with-device-guard-in-windows-10/) can use hardware technology and virtualization to isolate the Code Integrity (CI) decision-making function from the rest of the Windows operating system. When using virtualization-based security to isolate Code Integrity, the only way kernel memory can become executable is through a Code Integrity verification. This means that kernel memory pages can never be Writable and Executable (W+X) and executable code cannot be directly modified. The code integrity checks ensure compatibility of these code integrity rules, and detects the following violations:

<table>
  <tr>
    <th>Error code</th>
    <th>Code integrity issue</th>
  </tr>
  <tr>
    <td>0x2000:
        <ul>
            <li>2 - The address in the driver&#39;s code where the error was detected.</li>
            <li>3 - Pool Type.</li>
            <li>4 - Pool Tag (if provided).</li>
        </ul><br/>    </td>
    <td>The caller specified an executable pool type. (Expected: NonPagedPoolNx)</td>
  </tr>
  <tr>
    <td>0x2001:
        <ul><li>2 - The address in the driver&#39;s code where the error was detected.</li>
        <li>3 - Page Protection (WIN32_PROTECTION_MASK).
    </td>
    <td>The caller specified an executable page protection. (Expected: cleared PAGE_EXECUTE* bits)</td>
  </tr>
  <tr>
    <td>0x2002:
        <ul><li>2 - The address in the driver&#39;s code where the error was detected.</li>
            <li>3 - Page Priority (MM_PAGE_PRIORITY logically OR&#39;d with MdlMapping*).</li></ul>
    </td>
    <td>The caller specified an executable MDL mapping. (Expected: MdlMappingNoExecute).</td>
  </tr>
  <tr>
    <td>0x2003:
        <ul><li>2 - The image file name (Unicode string).</li>
            <li>3 - The address of the section header.</li>
            <li>4 - The section name (UTF-8 encoded string).</li></ul>
    </td>
    <td>The image contains an executable and writable section.</td>
  </tr>
  <tr>
    <td>0x2004:
        <ul><li>2 - The image file name (Unicode string).</li>
            <li>3 - The address of the section header.</li>
            <li>4 - The section name (UTF-8 encoded string).</li></ul>
    </td>
    <td>The image contains a section that is not page aligned.</td>
  </tr>
  <tr>
    <td>0x2005:
        <ul><li>2 - The image file name (Unicode string).</li>
            <li>3 - IAT Directory.</li>
            <li>4 - The section name (UTF-8 encoded string).</li><ul>
    </td>
    <td>The image contains an IAT located in an executable section.</td>
  </tr>
</table>

### Activating this option:

You can activate port/miniport interface checking for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting driver verifier options](https://docs.microsoft.com/windows-hardware/drivers/devtest/selecting-driver-verifier-options). You must restart the computer to activate or deactivate the port/miniport interface checking option.

* **At the command line**

    At the command line, the port miniport interface checking is represented by **0x02000000 (Bit 25)**. For example:

    `verifier /flags 0x02000000 /driver MyDriver.sys`

    The feature will be active after the next boot.

* **Using Driver Verifier Manager**

1. Start Driver Verifier Manager. Type Verifier in a Command Prompt window.
2. Select Create custom settings (for code developers) and then click Next.
3. Select(check) Port miniport interface checking.
4. Restart the computer.
