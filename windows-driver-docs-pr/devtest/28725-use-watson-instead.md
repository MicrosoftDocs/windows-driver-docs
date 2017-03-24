---
title: C28725
description: Warning C28725 Use Watson instead of this SetUnhandledExceptionFilter.
ms.assetid: 826B4BD2-226C-4986-86B3-E9DFD62DB225
---

# C28725


warning C28725: Use Watson instead of this SetUnhandledExceptionFilter

This warning is reported when an application uses the [**SetUnhandledExceptionFilter function**](https://msdn.microsoft.com/library/windows/desktop/ms680634). The function can be used to supersede the top-level exception handler of each thread of a process. By default, the system passes unhandled exceptions to [Windows Error Reporting](https://msdn.microsoft.com/library/windows/desktop/bb513641) (WER). For security and for convenience, see [Using WER](https://msdn.microsoft.com/library/windows/desktop/bb513616).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28725%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




