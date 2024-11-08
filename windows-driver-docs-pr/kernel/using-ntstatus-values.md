---
title: Use NTSTATUS Values
description: Use NTSTATUS Values
keywords: ["NTSTATUS values WDK kernel", "driver support routines WDK kernel", "return values WDK kernel", "testing return values WDK NTSTATUS values", "success values WDK NTSTATUS values", "informational values WDK NTSTATUS values", "warnings WDK NTSTATUS values", "error values WDK NTSTATUS values", "status information WDK NTSTATUS values", "checking return values"]
ms.date: 11/08/2024
---

# Use NTSTATUS Values

> [!IMPORTANT]
> If you are looking for a table of mappings of NTSTATUS values to the corresponding Win32 error codes, see [NTSTATUS to Win32 Error Code Mappings](https://www.osr.com/blog/2020/04/23/ntstatus-to-win32-error-code-mappings/).

Many kernel-mode [standard driver routines](./introduction-to-standard-driver-routines.md) and driver support routines use the NTSTATUS type for return values. Additionally, drivers provide an NTSTATUS-typed value in an IRP's [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure when [completing IRPs](completing-irps.md). The NTSTATUS type is defined in Ntdef.h, and system-supplied status codes are defined in Ntstatus.h. (Vendors can also define private status codes, although they rarely need to. For more information, see [Defining New NTSTATUS Values](defining-new-ntstatus-values.md).)

NTSTATUS values are divided into four types: success values, informational values, warnings, and error values.

Numerous values are assigned to each type. A common mistake, when testing for a successful return from a routine, is to compare the routine's return value with STATUS_SUCCESS. This comparison checks for only one of several success values.

When testing a return value, you should use one of the following system-supplied macros (defined in Ntdef.h):

| Macro | Description |
|--|--|
| NT_SUCCESS(*Status*) | Evaluates to **TRUE** if the return value specified by *Status* is a success type (0 − 0x3FFFFFFF) or an informational type (0x40000000 − 0x7FFFFFFF). |
| NT_INFORMATION(*Status*) | Evaluates to **TRUE** if the return value specified by *Status* is an informational type (0x40000000 − 0x7FFFFFFF). |
| NT_WARNING(*Status*) | Evaluates to **TRUE** if the return value specified by *Status* is a warning type (0x80000000 − 0xBFFFFFFF). |
| NT_ERROR(*Status*) | Evaluates to **TRUE** if the return value specified by *Status* is an error type (0xC0000000 - 0xFFFFFFFF). |

For example, suppose a driver calls [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) to register a device interface. If the driver checks the return value using the NT_SUCCESS macro, the macro evaluates to **TRUE** if the routine returns STATUS_SUCCESS, which indicates no errors, or if it returns the informational status STATUS_OBJECT_NAME_EXISTS, which indicates that the device interface is already registered.

As another example, suppose a driver calls [**ZwEnumerateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey) to enumerate the subkeys of a specified registry key. If the NT_SUCCESS macro evaluates to **FALSE**, it might be because the routine returned STATUS_INVALID_PARAMETER, which is an error code, or because the routine returned STATUS_NO_MORE_ENTRIES, which is a warning code.

As a final example, suppose a driver sends an IRP that causes a lower-level driver to read information from a device. If the requesting driver specifies a buffer that is too small to receive any information, the lower-level driver might respond by returning STATUS_BUFFER_TOO_SMALL, which is an error code. If the first driver specifies a buffer that can receive some, but not all, of the requested information, the lower-level driver might respond by supplying as much data as possible and then returning STATUS_BUFFER_OVERFLOW, which is a warning code. If the first driver tests the status value using NT_SUCCESS or NT_ERROR incorrectly, it might inadvertently drop some of the information received.
