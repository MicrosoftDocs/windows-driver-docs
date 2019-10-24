---
title: Driver security checklist
description: This article provides a driver security checklist for driver developers.
ms.assetid: 25375E02-FCA1-4E94-8D9A-AA396C909278
ms.date: 04/02/2019
ms.localizationpriority: medium
---

# Driver security checklist

This article provides a driver security checklist for driver developers to help reduce the risk of drivers being compromised.

## <span id="Driver_Security_Overview"></span><span id="driver_security_overview"></span><span id="DRIVER_SECURITY_OVERVIEW"></span>Driver security overview

A security flaw is any flaw that allows an attacker to cause a driver to malfunction in such a way that it causes the system to crash or become unusable. In addition, vulnerabilities in driver code can allow an attacker to gain access to the kernel, creating a possibility of compromising the entire OS. When most developers are working on their driver, their focus is on getting the driver to work properly, and not on whether a malicious attacker will attempt to exploit vulnerabilities within their code.

After a driver is released, however, attackers can attempt to probe and identify security flaws. Developers must consider these issues during the design and implementation phase in order to minimize the likelihood of such vulnerabilities. The goal is to eliminate all known security flaws before the driver is released.

Creating more secure drivers requires the cooperation of the system architect (consciously thinking of potential threats to the driver), the developer implementing the code (defensively coding common operations that can be the source of exploits), and the test team (proactively attempting to find weakness and vulnerabilities). By properly coordinating all of these activities, the security of the driver is dramatically enhanced.

In addition to avoiding the issues associated with a driver being attacked, many of the steps described, such as more precise use of kernel memory, will increase the reliability of your driver. This will reduce support costs and increase customer satisfaction with your product. Completing the tasks in the checklist below will help to achieve all these goals.

**Security checklist:** *Complete the security task described in each of these topics.*

![empty checkbox](images/checkbox.png)[Confirm that a kernel driver is required](#confirmkernel)

![empty checkbox](images/checkbox.png)[Use the driver frameworks](#confirmkernel)

![empty checkbox](images/checkbox.png)[Control access to software only drivers](#controlsoftwareonly)

![empty checkbox](images/checkbox.png)[Do not production sign test driver code](#donotproductionsign) 

![empty checkbox](images/checkbox.png)[Perform threat analysis](#threatanalysis)

![empty checkbox](images/checkbox.png)[Follow driver secure coding guidelines](#driversecuritycodepractices)

![empty checkbox](images/checkbox.png)[Validate Device Guard compatibility](#dgc)

![empty checkbox](images/checkbox.png)[Follow technology specific code best practices](#technologyspecificcodepractices)

![empty checkbox](images/checkbox.png)[Perform peer code review](#peercodereview)

![empty checkbox](images/checkbox.png)[Manage driver access control](#managingdriveraccesscontrol)

![empty checkbox](images/checkbox.png)[Enhance device installation security](#enhancedeviceinstallationsecurity)

![empty checkbox](images/checkbox.png)[Execute proper release driver signing](#releasedriversigning)

![empty checkbox](images/checkbox.png)[Use code analysis in Visual Studio to investigate driver security](#use-code-analysis)

![empty checkbox](images/checkbox.png)[Use Static Driver Verifier to Check for Vulnerabilities](#sdv)

![empty checkbox](images/checkbox.png)[Check code with Binscope Binary Analyzer](#binscope)

![empty checkbox](images/checkbox.png)[Use code validation tools](#codevalidationtools)

![empty checkbox](images/checkbox.png)[Review debugger techniques and extensions](#debugger)

![empty checkbox](images/checkbox.png)[Review secure coding resources](#securecodingresources)

[Summary of key takeaways](#keytakeaways)

## <span id="confirmkernel"></span>Confirm that a kernel driver is required

**Security checklist item \#1:** *Confirm that a kernel driver is required and that a lower risk approach, such as Windows service or app, is not a better option.*

Drivers live in the Windows kernel, and having an issue when executing in kernel exposes the entire operating system. If any other option is available, it likely will be lower cost and have less associated risk than creating a new kernel driver.
For more information about using the built in Windows drivers, see [Do you need to write a driver?](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/do-you-need-to-write-a-driver-).

For information on using background tasks, see  [Support your app with background tasks](https://docs.microsoft.com/windows/uwp/launch-resume/support-your-app-with-background-tasks).

For information on using Windows Services, see [Services](https://docs.microsoft.com/windows/desktop/Services/services).

## <span id="confirmkernel"></span>Use the driver frameworks 

**Security checklist item \#2:** *Use the driver frameworks to reduce the size of your code and increase it's reliability and security.*

Use the [Windows Driver Frameworks](https://docs.microsoft.com/windows-hardware/drivers/wdf/) to reduce the size of your code and increase it's reliability and security.  To get started, review [Using WDF to Develop a Driver](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-the-framework-to-develop-a-driver). For information on using the lower risk user mode framework driver (UMDF), see [Choosing a driver model](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/choosing-a-driver-model).

Writing an old fashion [Windows Driver Model (WDM)](https://docs.microsoft.com/windows-hardware/drivers/kernel/windows-driver-model) driver is more time consuming, costly, and almost always involves recreating code that is available in the driver frameworks.

The Windows Driver Framework source code is open source and available on GitHub. This is the same source code from which the WDF runtime library that ships in Windows 10 is built. You can debug your driver more effectively when you can follow the interactions between the driver and WDF. Download it from [https://github.com/Microsoft/Windows-Driver-Frameworks](https://github.com/Microsoft/Windows-Driver-Frameworks).


## <span id="controlsoftwareonly"></span>Control access to software only drivers

**Security checklist item \#3:** *If a software-only driver is going to be created, additional access control must be implemented.*

Software-only kernel drivers do not use plug-and-play (PnP) to become associated with specific hardware IDs, and can run on any PC. Such a driver could be used for purposes other than the one originally intended, creating an attack vector. 

Because software-only kernel drivers contain additional risk, they must be limited to run on specific hardware (for example, by using a unique PnP ID to enable creation of a PnP driver, or by checking the SMBIOS table for the presence of specific hardware).

For example, imagine OEM Fabrikam wants to distribute a driver that enables an overclocking utility for their systems.  If this software-only driver were to execute on a system from a different OEM, system instability or damage might result.  Fabrikam’s systems should include a unique PnP ID to enable creation of a PnP driver that is also updatable through Windows Update.  If this is not possible, and Fabrikam authors a Legacy driver, that driver should find another method to verify that it is executing on a Fabrikam system (for example, by examination of the SMBIOS table prior to enabling any capabilities). 


## <span id="donotproductionsign"></span> Do not production sign test code

**Security checklist item \#4:** *Do not production code sign development, testing, and manufacturing kernel driver code.*

Kernel driver code that is used for development, testing, or manufacturing might include dangerous capabilities that pose a security risk.  This dangerous code should never be signed with a certificate that is trusted by Windows.  The correct mechanism for executing dangerous driver code is to disable UEFI Secure Boot, enable the BCD “TESTSIGNING”, and sign the development, test, and manufacturing code using an untrusted certificate (for example, one generated by makecert.exe).

Code signed by a trusted Software Publishers Certificate (SPC) or Windows Hardware Quality Labs (WHQL) signature must not facilitate bypass of Windows code integrity and security technologies.  Before code is signed by a trusted SPC or WHQL signature, first ensure it complies with guidance from [Creating Reliable Kernel-Mode Drivers](https://docs.microsoft.com/windows-hardware/drivers/kernel/creating-reliable-kernel-mode-drivers). In addition the code must not contain any dangerous behaviors, described below.  For more information about driver signing, see [Release driver signing](#releasedriversigning) later in this article.

Examples of dangerous behavior include the following:

- Providing the ability to map arbitrary kernel, physical, or device memory to user mode.
- Providing the ability to read or write arbitrary kernel, physical or device memory, including Port input/output (I/O).
- Providing access to storage that bypasses Windows access control. 
- Providing the ability to modify hardware or firmware that the driver was not designed to manage.  


## <span id="ThreatAnalysis"></span><span id="threatanalysis"></span><span id="THREATANALYSIS"></span>Perform threat analysis


**Security checklist item \#5:** *Either modify an existing driver threat model or create a custom threat model for your driver.*

In considering security, a common methodology is to create specific threat models that attempt to describe the types of attacks that are possible. This technique is useful when designing a driver because it forces the developer to consider the potential attack vectors against a driver in advance. Having identified potential threats, a driver developer can then consider means of defending against these threats in order to bolster the overall security of the driver component.

This article provides driver specific guidance for creating a lightweight threat model: [Threat modeling for drivers](threat-modeling-for-drivers.md). The article provides an example driver threat model diagram that can be used as a starting point for your driver.

![Sample data flow diagram for hypothetical kernel-mode driver](images/sampledataflowdiagramkernelmodedriver.gif)

Security Development Lifecycle (SDL) best practices and associated tools can be used by IHVs and OEMs to improve the security of their products. For more information see [SDL recommendations for OEMs](https://docs.microsoft.com/en-us/windows-hardware/drivers/bringup/security-overview#sdl-recommendations-for-oems).


## <span id="DriverSecurityCodePractices"></span><span id="driversecuritycodepractices"></span><span id="DRIVERSECURITYCODEPRACTICES"></span>Follow driver secure coding guidelines

**Security checklist item \#6:** *Review your code and remove any known code vulnerabilities.*

The core activity of creating secure drivers is identifying areas in the code that need to be changed to avoid known software vulnerabilities. Many of these known software vulnerabilities deal with keeping strict track of the use of memory to avoid issues with others overwriting or otherwise comprising the memory locations that your driver uses.

The [Code Validation Tools](#codevalidationtools) section of this article describes software tools that can be used to help locate known software vulnerabilities.


**Memory buffers**

- Always check the sizes of the input and output buffers to ensure that the buffers can hold all the requested data. For more information, see [Failure to Check the Size of Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-check-the-size-of-buffers).

- Properly initialize all output buffers with zeros before returning them to the caller. For more information, see [Failure to Initialize Output Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-initialize-output-buffers).

- Validate variable-length buffers. For more information, see [Failure to Validate Variable-Length Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-validate-variable-length-buffers). For more information about working with buffers and using [**ProbeForRead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) and [**ProbeForWrite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite) to validate the address of a buffer, see [Buffer Handling](https://docs.microsoft.com/windows-hardware/drivers/ifs/buffer-handling).


**Use the appropriate method for accessing  data buffers with IOCTLs**

One of the primary responsibilities of a Windows driver is transferring data between user-mode applications and a system's devices. The three methods for accessing data buffers are shown in the following table. 

|IOCTL Buffer Type | Summary                                    | For more information |  
|------------------|--------------------------------------------|-------------------------------------------------------------------------|
| METHOD_BUFFERED  |Recommended for most situtations            | [Using Buffered I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/using-buffered-i-o)
| METHOD_IN_DIRECT or METHOD_OUT_DIRECT |Used in some high speed HW I/O    |[Using Direct I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/using-direct-i-o) |
| METHOD_NEITHER |Avoid if possible |[Using Neither Buffered Nor Direct I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/using-neither-buffered-nor-direct-i-o)|

In general buffered I/O is recommended as it provides the most secure buffering methods. But even when using buffered I/O there are risks, such as embedded pointers that must be mitigated.

For more information about working with buffers in IOCTLs, see [Methods for Accessing Data Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/methods-for-accessing-data-buffers).

**Errors in use of IOCTL buffered I/O**

- Check the size of IOCTL related buffers. For more information, see [Failure to Check the Size of Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-check-the-size-of-buffers).
 
- Properly initialize output buffers. For more information, see [Failure to Initialize Output Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-initialize-output-buffers).

- Properly validate variable-length buffers. For more information, see [Failure to Validate Variable-Length Buffers](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-validate-variable-length-buffers).

- When using buffered I/O, be sure and return the proper length for the OutputBuffer in the [IO_STATUS_BLOCK](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure Information field.  Don't just directly return the length directly from a READ request.  For example, consider a situation where the returned data from the user space indicates that there is a 4K buffer.  If the driver actually should only return 200 bytes, but instead just returns 4K in the Information field an information disclosure vulnerability has occurred. This problem occurs because in earlier versions of Windows, the buffer the I/O Manager uses for Buffered I/O is not zeroed.  Thus, the user app gets back the original 200 bytes of data plus 4K-200 bytes of whatever was in the buffer (non-paged pool contents). This scenario can occur with all uses of Buffered I/O and not just with IOCTLs.

**Errors in IOCTL direct I/O**

Handle zero-length buffers correctly. For more information, see [Errors in Direct I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-direct-i-o).

**Errors in referencing user-space addresses**
- Validate pointers embedded in buffered I/O requests. For more information, see [Errors in Referencing User-Space Addresses](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-referencing-user-space-addresses).

- Validate any address in the user space before trying to use it, using APIs such as [**ProbeForRead**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread) and [**ProbeForWrite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite) when appropriate. 

**TOCTOU vulnerabilities**

There is a [potential time of check to time of use](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use) (TOCTOU) vulnerability when using direct I/O (for IOCTLs or for Read/Write).  Be aware that the driver is accessing the user data buffer, the user can simultaneously be accessing it. 

To manage this risk, copy any parameters that need to be validated from the user data buffer to memory that is solely accessibly from kernel mode (such as the stack or pool).  Then once the data can not be accessed by the user application, validate and then operate on the data that was passed-in.

**Driver code must make correct use of memory**

- All driver pool allocations must be in non-executable (NX) pool. Using NX memory pools is inherently more secure than using executable non-paged (NP) pools, and provides better protection against overflow attacks. 

- Device drivers must properly handle various user-mode, as well as kernel to kernel I/O, requests. 

To allow drivers to support HVCI virtualization, there are additional memory requirements. For more information, see [Device Guard Compatibility](#dgc) later in this article.

**Handles**

- Validate handles passed between user-mode and kernel-mode memory. For more information, see [Handle Management](https://docs.microsoft.com/windows-hardware/drivers/ifs/handle-management) and [Failure to Validate Object Handles](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-validate-object-handles).

**Device objects**

- Secure device objects. For more information, see [Securing Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/securing-device-objects).

- Validate device objects. For more information, see [Failure to Validate Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-validate-device-objects).

**IRPs**

**WDF and IRPs** 

One advantage of using WDF, is that WDF drivers typically do not directly access IRPs. For example, the framework converts the WDM IRPs that represent read, write, and device I/O control operations to framework request objects that KMDF/UMDF receive in I/O queues. 

If you are writing a WDM driver, review the following guidance.

**Properly manage IRP I/O buffers**

The following articles provide information about validating IRP input values:

[DispatchReadWrite Using Buffered I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/dispatchreadwrite-using-buffered-i-o)

[Errors in Buffered I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-buffered-i-o)

[DispatchReadWrite Using Direct I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/dispatchreadwrite-using-direct-i-o)

[Errors in Direct I/O](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-direct-i-o)

[Security Issues for I/O Control Codes](https://docs.microsoft.com/windows-hardware/drivers/kernel/security-issues-for-i-o-control-codes)

Consider validating values that are associated with an IRP, such as buffer addresses and lengths. 

If you chose to use Neither I/O, be aware that unlike Read and Write, and unlike Buffered I/O and Direct I/O, that when using Neither I/O IOCTL the buffer pointers and lengths are not validated by the I/O Manager.  


**Handle IRP completion operations properly**

A driver must never complete an IRP with a status value of STATUS\_SUCCESS unless it actually supports and processes the IRP. For information about the correct ways to handle IRP completion operations, see [Completing IRPs](https://docs.microsoft.com/windows-hardware/drivers/kernel/completing-irps).

**Manage driver IRP pending state**

The driver should mark the IRP pending before it saves the IRP, and should consider including both the call to [**IoMarkIrpPending**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) and the assignment in an interlocked sequence. For more information, see [Failure to Check a Driver's State](https://docs.microsoft.com/windows-hardware/drivers/kernel/failure-to-check-a-driver-s-state) and [Holding Incoming IRPs When A Device Is Paused](https://docs.microsoft.com/windows-hardware/drivers/kernel/holding-incoming-irps-when-a-device-is-paused).

**Handle IRP cancellation operations properly**

Cancel operations can be difficult to code properly because they typically execute asynchronously. Problems in the code that handles cancel operations can go unnoticed for a long time, because this code is typically not executed frequently in a running system. Be sure to read and understand all of the information supplied under [Canceling IRPs](https://docs.microsoft.com/windows-hardware/drivers/kernel/canceling-irps). Pay special attention to [Synchronizing IRP Cancellation](https://docs.microsoft.com/windows-hardware/drivers/kernel/synchronizing-irp-cancellation) and [Points to Consider When Canceling IRPs](https://docs.microsoft.com/windows-hardware/drivers/kernel/points-to-consider-when-canceling-irps).

One recommended way to minimize the synchronization problems that are associated with cancel operations is to implement a [cancel-safe IRP queue](https://docs.microsoft.com/windows-hardware/drivers/kernel/cancel-safe-irp-queues).

**Handle IRP cleanup and close operations properly**

Be sure that you understand the difference between [**IRP\_MJ\_CLEANUP**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-cleanup) and [**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close) requests. Cleanup requests arrive after an application closes all handles on a file object, but sometimes before all I/O requests have completed. Close requests arrive after all I/O requests for the file object have been completed or canceled. For more information, see the following articles:

[DispatchCreate, DispatchClose, and DispatchCreateClose Routines](https://docs.microsoft.com/windows-hardware/drivers/kernel/dispatchcreate--dispatchclose--and-dispatchcreateclose-routines)

[DispatchCleanup Routines](https://docs.microsoft.com/windows-hardware/drivers/kernel/dispatchcleanup-routines)

[Errors in Handling Cleanup and Close Operations](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-handling-cleanup-and-close-operations)

For more information about handling IRPs correctly, see [Additional Errors in Handling IRPs](https://docs.microsoft.com/windows-hardware/drivers/kernel/additional-errors-in-handling-irps).

**Other security issues**

- Use a lock or an interlocked sequence to prevent race conditions. For more information, see [Errors in a Multiprocessor Environment](https://docs.microsoft.com/windows-hardware/drivers/kernel/errors-in-a-multiprocessor-environment).

- Ensure that device drivers properly handle various user-mode as well as kernel to kernel I/O requests.

- Ensure that no TDI filters or LSPs are installed by the driver or associated software packages during installation or usage. 

**Use safe functions**

- Use safe string functions. For more information, see [Using Safe String Functions](https://docs.microsoft.com/windows-hardware/drivers/kernel/using-safe-string-functions).

- Use safe arithmetic functions. For more information, see [Arithmetic Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/index) in [Safe Integer Library Routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/index)

- Use safe conversion functions. For more information, see [Conversion Functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/index) in [Safe Integer Library Routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/index)

**Additional code vulnerabilities**

In addition to the possible vulnerabilities covered here, this article provides additional information about enhancing the security of kernel mode driver code: [Creating Reliable Kernel-Mode Drivers](https://docs.microsoft.com/windows-hardware/drivers/kernel/creating-reliable-kernel-mode-drivers).

For additional information about C and C++ secure coding, see [Secure coding resources](#securecodingresources) at the end of this article.



## <span id="ManagingDriverAccessControl"></span><span id="managingdriveraccesscontrol"></span><span id="MANAGINGDRIVERACCESSCONTROL"></span>Manage driver access control

**Security checklist item \#7:** *Review your driver to make sure that you are properly controlling access.*

**Managing driver access control - WDF**

Drivers must work to prevent users from inappropriately accessing a computer's devices and files. To prevent unauthorized access to devices and files, you must:

-   Name device objects only when necessary. Named device objects are generally only necessary for legacy reasons, for example if you have an application that expects to open the device using a particular name or if you’re using a non-PNP device/control device.  Note that WDF drivers do not need to name their PnP device FDO in order to create a symbolic link using [WdfDeviceCreateSymbolicLink](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatesymboliclink).

-   Secure access to device objects and interfaces. 

In order to allow applications or other WDF drivers to access your PnP device PDO, you should use device interfaces. For more information, see [Using Device Interfaces](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-device-interfaces). A device interface serves as a symbolic link to your device stack’s PDO. 

One of the betters way to control access to the PDO is by specifying an SDDL string in your INF. If the SDDL string is not in the INF file, Windows will apply a default security descriptor. For more information, see [Securing Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/securing-device-objects) and [SDDL for Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/sddl-for-device-objects). 

For more information about controlling access, see the following articles:

[Controlling Device Access in KMDF Drivers](https://docs.microsoft.com/windows-hardware/drivers/wdf/controlling-device-access-in-kmdf-drivers)

[Names, Security Descriptors and Device Classes - Making Device Objects Accessible… and SAFE](https://www.osr.com/nt-insider/2017-issue1/making-device-objects-accessible-safe/) from the *January February 2017 The NT Insider Newsletter* published by [OSR](https://www.osr.com).


**Managing driver access control - WDM**

If you are working with a WDM Driver and you used a named device object you can use [IoCreateDeviceSecure](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) and specify a SDDL to secure it. When you implement [IoCreateDeviceSecure](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure) always specify a custom class GUID for DeviceClassGuid. You should not specify an existing class GUID here. Doing so has the potential to break security settings or compatibility for other devices belonging to that class. For more information, see [WdmlibIoCreateDeviceSecure](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdmsec/nf-wdmsec-wdmlibiocreatedevicesecure).
   
For more information, see the following articles:

[Controlling Device Access](https://docs.microsoft.com/windows-hardware/drivers/kernel/controlling-device-access)

[Controlling Device Namespace Access](https://docs.microsoft.com/windows-hardware/drivers/kernel/controlling-device-namespace-access)

[Windows security model for driver developers](windows-security-model.md)


**Security Identifiers (SIDs) risk hierarchy** 

The following section describes the risk hierarchy of the common SIDs used in driver code. For general information about SDDL, see [SDDL for Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/sddl-for-device-objects), [SID Strings](https://docs.microsoft.com/windows/desktop/SecAuthZ/sid-strings), and [SDDL String Syntax](https://docs.microsoft.com/openspecs/windows_protocols/ms-dtyp/f4296d69-1c0f-491f-9587-a960b292d070). 

It is important to understand that if lower privilege callers are allowed to access the kernel, code risk is increased. In this summary diagram, the risk increases as you allow lower privilege SIDs access to your driver functionality.

```cpp
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

**WDM Granular IOCTL security control**

To further manage security when IOCTLs are sent by user-mode callers, the driver code can include the [IoValidateDeviceIoControlAccess](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess) function. This function allows a driver to check access rights. Upon receiving an IOCTL, a driver can call [IoValidateDeviceIoControlAccess](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iovalidatedeviceiocontrolaccess), specifying FILE_READ_ACCESS, FILE_WRITE_ACCESS, or both. 

Implementing granular IOCTL security control does not replace the need to manage driver access using the techniques discussed above.

For more information, see the following articles:

[Defining I/O Control Codes](https://docs.microsoft.com/windows-hardware/drivers/kernel/defining-i-o-control-codes)


## <span id="DGC"></span><span id="dgc"></span>Validate Device Guard compatibility

**Security checklist item \#8:** *Validate that your driver uses memory so that it is Device Guard compatible.*

**Memory usage and Device Guard compatibility**

Device Guard uses hardware technology and virtualization to isolate the Code Integrity (CI) decision-making function from the rest of the operating system. When using virtualization-based security to isolate CI, the only way kernel memory can become executable is through a CI verification. This means that kernel memory pages can never be Writable and Executable (W+X) and executable code cannot be directly modified. 

To implement Device Guard compatible code, make sure your driver code does the following:

- Opts in to NX by default
- Uses NX APIs/flags for memory allocation (NonPagedPoolNx)
- Does not use sections that are both writable and executable
- Does not attempt to directly modify executable system memory
- Does not use dynamic code in kernel
- Does not load data files as executable
- Section alignment is a multiple of 0x1000 (PAGE\_SIZE). E.g. DRIVER\_ALIGNMENT=0x1000

For more information about using the tool and a list of incompatible memory calls, see [Use the Device Guard Readiness Tool to evaluate HVCI driver compatibility](use-device-guard-readiness-tool.md).

For general information about Device Guard, see [Driver compatibility with Device Guard in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/bg-p/WindowsHardwareCertification).

For more information about the related system fundamentals security test, see [Device Guard - Compliance Test](https://docs.microsoft.com/en-us/windows-hardware/test/hlk/testref/10c242b6-49f6-491d-876c-c39b22b36abc) and [Driver Compatibility with Device Guard](https://docs.microsoft.com/en-us/windows-hardware/test/hlk/testref/driver-compatibility-with-device-guard).



## <span id="technologyspecificcodepractices"></span>Follow technology-specific code best practices


**Security checklist item \#9:** *Review the following technology-specific guidance for your driver.*

*File Systems*

For more information, about file system driver security see the following articles:

[Security Considerations for File Systems](https://docs.microsoft.com/windows-hardware/drivers/ifs/security-considerations-for-file-systems)

[File System Security Issues](https://docs.microsoft.com/windows-hardware/drivers/ifs/file-system-security-issues)

[Security Features for File Systems](https://docs.microsoft.com/windows-hardware/drivers/ifs/security-features-for-file-systems)

[Security Considerations for File System Filter Drivers](https://docs.microsoft.com/windows-hardware/drivers/ifs/security-considerations-for-file-system-filter-drivers)

*NDIS - Networking*

For information about NDIS driver security, see [Security Issues for Network Drivers](https://docs.microsoft.com/windows-hardware/drivers/network/security-issues-for-network-drivers).

*Display*

For information about display driver security, see &lt;Content Pending&gt;.


*Printers*

For information related to printer driver security, see [V4 Printer Driver Security Considerations](https://docs.microsoft.com/windows-hardware/drivers/print/v4-printer-driver-security-considerations).

*Security Issues for Windows Image Acquisition (WIA) Drivers*

For information about WIA security, see [Security Issues for Windows Image Acquisition (WIA) Drivers](https://docs.microsoft.com/windows-hardware/drivers/image/security-issues-for-wia-drivers).



## <span id="enhancedeviceinstallationsecurity"></span>Enhance device installation security

**Security checklist item \#10:** *Review driver inf creation and installation guidance to make sure you are following best practices.*

When you create the code that installs your driver, you must make sure that the installation of your device will always be performed in a secure manner. A secure device installation is one that does the following:
 
- Limits access to the device and its device interface classes
- Limits access to the driver services that were created for the device
- Protects driver files from modification or deletion
- Limits access to the device's registry entries
- Limits access to the device's WMI classes
- Uses SetupAPI functions correctly

For more information, see the following articles:

[Creating Secure Device Installations](https://docs.microsoft.com/windows-hardware/drivers/install/creating-secure-device-installations)

[Guidelines for Using SetupAPI](https://docs.microsoft.com/windows-hardware/drivers/install/guidelines-for-using-setupapi)

[Using Device Installation Functions](https://docs.microsoft.com/windows-hardware/drivers/install/using-device-installation-functions)

[Device and Driver Installation Advanced Topics](https://docs.microsoft.com/windows-hardware/drivers/install/device-and-driver-installation-advanced-topics)



## <span id="peercodereview"></span>Perform peer code review

**Security checklist item \#11:** *Perform peer code review, to look for issues not surfaced by the other tools and processes*

Seek out knowledgeable code reviewers to look for issues that you may have missed. A second set of eyes will often see issues that you may have overlooked.

If you don't have suitable staff to review you code internally, consider engaging outside help for this purpose.



## <span id="ReleaseDriverSigning"></span><span id="releasedriversigning"></span><span id="RELEASEDRIVERSIGNING"></span>Execute proper release driver signing


**Security checklist item \#12:** *Use the Windows partner portal to properly sign your driver for distribution.*

Before you release a driver package to the public, we recommend that you submit the package for certification. For more information, see [Test for performance and compatibility](https://docs.microsoft.com/windows-hardware/test/index), [Get started with the Hardware program](https://docs.microsoft.com/windows-hardware/drivers/dashboard/get-started-with-the-hardware-dashboard), [Hardware Dashboard Services](https://docs.microsoft.com/windows-hardware/drivers/dashboard/dashboard-services), and [Attestation signing a kernel driver for public release](https://docs.microsoft.com/windows-hardware/drivers/dashboard/attestation-signing-a-kernel-driver-for-public-release).



## <span id="use-code-analysis"></span>Use code analysis in Visual Studio to investigate driver security

**Security checklist item \#13:** *Follow these steps to use the code analysis feature in Visual Studio to check for vulnerabilities in your driver code.*

Use the code analysis feature in Visual Studio to check for security vulnerabilities in your code. The Windows Driver Kit (WDK) installs rule sets that are designed to check for issues in native driver code.

For more information, see [How to run Code Analysis for drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/how-to-run-code-analysis-for-drivers).

For more information, see [Code Analysis for drivers overview](https://docs.microsoft.com/windows-hardware/drivers/devtest/code-analysis-for-drivers-overview). For additional background on code analysis, see [Visual Studio 2013 Static Code Analysis in depth](https://blogs.msdn.microsoft.com/hkamel/2013/10/24/visual-studio-2013-static-code-analysis-in-depth-what-when-and-how/).

To become familiar with code analysis, you can use one of the sample drivers for example, the featured toaster sample, <https://github.com/Microsoft/Windows-driver-samples/tree/master/general/toaster/toastDrv/kmdf/func/featured> or the ELAM Early Launch Anti-Malware sample <https://github.com/Microsoft/Windows-driver-samples/tree/master/security/elam>.

1. Open the driver solution in Visual Studio.

2. In Visual Studio, for each project in the solution change the project properties to use the desired rule set. For example: Project &gt;&gt; Properties &gt;&gt; Code Analysis &gt;&gt; General, select *Recommended driver rules*. In addition to using the recommenced driver rules, use the *Recommended native rules* rule set.

3. Select Build &gt;&gt; Run Code Analysis on Solution.

4. View warnings in the **Error List** tab of the build output window in Visual Studio.

Click on the description for each warning to see the problematic area in your code.

Click on the linked warning code to see additional information.

Determine whether your code needs to be changed, or whether an annotation needs to be added to allow the code analysis engine to properly follow the intent of your code. For more information on code annotation, see [Using SAL Annotations to Reduce C/C++ Code Defects](https://docs.microsoft.com/visualstudio/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects?view=vs-2015) and [SAL 2.0 Annotations for Windows Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/sal-2-annotations-for-windows-drivers).

For general information on SAL, refer to this article available from OSR.
https://www.osr.com/blog/2015/02/23/sal-annotations-dont-hate-im-beautiful/

## <span id="SDV"></span><span id="sdv"></span>Use Static Driver Verifier to check for vulnerabilities

**Security checklist item \#14:** *Follow these steps to use Static Driver Verifier (SDV) in Visual Studio to check for vulnerabilities in your driver code.*

Static Driver Verifier (SDV) uses a set of interface rules and a model of the operating system to determine whether the driver interacts correctly with the Windows operating system. SDV finds defects in driver code that could point to potential bugs in drivers.

For more information, see [Introducing Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/introducing-static-driver-verifier)
 and [Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier). Note that only certain types of drivers are supported by SDV. For more information about the drivers that SDV can verify, see [Supported Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/supported-drivers).

To become familiar with SDV, you can use one of the sample drivers (for example, the featured toaster sample: <https://github.com/Microsoft/Windows-driver-samples/tree/master/general/toaster/toastDrv/kmdf/func/featured>).

1. Open the targeted driver solution in Visual Studio.

2. In Visual Studio, change the build type to *Release*. Static Driver Verifier requires that the build type is release, not debug.

3. In Visual Studio, select Build &gt;&gt; Build Solution.

4. In Visual Studio, select Driver &gt;&gt; Launch Static Driver Verifier.

5. In SDV, on the *Rules* tab, select *Default* under *Rule Sets*.

Although the default rules find many common issues, consider running the more extensive *All driver rules* rule set as well.

6. On the *Main* tab of SDV, click *Start*.

7. When SDV is complete, review any warnings in the output. The *Main* tab displays the total number of defects found.

8. Click on each warning to load the SDV Report Page and examine the information associated with the possible code vulnerability. Use the report to investigate the verification result and to identify paths in your driver that fail a SDV verification. For more information, see [Static Driver Verifier Report](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier-report).




## <span id="BinScope"></span><span id="binscope"></span><span id="BINSCOPE"></span>Check code with BinScope Binary Analyzer

**Security checklist item \#15:** *Follow these steps to use BinScope to double check that compile and build options are configured to minimize known security issues.*

Use BinScope to examine application binary files to identify coding and building practices that can potentially render the application vulnerable to attack or to being used as an attack vector.

For more information, see [New Version of BinScope Binary Analyzer](https://www.microsoft.com/security/blog/2014/11/20/new-binscope-released/) and the user and getting started guides that are included with the tool download.


Follow these steps to validate that the security compile options are properly configured in the code that you are shipping:

1. Download BinScope Analyzer and related documents from here: <https://www.microsoft.com/download/details.aspx?id=44995>.

2. Review the *BinScope Getting Started Guide* that you downloaded.

3. Use the MSI file to install BinScope on the target test machine that contains the compiled code you wish to validate.

4. Open a command prompt window and execute the following command to examine a compiled driver binary. Update the path to point to your complied driver .sys file.

```cpp
C:\Program Files\Microsoft BinScope 2014>binscope "C:\Samples\KMDF_Echo_Driver\echo.sys" /verbose /html /logfile c:\mylog.htm 
```

5. Use a browser to review the BinScope report to confirm that all checks are marked (PASS).

By default, the HTML report is written to \\users\\&lt;username&gt;\\BinScope\\

There are three categories that may be output into a log file:

-   Failed checks \[Fail\]
-   Checks that didn’t complete \[Error\]
-   Passed checks \[Pass\]

Note that passed checks are not written to the log by default and must be enabled by using the /verbose switch.

```cpp
Results for Microsoft BinScope 2014 run on MyPC at 2017-01-28T00:18:48.3828242Z

Failed Checks
No failed checks. 
Passed Checks

• C:\Samples\KMDF_Echo_Driver\echo.sys - ATLVersionCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - ATLVulnCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - CompilerVersionCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - DBCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - DefaultGSCookieCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - ExecutableImportsCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - GSCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - GSFriendlyInitCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - GSFunctionSafeBuffersCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - HighEntropyVACheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - NXCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - RSA32Check (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - SafeSEHCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - SharedSectionCheck (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - VB6Check (PASS)
• C:\Samples\KMDF_Echo_Driver\echo.sys - WXCheck (PASS)

Checks Executed:
• ATLVersionCheck
• ATLVulnCheck
• CompilerVersionCheck
• DBCheck
• DefaultGSCookieCheck
• ExecutableImportsCheck
• GSCheck
• GSFriendlyInitCheck
• GSFunctionSafeBuffersCheck
• HighEntropyVACheck
• NXCheck
• RSA32Check
• SafeSEHCheck
• SharedSectionCheck
• VB6Check
• WXCheck

All Scanned Items

• C:\Samples\KMDF_Echo_Driver\echo.sys
```

## <span id="CodeValidationTools"></span><span id="codevalidationtools"></span><span id="CODEVALIDATIONTOOLS"></span>Use additional code validation tools

**Security checklist item \#16:** *Use these additional tools to help validate that your code follows security recommendations and to probe for gaps that were missed in your development process.*

In addition to [Visual Studio Code analysis](#use-code-analysis), [Static Driver Verifier](#sdv), and [Binscope](#binscope) discussed above, use the following tools to probe for gaps that were missed in your development process.

**Driver Verifier**

Driver Verifier allows for live testing of the driver. Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. Driver Verifier can subject the Windows drivers to a variety of stresses and tests to find improper behavior. For more information, see [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier).

**Hardware compatibility program tests**

The hardware compatibility program includes security related tests can be used to look for code vulnerabilities. The Windows Hardware Compatibility Program leverages the tests in the Windows Hardware Lab Kit (HLK). The HLK Device Fundamentals tests can be used on the command line to exercise driver code and probe for weakness. For general information about the device fundamentals tests and the hardware compatibility program, see [Windows Hardware Lab Kit](https://docs.microsoft.com/windows-hardware/test/hlk/).

The following tests are examples of tests that may be useful to check driver code for some behaviors associated with code vulnerabilities:

 [DF - Fuzz random IOCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/236b8ad5-0ba1-4075-80a6-ae9dafb71c94)

 [DF - Fuzz sub-opens test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/92bf534e-aa48-4aeb-b3cd-e46fb7cc7d80)

 [DF - Fuzz zero length buffer FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/5f5f6c7e-d5db-4ff1-8cee-da47203ab070)

 [DF - Fuzz random FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/e529e34e-076a-4978-926f-7eca333e8f4d)

 [DF - Fuzz Misc API test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/fb305d04-6e8c-4dfc-9984-9692df82fbd8)

 You can also use the [Kernel synchronization delay fuzzing](https://docs.microsoft.com/windows-hardware/drivers/devtest/kernel-synchronization-delay-fuzzing) that is included with Driver Verifier.

The CHAOS (Concurrent Hardware and Operating System) tests run various PnP driver tests, device driver fuzz tests, and power system tests concurrently. For more information, see [CHAOS Tests (Device Fundamentals)](https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/chaos-tests--device-fundamentals-).

The Device Fundamentals Penetration tests perform various forms of input attacks, which are a critical component of security testing. Attack and Penetration testing can help identify vulnerabilities in software interfaces. For more information, see [Penetration Tests (Device Fundamentals)](https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/penetration-tests--device-fundamentals-).

Use the [Device Guard - Compliance Test](https://docs.microsoft.com/en-us/windows-hardware/test/hlk/testref/10c242b6-49f6-491d-876c-c39b22b36abc), along with the other tools described in this article, to confirm that your driver is Device Guard compatible.


**Custom and domain-specific test tools**

Consider the development of custom domain-specific security tests. To develop additional tests, gather input from the original designers of the software, as well as unrelated development resources familiar with the specific type of driver being developed, and one or more people familiar with security intrusion analysis and prevention.



## <span id="Debugger"></span><span id="debugger"></span><span id="DEBUGGER"></span>Review debugger techniques and extensions


**Security checklist item \#17:** *Review these debugger tools and consider their use in your development debugging workflow.*

**!exploitable Crash Analyzer**

The !exploitable Crash Analyzer is a Windows debugger extensions that parses crash logs looking for unique issues. It also examines the type of crash and tries to determine whether the error is something that could be exploited by a malicious hacker.

Microsoft Security Engineering Center (MSEC), created the !exploitable Crash Analyzer. You can download the from codeplex: <https://msecdbg.codeplex.com/>.

For more information, see [!Exploitable crash analyzer version 1.6](https://www.microsoft.com/security/blog/2013/06/13/exploitable-crash-analyzer-version-1-6/) and the Channel 9 video [!exploitable Crash Analyzer](https://channel9.msdn.com/blogs/pdcnews/bang-exploitable-security-analyzer).

**Security related debugger commands**

The !acl extension formats and displays the contents of an access control list (ACL). For more information, see [Determining the ACL of an Object](https://docs.microsoft.com/windows-hardware/drivers/debugger/determining-the-acl-of-an-object) and [**!acl**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-acl).

The !token extension displays a formatted view of a security token object. For more information, see [**!token**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-token).

The !tokenfields extension displays the names and offsets of the fields within the access token object (the TOKEN structure). For more information, see [**!tokenfields**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-tokenfields).

The !sid extension displays the security identifier (SID) at the specified address. For more information, see [**!sid**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-sid).

The !sd extension displays the security descriptor at the specified address. For more information, see [**!sd**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-sd).


## <span id="SecureCodingResources"></span><span id="securecodingresources"></span><span id="SECURECODINGRESOURCES"></span>Review secure coding resources


**Security checklist item \#18:** *Review these resources to expand your understanding of the secure coding best practices that are applicable to driver developers.*

*Review these resources to learn more about driver security*

**Secure kernel-mode driver coding guidelines**

[Creating Reliable Kernel-Mode Drivers](https://docs.microsoft.com/windows-hardware/drivers/kernel/creating-reliable-kernel-mode-drivers)

**Secure coding organizations**

[Carnegie Mellon University SEI CERT](https://www.sei.cmu.edu/about/divisions/cert/index.cfm)

Carnegie Mellon University SEI CERT [C Coding Standard: Rules for Developing Safe, Reliable, and Secure Systems](https://www.securecoding.cert.org/confluence/display/c/SEI+CERT+C+Coding+Standard) (2016 Edition).

CERT - [Build Security In](https://www.us-cert.gov/bsi)

MITRE - [Weaknesses Addressed by the CERT C Secure Coding Standard](https://cwe.mitre.org/data/definitions/734.html)

Building Security In Maturity Model (BSIMM) - [https://www.bsimm.com/](https://www.bsimm.com/)

SAFECode - [https://safecode.org/](https://safecode.org/)


**OSR**

[OSR](https://www.osr.com) provides driver development training and consulting services. These articles from the OSR newsletter highlight driver security issues.

[Names, Security Descriptors and Device Classes - Making Device Objects Accessible… and SAFE](https://www.osr.com/nt-insider/2017-issue1/making-device-objects-accessible-safe/)

[You've Gotta Use Protection -- Inside Driver & Device Security](https://www.osronline.com/article.cfm^article=100.htm)

[Locking Down Drivers - A Survey of Techniques](https://www.osronline.com/article.cfm^article=357.htm) 

[Meltdown and Spectre: What about drivers?](https://www.osr.com/blog/2018/01/23/meltdown-spectre-drivers/) 

**Case Study**

[From alert to driver vulnerability: Microsoft Defender ATP investigation unearths privilege escalation flaw](https://www.microsoft.com/security/blog/2019/03/25/from-alert-to-driver-vulnerability-microsoft-defender-atp-investigation-unearths-privilege-escalation-flaw/)


**Books**

*24 deadly sins of software security : programming flaws and how to fix them* by Michael Howard, David LeBlanc and John Viega

*The art of software security assessment : identifying and preventing software vulnerabilities*, Mark Dowd, John McDonald and Justin Schuh

*Writing Secure Software Second Edition*, Michael Howard and David LeBlanc

*The Art of Software Security Assessment: Identifying and Preventing Software Vulnerabilities*, Mark Dowd and John McDonald

*Secure Coding in C and C++ (SEI Series in Software Engineering) 2nd Edition*, Robert C. Seacord

*Programming the Microsoft Windows Driver Model (2nd Edition)*, Walter Oney

*Developing Drivers with the Windows Driver Foundation (Developer Reference)*, Penny Orwick and Guy Smith 


**Training**

Windows driver classroom training is available from vendors such as the following:

- [OSR](https://www.osr.com) 
- [Winsider](https://www.windows-internals.com/)
- [Azius](https://azius.com/)

Secure coding online training is available from a variety of sources. For example, this course is available from coursera:

[https://www.coursera.org/learn/software-security](https://www.coursera.org/learn/software-security).

SAFECode offers free training as well:

[SAFECode.org/training](https://safecode.org/training/)

**Professional Certification**

 CERT offers a [Secure Coding Professional Certification](https://www.sei.cmu.edu/education-outreach/credentials/index.cfm).


## <span id="keytakeaways"></span>Summary of key takeaways

Driver security is a complex undertaking containing many elements, but here are a few key points to consider:

-   Drivers live in the windows kernel, and having an issue when executing in kernel exposes the entire operating system. Because of this, pay close attention to driver security and design with security in mind.

-   Apply the principle of least privilege:

    a.	Use a strict SDDL string to restrict access to the driver

    b.	Further restrict individual IOCTL’s 

-	Create a threat model to identify attack vectors and consider whether anything can be restricted further.
-	Be careful with regard to embedded pointers being passed in from usermode. They need to be probed, accessed within try except, and they are prone to time of check time of use (ToCToU) issues unless the value of the buffer is captured and compared.
-	If you're unsure, use METHOD_BUFFERED as an IOCTL buffering method.
-   Use code scanning utilities to look for known code vulnerabilities and remediate any identified issues.
-   Seek out knowledgeable code reviewers to look for issues that you may have missed.
-	Use driver verifiers and test your driver with multiple inputs, including corner cases.

 

[Send comments about this article to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design/hw_design]:%20Driver%20security%20checklist%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20https://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




