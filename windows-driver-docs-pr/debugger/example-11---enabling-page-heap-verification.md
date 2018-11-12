---
title: Example 11 Enabling Page Heap Verification
description: Example 11 Enabling Page Heap Verification
ms.assetid: 5d0303a9-29f7-4759-ae7b-ad670eaee0ee
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 11: Enabling Page Heap Verification


## <span id="ddk_example_11___enabling_page_heap_verification_dtools"></span><span id="DDK_EXAMPLE_11___ENABLING_PAGE_HEAP_VERIFICATION_DTOOLS"></span>


The following commands enable full and standard page heap verification for myapp.exe, a fictitious program.

The first command enables *standard* page heap verification for myapp.exe. It uses the **/p** parameter to enable page heap for a process. By default, **/p** enables standard page heap.

```console
gflags /p /enable myapp.exe 
```

The following commands enable *full* page heap verification for the myapp.exe program. Although these commands create different settings in the registry, they are all functionally equivalent to selecting the **Enable page heap** check box for the myapp.exe image file in the **Global Flags** dialog box. These methods can be used interchangeably.

```console
gflags /p /enable myapp.exe /full
gflags /i myapp.exe +hpa
gflags /i myapp.exe +02000000
```

The following commands disable full or standard page heap verification for the myapp.exe program, regardless of the command or dialog box method used to enable page heap verification.

```console
gflags /p /disable myapp.exe
gflags /i myapp.exe -hpa
gflags /i myapp.exe -02000000
```

**Note**   When using the **/debug** or **/kdebug** parameters, use the **/p /disable** parameters to turn off the page heap verification (not the **/i -hpa** parameters). The **/p /disable** parameters disable page heap verification and delete registry entries that the debugger reads.

 

 

 





