---
title: IWiaLog COM interface
description: IWiaLog COM interface
ms.date: 05/03/2023
---

# IWiaLog COM interface

> [!IMPORTANT]
> The [**IWiaLog**](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwialog) interface is obsolete in Microsoft Windows XP and later versions and is no longer supported. Use the [WIA Diagnostic Log Macros](wia-diagnostic-log-macros.md) instead.

The **IWiaLog** interface is provided for backward compatibility only. The methods in this interface allow a minidriver to write error, trace, and warning messages to a log. The **IWiaLog** interface provides the following methods.

| Method | Description |
|--|--|
| [**IWiaLog::InitializeLog**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-initializelog) | Initializes the logging utility. |
| [**IWiaLog::Log**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-log) | Logs a message to a file or other target. |
| [**IWiaLog::hResult**](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-hresult) | Translates an HRESULT into a string. |

For more information about this interface, see [IWiaLog Interface and Diagnostic Log Macros](/windows-hardware/drivers/ddi/_image/index).
