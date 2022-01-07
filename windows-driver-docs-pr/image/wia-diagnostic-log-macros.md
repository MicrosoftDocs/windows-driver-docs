---
title: WIA Diagnostic Log Macros
description: WIA Diagnostic Log Macros
ms.date: 04/20/2017
---

# WIA Diagnostic Log Macros

> [!NOTE]
> For WIA error handling on modern Windows operating systems, see [WIA Driver Error Recovery](wia-driver-error-recovery-for-windows-vista.md).

The Diagnostic Log Macros enable minidrivers to log trace, error, and warning messages to the *Wiaservc.log* diagnostic log file.

| Macro | Description |
| --- | --- |
|[WIAS_LERROR](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lerror) | Writes a log statement of type ERROR to the Wiaservc.log diagnostic log file. |
| [WIAS_LHRESULT](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lhresult) | Translates an HRESULT value into a string and writes the string to the Wiaservc.log diagnostic log file. |
| [WIAS_LTRACE](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_ltrace) | Writes a log statement of type TRACE to the Wiaservc.log diagnostic log file. |
| [WIAS_LWARNING](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lwarning) | Writes a log statement of type WARNING to the Wiaservc.log diagnostic log file. |
| [WIAS_ERROR](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_error) | Writes a log statement of type ERROR to the Wiatrace.log diagnostic log file. |
| [WIAS_TRACE](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_trace) | Writes a log statement of type TRACE to the Wiatrace.log diagnostic log file. |
