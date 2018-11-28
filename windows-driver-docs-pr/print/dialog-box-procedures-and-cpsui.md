---
title: Dialog Box Procedures and CPSUI
description: Dialog Box Procedures and CPSUI
ms.assetid: fad65a34-9580-41a5-ad58-91ea7ffcd3d5
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
- message handlers WDK CPSUI
- CPSUI WDK print , message handlers
- dialog box procedures WDK CPSUI
- window messages WDK CPSUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dialog Box Procedures and CPSUI





A dialog box procedure is a callback function that handles window messages sent by the system. This type of [page event callback](page-event-callbacks.md) is required if you are creating a customized property sheet page that is not supplied by CPSUI. (You can also use dialog box procedures with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), but use of a [CPSUI message handler](cpsui-message-handler.md) is recommended.) For more information about dialog box procedures, see DialogProc in the Microsoft Windows SDK documentation. Pointers to dialog box procedures are declared using the DLGPROC pointer type, also described in the Windows SDK documentation.

For all property sheet pages created using CPSUI, window messages are first intercepted by CPSUI before being passed to the application-supplied dialog box procedure. If the page was defined using a CPSUI-supplied template, the application-supplied dialog procedure can supply a return value indicating that CPSUI should process the message.

A dialog box procedure can use the [**SetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff562624) and [**GetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff549922) functions to store and retrieve an application-supplied value.

For more information about using dialog box procedures with CPSUI, see the Remarks section for [**DLGPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff547607).

 

 




