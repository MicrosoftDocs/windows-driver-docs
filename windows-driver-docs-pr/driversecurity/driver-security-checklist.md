---
title: Driver security checklist
description: This article provides a driver security checklist for driver developers.
ms.date: 01/23/2025
---

# Driver security checklist

This article provides a driver security checklist for driver developers to help reduce the risk of drivers being compromised. Driver security is critical and directly impacts reliability. When Windows detects that incorrect memory access is taking place, it will shut down the OS and display a blue error screen. As a Windows partner you must work to reduce the significant impact that a failed driver has on our customers' lives.

For more information on the benefits of providing a secure and reliable driver, see [Driver security guidance](index.md).

## Driver security overview

A security flaw is any flaw that allows an attacker to cause a driver to malfunction in such a way that it enables an attacker to gain unauthorized access, manipulate the system, or compromise data, potentially causing the system to crash or become unusable. In addition, vulnerabilities in driver code can allow an attacker to gain access to the kernel, creating a possibility of compromising the entire OS. 

When most developers are working on their driver, their focus is on getting the driver to work properly, and not on whether a malicious attacker will attempt to exploit vulnerabilities within their code. After a driver is released, however, attackers can attempt to probe and identify security flaws. Developers must consider these issues during the design and implementation phase in order to minimize the likelihood of such vulnerabilities. The goal is to eliminate all known security flaws before the driver is released.

Creating more secure drivers requires the cooperation of the system architect (consciously thinking of potential threats to the driver), the developer implementing the code (defensively coding common operations that can be the source of exploits), and the test team (proactively attempting to find weakness and vulnerabilities). By properly coordinating all of these activities, the security of the driver is dramatically enhanced.

In addition to avoiding the issues associated with a driver being attacked, many of the steps described, such as more precise use of kernel memory, will increase the reliability of your driver. This reduces support costs and increases customer satisfaction with your product. Completing the tasks in the checklist below will help to achieve all these goals.

**Security checklist:** *Complete the security task described in each of these topics.*

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Confirm that a kernel driver is required](#confirm-that-a-kernel-driver-is-required)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Use the driver frameworks](#use-the-driver-frameworks)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Manage driver access control](#manage-driver-access-control)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Control access to software only drivers](#control-access-to-software-only-drivers)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Follow driver secure coding guidelines](#follow-driver-secure-coding-guidelines)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Implement HVCI compatible code](#implement-hvci-compatible-code)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Follow technology-specific code best practices](#follow-technology-specific-code-best-practices)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Add SAL annotations to your driver code](#add-sal-annotations-to-your-driver-code)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Perform peer code review](#perform-peer-code-review)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Perform threat analysis](#perform-threat-analysis)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Use CodeQL to check your driver code](#use-codeql-to-check-your-driver-code)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Use Driver Verifier to check for vulnerabilities](#use-driver-verifier-to-check-for-vulnerabilities)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Check code with the hardware compatibility program tests](#check-code-with-the-hardware-compatibility-program-tests)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Check ready to ship drivers with the tools like BinSkim and SignTool](#check-ready-to-ship-drivers-with-tools-like-binskim-and-signtool)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Do not production sign test driver code](#do-not-production-sign-test-code)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Execute proper release driver signing and distribute your driver package using Windows Update](#execute-proper-release-driver-signing-and-distribute-your-driver-package-using-windows-update)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Understand how drivers are reported using the Microsoft Vulnerable and Malicious Driver Reporting Center](#understand-how-drivers-are-reported-using-the-microsoft-vulnerable-and-malicious-driver-reporting-center)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist."::: [Review secure coding resources](#review-secure-coding-resources)

:::image type="content" source="images/checkbox.png" alt-text="Unmarked checkbox representing an item in the security checklist.":::Review the [Summary of key takeaways](#summary-of-key-takeaways)

## Confirm that a kernel driver is required

**Security checklist item \#1:** *Confirm that a kernel driver is required and that a lower risk approach, such as Windows service or app, isn't a better option.*

Kernel drivers live in the Windows kernel and having an issue when executing in kernel exposes the entire operating system. If any other option is available, it likely will be lower cost and have less associated risk than creating a new kernel driver.

For more information about using the built-in Windows drivers, see [Do you need to write a driver?](../gettingstarted/do-you-need-to-write-a-driver-.md).

For information on using background tasks, see [Support your app with background tasks](/windows/uwp/launch-resume/support-your-app-with-background-tasks).

For information on using Windows Services, see [Services](/windows/desktop/Services/services).

## Use the driver frameworks

**Security checklist item \#2:** *Use the driver frameworks to reduce the size of your code and increase its reliability and security.*

Use the [Windows Driver Frameworks](../wdf/index.md) to reduce the size of your code and increase its reliability and security. To get started, review [Using WDF to Develop a Driver](../wdf/using-the-framework-to-develop-a-driver.md). For information on using the lower risk User Mode Driver Framework (UMDF), see [Choosing a driver model](../gettingstarted/choosing-a-driver-model.md).

Writing an old-fashion [Windows Driver Model (WDM)](../kernel/writing-wdm-drivers.md) driver is more time consuming, costly, and involves recreating code that is available in the driver frameworks.

The Windows Driver Framework (WDF) source code is open source and available on GitHub. This is the same WDF source code that ships in Windows. You can debug your driver more effectively when you can follow the interactions between the driver and WDF. Download it from [https://github.com/Microsoft/Windows-Driver-Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks).

### DMF - Driver Module Framework

Consider the use of the Driver Module Framework (DMF) in your driver project. Developed by the Microsoft Surface team, DMF is a framework that allows creation of WDF objects called DMF modules. The code for these DMF modules can be shared between different drivers. In addition, DMF provides a library of DMF modules that have been developed for drivers and offer code reuse for tasks such as thread and I/O management. A DMF module is used to encapsulate driver tasks into smaller units. Each module is self-contained and has its own code, context, and callbacks, making it easier to reuse. For more information, see [Introducing Driver Module Framework](https://blogs.windows.com/windowsdeveloper/2018/08/15/introducing-driver-module-framework/) and the [GitHub site documentation](https://github.com/Microsoft/DMF/blob/master/Dmf/Documentation/Driver%20Module%20Framework.md#what-is-the-driver-module-framework-dmf).

## Manage driver access control

**Security checklist item \#3:** *Review your driver to make sure that you're properly controlling access.*

### Managing driver access control - WDF

Drivers must work to prevent users from inappropriately accessing a computer's devices and files. To prevent unauthorized access to devices and files, you must:

- Name device objects only when necessary. Named device objects are generally only necessary for legacy reasons, for example if you have an application that expects to open the device using a particular name or if you're using a non-PNP device/control device. Note that WDF drivers do not need to name their PnP device FDO in order to create a symbolic link using [WdfDeviceCreateSymbolicLink](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatesymboliclink).

- Secure access to device objects and interfaces.

In order to allow applications or other WDF drivers to access your PnP device PDO, you should use device interfaces. For more information, see [Using Device Interfaces](../wdf/using-device-interfaces.md). A device interface serves as a symbolic link to your device stack's PDO.

One of the better ways to control access to the PDO is by specifying an SDDL string in your INF. If the SDDL string isn't in the INF file, Windows will apply a default security descriptor. For more information, see [Securing Device Objects](../kernel/controlling-device-access.md) and [SDDL for Device Objects](../kernel/sddl-for-device-objects.md).

For more information about controlling access, see the following:

[Controlling Device Access in KMDF Drivers](../wdf/controlling-device-access-in-kmdf-drivers.md)

[Names, Security Descriptors and Device Classes - Making Device Objects Accessible… and SAFE](https://www.osr.com/nt-insider/2017-issue1/making-device-objects-accessible-safe/) from the *January February 2017 The NT Insider Newsletter* published by [OSR](https://www.osr.com).

### Managing driver access control - WDM

If you're working with a WDM Driver and you used a named device object you can use [IoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) and specify a SDDL to secure it. When you implement [IoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) always specify a custom class GUID for DeviceClassGuid. You should not specify an existing class GUID here. Doing so has the potential to break security settings or compatibility for other devices belonging to that class. For more information, see [WdmlibIoCreateDeviceSecure](/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure).

For more information, see the following:

[Controlling Device Access](../kernel/controlling-device-access.md)

[Controlling Device Namespace Access](../kernel/controlling-device-namespace-access.md)

[Windows security model for driver developers](windows-security-model.md)

### Security Identifiers (SIDs) risk hierarchy

The following section describes the risk hierarchy of the common SIDs used in driver code. For general information about SDDL, see [SDDL for Device Objects](../kernel/sddl-for-device-objects.md), [SID Strings](/windows/desktop/SecAuthZ/sid-strings), and [SDDL String Syntax](/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070).

It is important to understand that if lower privilege callers are allowed to access the kernel, code risk is increased. In this summary diagram, the risk increases as you allow lower privilege SIDs access to your driver functionality.

```text
SY (System)
     \/
BA (Built-in Administrators)
     \/
LS (Local Service)
     \/
BU (Built-in User)
     \/
AC (Application Container)
```

Following the general least privilege security principle, configure only the minimum level of access that is required for your driver to function.

### WDM Granular IOCTL security control

An IOCTL (Input/Output Control) in Windows is a system call for device-specific input/output operations. IOCTLs are used by applications to communicate with device drivers, allowing them to send commands or request information from the hardware. For more information, see [Introduction to I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) and [Example I/O Request - An Overview](../kernel/example-i-o-request---an-overview.md).

To further manage security when IOCTLs are sent by user-mode callers, the driver code can include the [IoValidateDeviceIoControlAccess](/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess) function. This function allows a driver to check access rights. Upon receiving an IOCTL, a driver can call [IoValidateDeviceIoControlAccess](/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess), specifying FILE_READ_ACCESS, FILE_WRITE_ACCESS, or both.

Implementing granular IOCTL security control does not replace the need to manage driver access using the techniques discussed above.

For more information, see [Defining I/O Control Codes](../kernel/defining-i-o-control-codes.md) and 
[Security Issues for I/O Control Codes](../kernel/security-issues-for-i-o-control-codes.md).

## Control access to software only drivers

**Security checklist item \#4:** *If a software-only driver is going to be created, additional access control must be implemented.*

Software-only kernel drivers do not use plug-and-play (PnP) to become associated with specific hardware IDs, and can run on any PC. Such a driver could be used for purposes other than the one originally intended, creating an attack vector.

Because software-only kernel drivers contain additional risk, they must be limited to run on specific hardware (for example, by using a unique PnP ID to enable creation of a PnP driver, or by checking the SMBIOS table for the presence of specific hardware).

For example, imagine OEM Fabrikam wants to distribute a driver that enables an overclocking utility for their systems. If this software-only driver were to execute on a system from a different OEM, system instability or damage might result. Fabrikam's systems should include a unique PnP ID to enable creation of a PnP driver that is also updatable through Windows Update. If this isn't possible, and Fabrikam authors a Legacy driver, that driver should find another method to verify that it is executing on a Fabrikam system (for example, by examination of the SMBIOS table before enabling any capabilities).

## Follow driver secure coding guidelines

**Security checklist item \#5:** *Review your code and remove any known code vulnerabilities.*

The core activity of creating secure drivers is identifying areas in the code that need to be changed to avoid known software vulnerabilities. Many of these known software vulnerabilities deal with keeping strict track of the use of memory to avoid issues with others overwriting or otherwise compromising the memory locations that your driver uses.

Code scanning tools such as CodeQL and driver specific tests, can be used to help locate, some, but not all, of these vulnerabilities. These tools and tests are described later in this topic.

### Memory buffers

- Always check the sizes of the input and output buffers to ensure that the buffers can hold all the requested data. For more information, see [Failure to Check the Size of Buffers](../kernel/failure-to-check-the-size-of-buffers.md).

- Properly initialize all output buffers with zeros before returning them to the caller. For more information, see [Failure to Initialize Output Buffers](../kernel/failure-to-initialize-output-buffers.md).

- Validate variable-length buffers. For more information, see [Failure to Validate Variable-Length Buffers](../kernel/failure-to-validate-variable-length-buffers.md). For more information about working with buffers and using [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) to validate the address of a buffer, see [Buffer Handling](../ifs/buffer-handling.md).

#### Use the appropriate method for accessing data buffers with IOCTLs

One of the primary responsibilities of a Windows driver is transferring data between user-mode applications and a system's devices. The three methods for accessing data buffers are shown in the following table.

| IOCTL Buffer Type                     | Summary                          | For more information                                                                        |
|---------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------|
| METHOD_BUFFERED                       | Recommended for most situations | [Using Buffered I/O](../kernel/using-buffered-i-o.md)                                       |
| METHOD_IN_DIRECT or METHOD_OUT_DIRECT | Used in some high speed HW I/O   | [Using Direct I/O](../kernel/using-direct-i-o.md)                                           |
| METHOD_NEITHER                        | Avoid if possible                | [Using Neither Buffered Nor Direct I/O](../kernel/using-neither-buffered-nor-direct-i-o.md) |

In general, buffered I/O is recommended as it provides the most secure buffering methods. But even when using buffered I/O there are risks, such as embedded pointers that must be mitigated.

For more information about working with buffers in IOCTLs, see [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md).

#### Errors in use of IOCTL buffered I/O

- Check the size of IOCTL related buffers. For more information, see [Failure to Check the Size of Buffers](../kernel/failure-to-check-the-size-of-buffers.md).

- Properly initialize output buffers. For more information, see [Failure to Initialize Output Buffers](../kernel/failure-to-initialize-output-buffers.md).

- Properly validate variable-length buffers. For more information, see [Failure to Validate Variable-Length Buffers](../kernel/failure-to-validate-variable-length-buffers.md).

- When using buffered I/O, be sure and return the proper length for the OutputBuffer in the [IO_STATUS_BLOCK](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure Information field. Don't just directly return the length directly from a READ request. For example, consider a situation where the returned data from the user space indicates that there is a 4K buffer. If the driver actually should only return 200 bytes, but instead just returns 4K in the Information field an information disclosure vulnerability has occurred. This problem occurs because in earlier versions of Windows, the buffer the I/O Manager uses for Buffered I/O isn't zeroed. Thus, the user app gets back the original 200 bytes of data plus 4K-200 bytes of whatever was in the buffer (non-paged pool contents). This scenario can occur with all uses of Buffered I/O and not just with IOCTLs.

#### Errors in IOCTL direct I/O

Handle zero-length buffers correctly. For more information, see [Errors in Direct I/O](../kernel/errors-in-direct-i-o.md).

#### Errors in referencing user-space addresses

- Validate pointers embedded in buffered I/O requests. For more information, see [Errors in Referencing User-Space Addresses](../kernel/errors-in-referencing-user-space-addresses.md).

- Validate any address in the user space before trying to use it, using APIs such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread).

### Driver code must make correct use of memory

- All driver pool allocations must be in non-executable (NX) pool. Using NX memory pools is inherently more secure than using executable non-paged (NP) pools, and provides better protection against overflow attacks.

- To allow drivers to support HVCI virtualization, there are additional memory requirements. For more information, see [Implement HVCI compatible code](#implement-hvci-compatible-code) later in this article.

#### TOCTOU vulnerabilities

There is a [potential time of check to time of use](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use) (TOCTOU) vulnerability when using direct I/O (for IOCTLs or for Read/Write). Be aware that as the driver is accessing the user data buffer, the user app can simultaneously be accessing the same data buffer.

To manage this risk, copy any parameters that need to be validated from the user data buffer to memory that is solely accessible from kernel mode (such as the stack or pool). Then once the data can't be accessed by the user application, validate and then operate on the data that was passed in.

#### MSR model-specific register reads and writes

Compiler intrinsics, such as [__readmsr](/cpp/intrinsics/readmsr) and [__writemsr](/cpp/intrinsics/writemsr) can be used to access the model-specific registers. If this access is required, the driver must always check that the register to read or write to, is constrained to the expected index or range.

For more information, and code examples, see [Providing the ability to read/write MSRs](driver-security-dev-best-practices.md#providing-the-ability-to-read-and-write-msrs) in [Best practices for constraining high privileged behavior in kernel mode drivers](driver-security-dev-best-practices.md).

### Handles

- Validate handles passed between user-mode and kernel-mode memory. For more information, see [Handle Management](../ifs/handle-management.md) and [Failure to Validate Object Handles](../kernel/failure-to-validate-object-handles.md).

### Device objects

- Secure device objects. For more information, see [Securing Device Objects](../kernel/controlling-device-access.md).

- Validate device objects. For more information, see [Failure to Validate Device Objects](../kernel/failure-to-validate-device-objects.md).

### IRPs

Windows I/O Request Packets (IRPs) are used to communicate I/O requests between the operating system and kernel-mode drivers, encapsulating all necessary information in the packet. IRPs facilitate asynchronous data transfer, synchronization, and error handling, ensuring efficient and reliable communication with hardware devices. For more information, see [I/O Request Packets](../gettingstarted/i-o-request-packets.md) and [Overview of the Windows I/O Model](../kernel/overview-of-the-windows-i-o-model.md).

#### WDF and IRPs

One advantage of using WDF, is that WDF drivers typically do not directly access IRPs. For example, the framework converts the WDM IRPs that represent read, write, and device I/O control operations to framework request objects that KMDF/UMDF receive in I/O queues. Whenever possible, the use of WDF is strongly recommended.

If you need to write a WDM driver, review the following guidance.

#### Properly manage IRP I/O buffers

Review these topics that cover how to validate IRP input values:

[DispatchReadWrite Using Buffered I/O](../kernel/dispatchreadwrite-using-buffered-i-o.md)

[Errors in Buffered I/O](../kernel/failure-to-check-the-size-of-buffers.md)

[DispatchReadWrite Using Direct I/O](../kernel/dispatchreadwrite-using-direct-i-o.md)

[Errors in Direct I/O](../kernel/errors-in-direct-i-o.md)

Validate values that are associated with an IRP, such as buffer addresses and lengths.

If you chose to use Neither I/O, be aware that unlike Read and Write, and unlike Buffered I/O and Direct I/O, that when using Neither I/O IOCTL the buffer pointers and lengths are not validated by the I/O Manager.

#### Handle IRP completion operations properly

A driver must never complete an IRP with a status value of `STATUS_SUCCESS` unless it actually supports and processes the IRP. For information about the correct ways to handle IRP completion operations, see [Completing IRPs](../kernel/completing-irps.md).

#### Manage driver IRP pending state

The driver should mark the IRP pending before it saves the IRP, and should consider including both the call to [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) and the assignment in an interlocked sequence. For more information, see [Failure to Check a Driver's State](../kernel/failure-to-check-a-driver-s-state.md) and [Holding Incoming IRPs When A Device Is Paused](../kernel/holding-incoming-irps-when-a-device-is-paused.md).

#### Handle IRP cancellation operations properly

Cancel operations can be difficult to code properly because they typically execute asynchronously. Problems in the code that handles cancel operations can go unnoticed for a long time, because this code is typically not executed frequently in a running system. Be sure to read and understand all of the information supplied under [Canceling IRPs](../kernel/canceling-irps.md). Pay special attention to [Synchronizing IRP Cancellation](../kernel/synchronizing-irp-cancellation.md) and [Points to Consider When Canceling IRPs](../kernel/points-to-consider-when-canceling-irps.md).

One recommended way to minimize the synchronization problems that are associated with cancel operations is to implement a [cancel-safe IRP queue](../kernel/cancel-safe-irp-queues.md).

#### Handle IRP cleanup and close operations properly

Be sure that you understand the difference between [**IRP\_MJ\_CLEANUP**](../kernel/irp-mj-cleanup.md) and [**IRP\_MJ\_CLOSE**](../kernel/irp-mj-close.md) requests. Cleanup requests arrive after an application closes all handles on a file object, but sometimes before all I/O requests have completed. Close requests arrive after all I/O requests for the file object have been completed or canceled. For more information, see the following:

[DispatchCreate, DispatchClose, and DispatchCreateClose Routines](../kernel/dispatchcreate--dispatchclose--and-dispatchcreateclose-routines.md)

[DispatchCleanup Routines](../kernel/dispatchcleanup-routines.md)

[Errors in Handling Cleanup and Close Operations](../kernel/errors-in-handling-cleanup-and-close-operations.md)

For more information about handling IRPs correctly, see [Additional Errors in Handling IRPs](../kernel/additional-errors-in-handling-irps.md).

#### Use safe functions

- Use safe string functions. For more information, see [Using Safe String Functions](../kernel/using-safe-string-functions.md).

- Use safe arithmetic functions. For more information, see [Safe Integer Library Routines](/windows-hardware/drivers/ddi/_kernel/#safe-integer-library-routines).

- Use safe conversion functions. For more information, see [Summary of Kernel-Mode Safe Integer Functions](../kernel/summary-of-safe-integer-functions.md).

### Other security issues

- Use a lock or an interlocked sequence to prevent race conditions. For more information, see [Errors in a Multiprocessor Environment](../kernel/errors-in-a-multiprocessor-environment.md).

- Ensure that no network Transport Driver Interface (TDI) filters or Layered Service Providers (LSPs) are installed by the driver or associated software packages during installation or usage. Instead use modern APIs, such as the [Windows Filtering Platform (WFP) ](/windows/win32/fwp/windows-filtering-platform-start-page).

### Additional code vulnerabilities

In addition to the possible vulnerabilities covered here, this article provides additional information about enhancing the security of kernel mode driver code: [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md).

For additional information about C and C++ secure coding, see [Secure coding resources](#review-secure-coding-resources) at the end of this article.

## Implement HVCI compatible code

**Security checklist item \#6:** *Validate that your driver uses memory so that it is HVCI compatible.*

### Memory integrity and HVCI compatibility

Memory integrity, also known as Hypervisor-protected Code Integrity (HVCI) uses hardware technology and virtualization to isolate the Code Integrity (CI) decision-making function from the rest of the operating system. When using virtualization-based security to isolate CI, the only way kernel memory can become executable is through a CI verification. This means that kernel memory pages can never be Writable and Executable (W+X) and executable code cannot be directly modified.

To implement HVCI compatible code, make sure your driver code does the following:

- Opts in to NX by default
- Uses NX APIs/flags for memory allocation (NonPagedPoolNx)
- Does not use sections that are both writable and executable
- Does not attempt to directly modify executable system memory
- Does not use dynamic code in kernel
- Does not load data files as executable
- Section alignment is a multiple of 0x1000 (PAGE\_SIZE). For example, DRIVER\_ALIGNMENT=0x1000

For more information about using the tool and a list of incompatible memory calls, see [Implement HVCI compatible code](implement-hvci-compatible-code.md).

For more information about the related system fundamentals security test, see [HyperVisor Code Integrity Readiness Test](/windows-hardware/test/hlk/testref/b972fc52-2468-4462-9799-6a1898808c86) and [Hypervisor-Protected Code Integrity (HVCI)](/windows-hardware/test/hlk/testref/driver-compatibility-with-device-guard).


## Enhance device installation security

**Security checklist item \#7:** *Review driver inf creation and installation guidance to make sure you're following best practices.*

When you create the code that installs your driver package, you must make sure that the installation of your device will always be performed in a secure manner. A secure device installation is one that does the following:

- Limits access to the device and its device interface classes
- Limits access to the driver services that were created for the device
- Protects driver files from modification or deletion
- Limits access to the device's registry entries
- Limits access to the device's WMI classes
- Uses SetupAPI functions correctly

For more information, see the following:

[Creating Secure Device Installations](../install/creating-secure-device-installations.md)

[Guidelines for Using SetupAPI](../install/guidelines-for-using-setupapi.md)

[Using Device Installation Functions](../install/using-device-installation-functions.md)

[Device and Driver Installation Advanced Topics](../install/creating-secure-device-installations.md)


## Follow technology-specific code best practices

**Security checklist item \#8:** *Review the following technology-specific guidance for your driver.*

### File Systems

For more information, about file system driver security see the following:

[Introduction to File Systems Security](../ifs/introduction-to-file-systems-security.md)

[File System Security Issues](../ifs/file-system-security-issues.md)

[Security Features for File Systems](../ifs/security-features-for-file-systems.md)

[Coexistence with other File System Filter Drivers](../ifs/coexistence-with-other-file-system-filter-drivers.md)

### Microsoft Virus Initiative

The Microsoft Virus Initiative (MVI) helps organizations improve the security solutions our customers rely on to keep them safe. Microsoft provides tools, resources, and knowledge to support better-together experiences with great performance, reliability, and compatibility. Microsoft collaborates with MVI partners to define and follow Safe Deployment Practices (SDP) to support the safety and resiliency of our mutual customers.

If you're an anti-virus vendor, see [Microsoft Virus Initiative](/defender-xdr/virus-initiative-criteria) to learn how to join MVI for more assistance on software deployment. For information on how security vendors can better leverage the integrated security capabilities of Windows for increased security and reliability, see [Windows Security best practices for integrating and managing security tools](https://www.microsoft.com/security/blog/2024/07/27/windows-security-best-practices-for-integrating-and-managing-security-tools/).

### NDIS - Networking

For information about NDIS driver security, see [Security Issues for Network Drivers](../network/security-issues-for-network-drivers.md).

### Printers

For information related to printer driver security, see [V4 Printer Driver Security Considerations](../print/v4-printer-driver-security-considerations.md).

### Security Issues for Windows Image Acquisition (WIA) Drivers

For information about WIA security, see [Security Issues for Windows Image Acquisition (WIA) Drivers](../image/security-issues-for-wia-drivers.md).

## Add SAL annotations to your driver code

**Security checklist item \#9:** *Add SAL annotations to your driver code.*

The source-code annotation language (SAL) provides a set of annotations that you can use to describe how a function uses its parameters, the assumptions that it makes about them, and the guarantees that it makes when it finishes. The annotations are defined in the header file `sal.h`. Visual Studio code analysis for C++ uses SAL annotations to modify its analysis of functions. For more information about SAL 2.0 for Windows driver development, see [SAL 2.0 Annotations for Windows Drivers](../devtest/sal-2-annotations-for-windows-drivers.md) and [Using SAL Annotations to Reduce C/C++ Code Defects](/visualstudio/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects).

For general information on SAL, refer to this article available from OSR. [SAL Annotations: Don’t Hate Me Because I’m Beautiful](https://www.osr.com/blog/2015/02/23/sal-annotations-dont-hate-im-beautiful/)

## Perform peer code review

**Security checklist item \#10:** *Perform peer code review, to look for issues not surfaced by the other tools and processes*

Seek out knowledgeable code reviewers to look for issues that you may have missed. A second set of eyes will often see issues that you may have overlooked.

If you don't have suitable staff to review your code internally, consider engaging outside help for this purpose.

## Perform threat analysis

**Security checklist item \#11:** *Either modify an existing driver threat model or create a custom threat model for your driver.*

In considering security, a common methodology is to create specific threat models that attempt to describe the types of attacks that are possible. This technique is useful when designing a driver because it forces the developer to consider the potential attack vectors against a driver in advance. Having identified potential threats, a driver developer can then consider means of defending against these threats in order to bolster the overall security of the driver component.

This article provides driver specific guidance for creating a lightweight threat model: [Threat modeling for drivers](threat-modeling-for-drivers.md). The article provides an example driver threat model diagram that can be used as a starting point for your driver.

:::image type="content" source="images/sampledataflowdiagramkernelmodedriver.gif" alt-text="Sample data flow diagram illustrating a hypothetical kernel-mode driver.":::

Security Development Lifecycle (SDL) best practices and associated tools can be used by IHVs and OEMs to improve the security of their products. For more information, see [SDL recommendations for OEMs](../bringup/security-overview.md#sdl-recommendations-for-oems).

## Use CodeQL to check your driver code

**Security checklist item \#12:** *Use CodeQL to check for vulnerabilities in your driver code.*

CodeQL, by GitHub, is a semantic code analysis engine, and the combination of an extensive suite of security queries along with a robust platform make it a valuable tool for securing driver code. For more information, see [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).

## Use Driver Verifier to check for vulnerabilities

**Security checklist item \#13:** *Use Driver Verifier to check for vulnerabilities in your driver code.*

Driver Verifier uses a set of interface rules and a model of the operating system to determine whether the driver interacts correctly with the Windows operating system. Driver Verifier finds defects in driver code that could point to potential bugs in drivers.

Driver Verifier allows for live testing of the driver. Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. An attached debugger, allows viewing of OS and driver code execution in real time. Driver Verifier can subject the Windows drivers to a variety of stresses and tests to find improper behavior. For more information, see [Driver Verifier](../devtest/driver-verifier.md).

Driver Verifer works with both WDM and KMDF drivers. For the specifics of what it can check, see the following topics.

- [Rules for WDM Drivers](../devtest/sdv-rules-for-wdm-drivers.md)
- [Rules for KMDF Drivers](../devtest/sdv-rules-for-kmdf-drivers.md)

For more information about the drivers that Driver Verifier can work with, see [DDI Compliance Rules](../devtest/static-driver-verifier-rules.md) and [Supported Drivers](../devtest/supported-drivers.md). For the addtional verifier rules for specific types of drivers, see:

- [Rules for NDIS Drivers](../devtest/sdv-rules-for-ndis-drivers.md)
- [Rules for Storport Drivers](../devtest/sdv-rules-for-storport-drivers.md)
- [Rules for Audio Drivers](../devtest/rules-for-audio-drivers.md)
- [Rules for AVStream Drivers](../devtest/rules-for-avstream-drivers.md)

To become familiar with DV, you can use one of the sample drivers (for example, the featured toaster sample: <https://github.com/Microsoft/Windows-driver-samples/tree/main/general/toaster/toastDrv/kmdf/func/featured>).

## Check code with the hardware compatibility program tests

**Security checklist item \#14:** *Use the security related hardware compatibility program tests to check for security issues.*

The hardware compatibility program includes security related tests can be used to look for code vulnerabilities. The Windows Hardware Compatibility Program leverages the tests in the Windows Hardware Lab Kit (HLK). The HLK Device Fundamentals tests can be used on the command line to exercise driver code and probe for weakness. For general information about the device fundamentals tests and the hardware compatibility program, see [Windows Hardware Lab Kit](/windows-hardware/test/hlk/).

The following tests are examples of tests that may be useful to check driver code for some behaviors associated with code vulnerabilities:

 [DF - Fuzz random IOCTL test (Reliability)](/windows-hardware/test/hlk/testref/236b8ad5-0ba1-4075-80a6-ae9dafb71c94)

 [DF - Fuzz sub-opens test (Reliability)](/windows-hardware/test/hlk/testref/92bf534e-aa48-4aeb-b3cd-e46fb7cc7d80)

 [DF - Fuzz zero length buffer FSCTL test (Reliability)](/windows-hardware/test/hlk/testref/5f5f6c7e-d5db-4ff1-8cee-da47203ab070)

 [DF - Fuzz random FSCTL test (Reliability)](/windows-hardware/test/hlk/testref/e529e34e-076a-4978-926f-7eca333e8f4d)

 [DF - Fuzz Misc API test (Reliability)](/windows-hardware/test/hlk/testref/fb305d04-6e8c-4dfc-9984-9692df82fbd8)

 You can also use the [Kernel synchronization delay fuzzing](../devtest/kernel-synchronization-delay-fuzzing.md) that is included with Driver Verifier.

The CHAOS (Concurrent Hardware and Operating System) tests run various PnP driver tests, device driver fuzz tests, and power system tests concurrently. For more information, see [CHAOS Tests (Device Fundamentals)](../devtest/chaos-tests--device-fundamentals-.md).

The Device Fundamentals Penetration tests perform various forms of input attacks, which are a critical component of security testing. Attack and Penetration testing can help identify vulnerabilities in software interfaces. For more information, see [Penetration Tests (Device Fundamentals)](../devtest/penetration-tests--device-fundamentals-.md).

Use the [Device Guard - Compliance Test](/windows-hardware/test/hlk/testref/10c242b6-49f6-491d-876c-c39b22b36abc), along with the other tools described in this article, to confirm that your driver is HVCI compatible.

### Custom and domain-specific test tools

Consider the development of custom domain-specific security tests. To develop additional tests, gather input from the original designers of the software, as well as unrelated development resources familiar with the specific type of driver being developed, and one or more people familiar with security intrusion analysis and prevention.

## Check ready to ship drivers with tools like BinSkim and SignTool

**Security checklist item \#15:** *Check compiled code with the tools like BinSkim and SignTool before it is uploaded to partner center.*

Use tools like BinSkim and SignTool to examine binary files to check compiled code before it is uploaded to the partner center to be distributed using Windows Update. Having tools in place to check compiled binaries, before they are submited for distribution, adds in another layer of protection.

### BinSkim

BinSkim can identify coding and building practices that can potentially render the binary vulnerable. BinSkim checks for:

- Use of outdated compiler tool sets - Binaries should be compiled against the most recent compiler tool sets wherever possible to maximize the use of current compiler-level and OS-provided security mitigations.
- Insecure compilation settings - Binaries should be compiled with the most secure settings possible to enable OS-provided security mitigations, maximize compiler errors and actionable warnings reporting, among other things.
- Signing issues - Signed binaries should be signed with cryptographically-strong algorithms.

BinSkim is an open source tool and generates output files that use the Static Analysis Results Interchange Format ([SARIF](https://github.com/oasis-tcs/sarif-spec)) format. BinSkim replaces the former [BinScope](https://www.microsoft.com/security/blog/2014/11/20/new-binscope-released/) tool.

For more information about BinSkim, see [Use BinSkim to check binaries](binskim-check-binaries.md) and the [BinSkim User Guide](https://github.com/microsoft/binskim/blob/master/docs/UserGuide.md).

### SignTool

Use SignTool to check release-signed driver files. For more information, see [Verifying the Signature of a Release-Signed Driver File](../install/verifying-the-signature-of-a-release-signed-driver-file.md) and [Verifying the Signature of a Catalog File Signed by a Commercial Release Certificate](../install/verifying-the-signature-of-a-catalog-file-signed-by-a-commercial-relea.md).

## Do not production sign test code

**Security checklist item \#16:** *Do not production code sign development, testing, and manufacturing kernel driver code.*

Kernel driver code that is used for development, testing, or manufacturing might include dangerous capabilities that pose a security risk. This dangerous code should never be signed with a certificate that is trusted by Windows. The correct mechanism for executing dangerous driver code is to disable UEFI Secure Boot, enable the BCD "TESTSIGNING", and sign the development, test, and manufacturing code using an untrusted certificate (for example, one generated by makecert.exe).

Code signed by a trusted Software Publishers Certificate (SPC) or Windows Hardware Quality Labs (WHQL) signature must not facilitate bypass of Windows code integrity and security technologies. Before code is signed by a trusted SPC or WHQL signature, first ensure it complies with guidance from [Creating Reliable Kernel-Mode Drivers](../kernel/creating-reliable-kernel-mode-drivers.md). In addition the code must not contain any dangerous behaviors, described below. 

Examples of dangerous behavior include the following:

- Providing the ability to map arbitrary kernel, physical, or device memory to user mode.
- Providing the ability to read or write arbitrary kernel, physical or device memory, including Port input/output (I/O).
- Providing access to storage that bypasses Windows access control.
- Providing the ability to modify hardware or firmware that the driver was not designed to manage.

## Execute proper release driver signing and distribute your driver package using Windows Update 

**Security checklist item \#17:** *Use the Windows partner portal to submit your driver package to be signed and distributed via Windows Update.*

Before you release a driver package to the public, you submit the package for certification. For more information, see [Test for performance and compatibility](/windows-hardware/test/index) and [Get started with the Hardware program](../dashboard/get-started-dashboard-submissions.md).

Using Windows Update is strongly recommended for the distribution of driver packages. Windows Update provides a robust, secure, globally scaled, and regulatory compliant distribution system that should be used to deliver driver updates. For more information, see [Distributing a driver package](../develop/distributing-a-driver-package.md).

Use gradual rollout and [Driver flighting](../dashboard/driver-flighting.md) in the [Partner Center for Windows Hardware](../dashboard/index.md) to distribute your driver package within defined Windows Insider rings, while providing automatic monitoring and evaluation. Monitor the roll out of the driver using the [Microsoft driver measures](../dashboard/overview-of-microsoft-driver-measure-dictionary.md), such as [Percent of Machines Without a Kernel Mode Crash](../dashboard/pct-machines-without-kernel-mode-crash.md) to maintain quality. 

For a description of safe software deployment practices refer to the CISA [Safe Software Deployment: How Software Manufacturers Can Ensure Reliability for Customers](https://www.cisa.gov/sites/default/files/2024-10/safe-software-deployment-how-software-manufacturers-can-ensure-reliability-for-customers-508c.pdf).

## Understand how drivers are reported using the *Microsoft Vulnerable and Malicious Driver Reporting Center*

**Security checklist item \#18:** Understand how drivers are reported using the *Microsoft Vulnerable and Malicious Driver Reporting Center*

Anyone can submit a questionable driver using the *Microsoft Vulnerable and Malicious Driver Reporting Center*. Refer to this blog entry for information on how drivers are submitted for analysis - [Improve kernel security with the new Microsoft Vulnerable and Malicious Driver Reporting Center](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)

The Reporting Center can scan and analyze Windows drivers built for x86 and x64 architectures. Vulnerable and malicious scanned drivers are flagged for analysis and investigation by Microsoft’s Vulnerable Driver team. After vulnerable drivers are confirmed, an appropriate notification occurs, they are added to the vulnerable driver blocklist. For more information about that, see [Microsoft recommended driver block rules](/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules). These rules are applied by default to Hypervisor-protected code integrity (HVCI) enabled devices and Windows 10 in S mode.

## Review secure coding resources

**Security checklist item \#19:** *Review these resources to expand your understanding of the secure coding best practices that are applicable to driver developers.*

### NIST known software vulnerability database 

The National Vulnerability Database (NVD) is a searchable repository of security-related software flaws, including Windows drivers.

[Search NIST Vulnerability Database](https://nvd.nist.gov/vuln/search)

[National Vulnerability Database Overview](https://nvd.nist.gov/) 

### Secure coding standards

Carnegie Mellon University SEI CERT - [C Coding Standard: Rules for Developing Safe, Reliable, and Secure Systems (PDF)](https://resources.sei.cmu.edu/downloads/secure-coding/assets/sei-cert-c-coding-standard-2016-v01.pdf).

MITRE - [Weaknesses Addressed by the CERT C Secure Coding Standard](https://cwe.mitre.org/data/definitions/734.html)

### Secure coding organizations

[Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/)

[CISA Resources](https://www.cisa.gov/resources-tools/resources)

SAFECode - [https://safecode.org/](https://safecode.org/)

[Carnegie Mellon University SEI CERT](https://www.sei.cmu.edu/about/divisions/cert/index.cfm)

### OSR

[OSR](https://www.osr.com) provides driver development training and consulting services. These articles from the OSR newsletter highlight driver security issues.

[Names, Security Descriptors and Device Classes - Making Device Objects Accessible… and SAFE](https://www.osr.com/nt-insider/2017-issue1/making-device-objects-accessible-safe/)

[You've Gotta Use Protection -- Inside Driver & Device Security](https://www.osronline.com/article.cfm^article=100.htm)

[Locking Down Drivers - A Survey of Techniques](https://www.osronline.com/article.cfm^article=357.htm)

[Meltdown and Spectre: What about drivers?](https://www.osr.com/blog/2018/01/23/meltdown-spectre-drivers/)

### Driver vulnerability case study

[From alert to driver vulnerability: Microsoft Defender ATP investigation unearths privilege escalation flaw](https://www.microsoft.com/security/blog/2019/03/25/from-alert-to-driver-vulnerability-microsoft-defender-atp-investigation-unearths-privilege-escalation-flaw/)

### Software supply chain security and Software Bill of Materials (SBOMs)

[The Supply Chain Integrity, Transparency and Trust (SCITT) initiative](https://scitt.io/) 

[Generating Software Bills of Materials (SBOMs) with SPDX at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/generating-software-bills-of-materials-sboms-with-spdx-at-microsoft/)

[Microsoft open sources its software bill of materials (SBOM) generation tool](https://devblogs.microsoft.com/engineering-at-microsoft/microsoft-open-sources-software-bill-of-materials-sbom-generation-tool/)


### Books

*24 Deadly Sins of Software Security: Programming Flaws and How to Fix Them* by Michael Howard, David LeBlanc, and John Viega

*Writing Secure Software Second Edition*, Michael Howard and David LeBlanc

*The Art of Software Security Assessment: Identifying and Preventing Software Vulnerabilities*, Mark Dowd, John McDonald and Justin Schuh

*Secure Coding in C and C++ (SEI Series in Software Engineering) 2nd Edition*, Robert C. Seacord

*Programming the Microsoft Windows Driver Model (2nd Edition)*, Walter Oney

*Developing Drivers with the Windows Driver Foundation (Developer Reference)*, Penny Orwick and Guy Smith

### Training

Windows driver classroom training is available from vendors such as the following:

- [OSR](https://www.osr.com)
- [Winsider](https://www.windows-internals.com/)

Secure coding online training is available from a variety of sources. For example, this course is available from coursera on:

[Identifying Security Vulnerabilities in C/C++ Programming](https://www.coursera.org/learn/identifying-security-vulnerabilities-c-programming).

SAFECode offers free training as well:

[SAFECode.org/training](https://safecode.org/training/)

### Professional Certification

 CERT offers a [Secure Coding Professional Certification](https://www.sei.cmu.edu/education-outreach/credentials/index.cfm).

## Summary of key takeaways

Driver security is a complex undertaking containing many elements, but here are a few key points to consider:

- Drivers live in the windows kernel, and having an issue when executing in kernel exposes the entire operating system. Because of this, pay close attention to driver security and design with security in mind.

- Apply the principle of least privilege:

    a. Use a strict SDDL string to restrict access to the driver

    b. Further restrict individual IOCTL's

- Create a threat model to identify attack vectors and consider whether anything can be restricted further.

- Be careful with regard to embedded pointers being passed in from usermode. They need to be probed, accessed within try except, and they are prone to time of check time of use (ToCToU) issues unless the value of the buffer is captured and compared.

- If you're unsure, use METHOD_BUFFERED as an IOCTL buffering method.

- Use code scanning utilities such as CodeQL to look for known code vulnerabilities and remediate any identified issues.

- Seek out knowledgeable code reviewers to look for issues that you may have missed.

- Use driver verifiers and test your driver with multiple inputs, including corner cases.
