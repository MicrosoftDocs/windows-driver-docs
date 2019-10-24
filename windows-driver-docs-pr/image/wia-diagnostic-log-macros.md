---
title: WIA Diagnostic Log Macros
description: WIA Diagnostic Log Macros
ms.assetid: 8b544045-e9d7-422b-825c-f1a5531e0e11
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Diagnostic Log Macros

> [!NOTE]
> For WIA error handling on modern Windows operating systems, see [WIA Driver Error Recovery](wia-driver-error-recovery-for-windows-vista.md).

The Diagnostic Log Macros enable minidrivers to log trace, error, and warning messages to the *Wiaservc.log* diagnostic log file.

| Macro | Description |
| --- | --- |
|[WIAS_LERROR](https://docs.microsoft.com/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lerror) | Writes a log statement of type ERROR to the Wiaservc.log diagnostic log file. |
| [WIAS_LHRESULT](https://docs.microsoft.com/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lhresult) | Translates an HRESULT value into a string and writes the string to the Wiaservc.log diagnostic log file. |
| [WIAS_LTRACE](https://docs.microsoft.com/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_ltrace) | Writes a log statement of type TRACE to the Wiaservc.log diagnostic log file. |
| [WIAS_LWARNING](https://docs.microsoft.com/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_lwarning) | Writes a log statement of type WARNING to the Wiaservc.log diagnostic log file. |
| [WIAS_ERROR](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_error) | Writes a log statement of type ERROR to the Wiatrace.log diagnostic log file. |
| [WIAS_TRACE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wias_trace) | Writes a log statement of type TRACE to the Wiatrace.log diagnostic log file. |
