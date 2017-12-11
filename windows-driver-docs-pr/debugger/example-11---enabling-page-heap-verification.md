---
title: Example 11 Enabling Page Heap Verification
description: Example 11 Enabling Page Heap Verification
ms.assetid: 5d0303a9-29f7-4759-ae7b-ad670eaee0ee
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 11: Enabling Page Heap Verification


## <span id="ddk_example_11___enabling_page_heap_verification_dtools"></span><span id="DDK_EXAMPLE_11___ENABLING_PAGE_HEAP_VERIFICATION_DTOOLS"></span>


The following commands enable full and standard page heap verification for myapp.exe, a fictitious program.

The first command enables *standard* page heap verification for myapp.exe. It uses the **/p** parameter to enable page heap for a process. By default, **/p** enables standard page heap.

```
gflags /p /enable myapp.exe 
```

The following commands enable *full* page heap verification for the myapp.exe program. Although these commands create different settings in the registry, they are all functionally equivalent to selecting the **Enable page heap** check box for the myapp.exe image file in the **Global Flags** dialog box. These methods can be used interchangeably.

```
gflags /p /enable myapp.exe /full
gflags /i myapp.exe +hpa
gflags /i myapp.exe +02000000
```

The following commands disable full or standard page heap verification for the myapp.exe program, regardless of the command or dialog box method used to enable page heap verification.

```
gflags /p /disable myapp.exe
gflags /i myapp.exe -hpa
gflags /i myapp.exe -02000000
```

**Note**   When using the **/debug** or **/kdebug** parameters, use the **/p /disable** parameters to turn off the page heap verification (not the **/i -hpa** parameters). The **/p /disable** parameters disable page heap verification and delete registry entries that the debugger reads.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%2011:%20%20Enabling%20Page%20Heap%20Verification%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




