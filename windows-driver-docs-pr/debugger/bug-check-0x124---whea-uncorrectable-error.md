---
title: Bug Check 0x124 WHEA_UNCORRECTABLE_ERROR
description: Learn about the bug check 0x124 WHEA_UNCORRECTABLE_ERROR, which indicates that a fatal hardware error has occurred. 
keywords: ["Bug Check 0x124 WHEA_UNCORRECTABLE_ERROR", "WHEA_UNCORRECTABLE_ERROR"]
ms.date: 12/12/2022
topic_type:
- apiref
api_name:
- WHEA_UNCORRECTABLE_ERROR
api_type:
- NA
ms.custom: contperf-fy22q1
---

# Bug Check 0x124: WHEA_UNCORRECTABLE_ERROR

The WHEA_UNCORRECTABLE_ERROR bug check has a value of 0x00000124 and indicates that a fatal hardware error has occurred. This bug check uses the error data provided by the Windows Hardware Error Architecture (WHEA).

To identify a specific cause of the error, an understanding of the [WHEA\_ERROR\_RECORD](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_error_record) structure is normally required. For more information, see the [remarks section](#remarks) of this article.

> [!IMPORTANT]
> This topic is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Parameters

| Parameter 1 | Parameter 2 | Parameter 3 | Parameter 4 | Cause of error |
|-------------|-------------|-------------|-------------|----------------|
| 0x0         | Address of WHEA_ERROR_RECORD structure | High 32 bits of MCi_STATUS MSR for the MCA bank that had the error | Low 32 bits of MCi_STATUS MSR for the MCA bank that had the error | A machine check exception occurred.<br><br> These parameter descriptions apply if the processor is based on the x64 architecture, or the x86 architecture that has the MCA feature available (for example, Intel Pentium Pro, Pentium IV, or Xeon). |
| 0x1         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A corrected machine check exception occurred. |
| 0x2         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A corrected platform error occurred.          |
| 0x3         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A nonmaskable interrupt (NMI) error occurred. |
| 0x4         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | An uncorrectable PCI Express error occurred.  |
| 0x5         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A generic hardware error occurred. |
| 0x6         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | An initialization error occurred. |
| 0x7         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A BOOT error occurred. |
| 0x8         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A scalable coherent interface (SCI) generic error occurred. |
| 0x9         | Address of WHEA_ERROR_RECORD structure | Length, in bytes, of the SAL log | Address of the SAL | An uncorrectable Itanium-based machine check abort error occurred. |
| 0xA         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A corrected Itanium-based machine check error occurred. |
| 0xB         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | A corrected Itanium platform error occurred. |
| 0xC         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | Other types of error sources v2. |
| 0xD         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | SCI-based GHESv2 (ACPI generic hardware error source). |
| 0xE         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | BMC (baseboard management controller) error info. |
| 0xF         | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | ARS PMEM (address range scrubbing persistent memory) error source.|
| 0x10        | Address of WHEA_ERROR_RECORD structure | Reserved | Reserved | Device driver error source. |

## Cause

This bug check is typically related to physical hardware failures. It can be heat related or a result of defective hardware, memory, or even a processor that's beginning to fail or has failed. If over-clocking has been enabled, try disabling it. Confirm that any cooling systems such as fans are functional. Run system diagnostics to confirm that the system memory isn't defective. It's less likely, but possible, that a driver is causing the hardware to fail with this bug check.

To learn more about general bug check troubleshooting, see [Blue screen data](blue-screen-data.md).

## Remarks

The [!analyze debug extension](-analyze.md) displays information about the bug check and can be helpful in determining the root cause.

- Parameter 1 identifies the type of error source that reported the error.
- Parameter 2 holds the address of the [WHEA\_ERROR\_RECORD](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_error_record) structure that describes the error condition.

When a hardware error occurs, WHEA creates an error record to store the error information associated with the hardware error condition. Each error record is described by a WHEA\_ERROR\_RECORD structure. The Windows kernel includes the error record with the Event Tracing for Windows (ETW) hardware error event that it raises in response to the error, so that the error record is saved in the system event log. The format of the error records that are used by WHEA are based on the Common Platform Error Record, as described in Appendix N of version 2.2 of the Unified Extensible Firmware Interface (UEFI) specification. For more information, see [WHEA\_ERROR\_RECORD](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_error_record) and [Windows Hardware Error Architecture (WHEA)](../whea/index.md).

You can use [!errrec address](-errrec.md) to display the WHEA\_ERROR\_RECORD structure using the address provided in Parameter 2. The [!whea](-whea.md) and [!errpkt](-errpkt.md) extensions can be used to display additional WHEA information.

For more information, see the following articles:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyze a kernel-mode dump file with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

Use the [!analyze extension](using-the--analyze-extension.md) and [!analyze](-analyze.md)

This bug check isn't supported in Windows versions prior to Windows Vista. Instead, machine check exceptions are reported through [bug check 0x9C](bug-check-0x9c--machine-check-exception.md).
