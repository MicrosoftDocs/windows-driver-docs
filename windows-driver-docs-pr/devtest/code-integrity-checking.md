---
title: Code integrity checks
description: Code integrity checks for Driver Verifier
keywords:
- Code integrity checks for Driver Verifier
ms.date: 09/14/2017 
---

# Code integrity checking

**Memory integrity** is a **virtualization-based security (VBS)** feature available in Windows 10, Windows 11, and Windows Server 2016 or higher. Memory integrity and VBS improve the threat model of Windows and provide stronger protections against malware trying to exploit the Windows kernel. VBS uses the Windows hypervisor to create an isolated virtual environment that becomes the root of trust of the OS that assumes the kernel can be compromised. Memory integrity is a critical component that protects and hardens Windows by running kernel mode code integrity within the isolated virtual environment of VBS. Memory integrity also restricts kernel memory allocations that could be used to compromise the system, ensuring that kernel memory pages are only made executable after passing code integrity checks inside the secure runtime environment, and executable pages themselves are never writable.

> [!NOTE]
> Memory integrity is sometimes referred to as *hypervisor-protected code integrity (HVCI)* or *hypervisor enforced code integrity*, and was originally released as part of *Device Guard*. Device Guard is no longer used except to locate memory integrity and VBS settings in Group Policy or the Windows registry.

The code integrity checks ensure compatibility with memory integrity's kernel memory usage requirements, and detects the following violations:

<table>
  <tr>
    <th>Error code</th>
    <th>Code integrity issue</th>
  </tr>
  <tr>
    <td>0x2000:
        <ul>
            <li>2 - The address in the driver's code where the error was detected.</li>
            <li>3 - Pool Type.</li>
            <li>4 - Pool Tag (if provided).</li>
        </ul><br/>    </td>
    <td>The caller specified an executable pool type. (Expected: NonPagedPoolNx)</td>
  </tr>
  <tr>
    <td>0x2001:
        <ul><li>2 - The address in the driver's code where the error was detected.</li>
        <li>3 - Page Protection (WIN32_PROTECTION_MASK).
    </td>
    <td>The caller specified an executable page protection. (Expected: cleared PAGE_EXECUTE* bits)</td>
  </tr>
  <tr>
    <td>0x2002:
        <ul><li>2 - The address in the driver's code where the error was detected.</li>
            <li>3 - Page Priority (MM_PAGE_PRIORITY logically OR'd with MdlMapping*).</li></ul>
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

You can activate code integrity checking for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting driver verifier options](./selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the code integrity checking option.

* **At the command line**

    At the command line, the code integrity checking is represented by **0x02000000 (Bit 25)**. For example:

    `verifier /flags 0x02000000 /driver MyDriver.sys`

    The feature will be active after the next boot.

* **Using Driver Verifier Manager**

1. Start Driver Verifier Manager. Type Verifier in a Command Prompt window.
2. Select Create custom settings (for code developers) and then click Next.
3. Select(check) code integrity checking.
4. Restart the computer.

## Related topics

[Implement memory integrity compatible code](../driversecurity/implement-hvci-compatible-code.md)
