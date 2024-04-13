---
title: Dialog Box Procedures and CPSUI
description: Dialog Box Procedures and CPSUI
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
- message handlers WDK CPSUI
- CPSUI WDK print , message handlers
- dialog box procedures WDK CPSUI
- window messages WDK CPSUI
ms.date: 01/27/2023
---

# Dialog Box Procedures and CPSUI

[!include[Print Support Apps](../includes/print-support-apps.md)]

A dialog box procedure is a callback function that handles window messages sent by the system. This type of [page event callback](page-event-callbacks.md) is required if you are creating a customized property sheet page that is not supplied by CPSUI. (You can also use dialog box procedures with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), but use of a [CPSUI message handler](cpsui-message-handler.md) is recommended.) For more information about dialog box procedures, see DialogProc in the Microsoft Windows SDK documentation. Pointers to dialog box procedures are declared using the DLGPROC pointer type, also described in the Windows SDK documentation.

For all property sheet pages created using CPSUI, window messages are first intercepted by CPSUI before being passed to the application-supplied dialog box procedure. If the page was defined using a CPSUI-supplied template, the application-supplied dialog procedure can supply a return value indicating that CPSUI should process the message.

A dialog box procedure can use the [**SetCPSUIUserData**](/windows-hardware/drivers/ddi/compstui/nf-compstui-setcpsuiuserdata) and [**GetCPSUIUserData**](/windows-hardware/drivers/ddi/compstui/nf-compstui-getcpsuiuserdata) functions to store and retrieve an application-supplied value.

For more information about using dialog box procedures with CPSUI, see the Remarks section for [**DLGPAGE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_dlgpage).
