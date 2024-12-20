---
title: About FSCTLs
description: About FSCTLs
keywords:
- filter drivers Windows , FSCTL
- file system filter drivers Windows , FSCTL
- Windows file system driver FSCTL
- Windows file system filter driver FSCTL
ms.date: 12/20/2024
---

# About FSCTLs

This article describes file system control codes (FSCTLs) and how they are used at the kernel level in Windows. For information about FSCTLs in user mode, see [Device Input and Output Control](/windows/win32/devio/device-input-and-output-control-ioctl-).

File system control codes (FSCTLs) can be thought of as special I/O control codes (IOCTLs). Whereas IOCTLs are used to perform *device control* operations, FSCTLs are used to perform *file system* operations. FSCTLs can be used to:

* Alter or query the behavior of the file system.
* Set or query metadata associated with a particular file or with the file system itself.

Kernel-mode modules in the file system stack, such as file systems and file system minifilter drivers, can see and issue FSCTLs. They are thus able to inspect, modify, or redirect operations.

A process invokes an FSCTL on a handle to perform an action against the file or directory associated with the handle. When a server receives an FSCTL request, it uses the information in the request to perform the requested action. How a server performs the action requested by an FSCTL is implementation-dependent.

Some system-defined generic FSCTLs are permitted to be invoked across the network. Generic FSCTLs are used by the local file systems or by multiple components within the system. Any application, service, or driver can define private FSCTLs. Most private FSCTLs are used locally in the internal driver stacks and don't flow over the wire. However, if a component allows its private FSCTLs to flow over the wire, that component is responsible for ensuring the FSCTLs and associated data structures are documented.

## Issuing an FSCTL in kernel mode

Generally, FSCTLs are issued through one of the following kernel-mode functions:

* [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile), which is a system-supplied function implemented by *FltMgr*. Minifilter drivers are a part of the Filter Manager framework, so should use this function to issue an FSCTL to the file system or other minifilters in the stack.

* [**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile), which is a system-supplied function implemented by the Windows kernel. Kernel-mode components other than file system minifilters can use this function to issue an FSCTL.

## FSCTL-specific information

See the FSCTL_*XXX* articles following this article for information about specific FSCTLs.
