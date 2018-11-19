---
title: DispatchSetInformation Routines
description: DispatchSetInformation Routines
ms.assetid: 9fb56504-32a7-47b0-b731-df1dc74ce861
keywords: ["dispatch routines WDK kernel , DispatchSetInformation routine", "DispatchSetInformation routine", "set information dispatch routines WDK kernel", "IRP_MJ_SET_INFORMATION I/O function code"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchSetInformation Routines





A driver's [*DispatchSetInformation*](https://msdn.microsoft.com/library/windows/hardware/ff543399) routine handles IRPs for the [**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550799) I/O function code. Driver support for this I/O function code is optional, and typically appears in higher-level or file system drivers. This request is sent by the I/O manager and other operating system components, as well as other kernel-mode drivers. For example, it is sent when a user-mode application calls [**SetEndOfFile**](https://msdn.microsoft.com/library/windows/desktop/aa365531), and when a kernel-mode component calls [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096).

 

 




