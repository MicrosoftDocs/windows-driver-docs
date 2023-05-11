---
title: WIA functions for debugging
description: WIA functions for debugging
ms.date: 05/10/2023
---

# WIA functions for debugging

You can use the following function to log trace messages, warning messages, and error messages when you are developing your WIA minidriver.

| Function | Description |
|--|--|
| [**wiauDbgDump**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgdump) | Logs a message containing one or more data values. |
| [**wiauDbgError**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerror) | Logs an error message. |
| [**wiauDbgErrorHr**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgerrorhr) | Logs a message containing an HRESULT and its error message string. |
| [**wiauDbgFlags**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgflags) | Determines whether a particular debugging flag is set. |
| [**wiauDbgHelper**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper) | Formats a message and writes it to a log file or the debugger. |
| [**wiauDbgHelper2**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbghelper2) | Writes a message to a log file, or debugger, or both. |
| [**wiauDbgInit**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbginit) | Initializes WIA debugging. |
| [**wiauDbgLegacyError**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror) | Logs an error message. |
| [**wiauDbgLegacyError2**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyerror2) | Logs an error message. |
| [**wiauDbgLegacyHresult2**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacyhresult2) | Logs a default message containing an HRESULT. |
| [**wiauDbgLegacyTrace**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace) | Logs a trace message. |
| [**wiauDbgLegacyTrace2**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacytrace2) | Logs a trace message. |
| [**wiauDbgLegacyWarning**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbglegacywarning) | Logs a warning message. |
| [**wiauDbgSetFlags**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgsetflags) | Sets debugging flags. |
| [**wiauDbgTrace**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgtrace) | Logs a trace message. |
| [**wiauDbgWarning**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaudbgwarning) | Logs a warning message. |
