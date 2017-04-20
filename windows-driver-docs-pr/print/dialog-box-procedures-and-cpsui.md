---
title: Dialog Box Procedures and CPSUI
author: windows-driver-content
description: Dialog Box Procedures and CPSUI
ms.assetid: fad65a34-9580-41a5-ad58-91ea7ffcd3d5
keywords:
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
- message handlers WDK CPSUI
- CPSUI WDK print , message handlers
- dialog box procedures WDK CPSUI
- window messages WDK CPSUI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Dialog Box Procedures and CPSUI


## <a href="" id="ddk-dialog-box-procedures-and-cpsui-gg"></a>


A dialog box procedure is a callback function that handles window messages sent by the system. This type of [page event callback](page-event-callbacks.md) is required if you are creating a customized property sheet page that is not supplied by CPSUI. (You can also use dialog box procedures with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), but use of a [CPSUI message handler](cpsui-message-handler.md) is recommended.) For more information about dialog box procedures, see DialogProc in the Microsoft Windows SDK documentation. Pointers to dialog box procedures are declared using the DLGPROC pointer type, also described in the Windows SDK documentation.

For all property sheet pages created using CPSUI, window messages are first intercepted by CPSUI before being passed to the application-supplied dialog box procedure. If the page was defined using a CPSUI-supplied template, the application-supplied dialog procedure can supply a return value indicating that CPSUI should process the message.

A dialog box procedure can use the [**SetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff562624) and [**GetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff549922) functions to store and retrieve an application-supplied value.

For more information about using dialog box procedures with CPSUI, see the Remarks section for [**DLGPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff547607).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Dialog%20Box%20Procedures%20and%20CPSUI%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


