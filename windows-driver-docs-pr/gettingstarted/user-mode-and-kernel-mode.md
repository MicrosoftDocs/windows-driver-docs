---
title: User mode and kernel mode
description: User mode and kernel mode
ms.assetid: 9988ff75-f84e-404e-8c2b-0f8325fbbc63
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User mode and kernel mode


A processor in a computer running Windows has two different modes: *user mode* and *kernel mode*. The processor switches between the two modes depending on what type of code is running on the processor. Applications run in user mode, and core operating system components run in kernel mode. While many drivers run in kernel mode, some drivers may run in user mode.

> 在執行Windows作業系統的電腦中，其處理器分為兩種模式: *user mode*和*kernel mode*。處理器會依據執行不同類型的程式碼在兩種模式下切換。
應用程序在user mode下運作，而核心的操作系統元件則是在kernel mode底下運作。當許多驅動器在kernel mode底下運作時，一部分的驅動器可能會在user mode下執行。

When you start a user-mode application, Windows creates a *process* for the application. The process provides the application with a private *virtual address space* and a private *handle table*. Because an application's virtual address space is private, one application cannot alter data that belongs to another application. Each application runs in isolation, and if an application crashes, the crash is limited to that one application. Other applications and the operating system are not affected by the crash.

> 當你啟始了user-mode的應用程式，Windows會為該應用程序創建一個*process*。這道process提供該應用程序一個私人的*virtual address space*以及*handle table*。由於該應用程序的virtual address space是私人的，因此在不同的應用程序之間是無法交換其所屬資料的。每一個應用程序都是獨立運作的，如果一個應用程序崩潰了，崩潰也只會被限制在該應用程序中。其他應用程序以及作業系統都不會被崩潰影響。

In addition to being private, the virtual address space of a user-mode application is limited. A processor running in user mode cannot access virtual addresses that are reserved for the operating system. Limiting the virtual address space of a user-mode application prevents the application from altering, and possibly damaging, critical operating system data.

> 除了被定義為私人之外，在user mode中的virtual address space是被限制的。一個處理器在user mode下運作時並不能訪問為作業系統保留的virtual address space。限制user mode底下的應用程序的virtual address space可以防止應用程序更改、甚至損壞作業系統的重要數據。

All code that runs in kernel mode shares a single virtual address space. This means that a kernel-mode driver is not isolated from other drivers and the operating system itself. If a kernel-mode driver accidentally writes to the wrong virtual address, data that belongs to the operating system or another driver could be compromised. If a kernel-mode driver crashes, the entire operating system crashes.

> 所有執行在kernel mode底下的程式碼都共享同一個virtual address space。這意味著kernel-mode driver與其他driver以及作業系統本身並不是獨立的，屬
於操作系統或其他driver的數據可能會受到威脅。如果kernel-mode driver崩潰，則會造成整個作業系統崩潰。

This diagram illustrates communication between user-mode and kernel-mode components.

![block diagram of user-mode and kernel-mode components](images/userandkernelmode01.png)

## <span id="related_topics"></span>Related topics


[Virtual Address Spaces](virtual-address-spaces.md)
