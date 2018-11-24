---
title: C28725
description: Warning C28725 Use Watson instead of this SetUnhandledExceptionFilter.
ms.assetid: 826B4BD2-226C-4986-86B3-E9DFD62DB225
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28725


warning C28725: Use Watson instead of this SetUnhandledExceptionFilter

This warning is reported when an application uses the [**SetUnhandledExceptionFilter function**](https://msdn.microsoft.com/library/windows/desktop/ms680634). The function can be used to supersede the top-level exception handler of each thread of a process. By default, the system passes unhandled exceptions to [Windows Error Reporting](https://msdn.microsoft.com/library/windows/desktop/bb513641) (WER). For security and for convenience, see [Using WER](https://msdn.microsoft.com/library/windows/desktop/bb513616).

 

 





