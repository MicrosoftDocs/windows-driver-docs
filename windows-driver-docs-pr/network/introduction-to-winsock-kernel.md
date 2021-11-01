---
title: Introduction to Winsock Kernel
description: Introduction to Winsock Kernel
keywords:
- Winsock Kernel WDK networking , about Winsock Kernel
- WSK WDK networking , about Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Winsock Kernel


Winsock Kernel (WSK) is a kernel-mode [Network Programming Interface (NPI)](network-programming-interface.md). With WSK, kernel-mode software modules can perform network I/O operations using the same socket programming concepts that are supported by user-mode Winsock2. The WSK NPI supports familiar socket operations such as socket creation, binding, connection establishment, and data transfers (send and receive). However, while the WSK NPI supports most of the same socket programming concepts as user-mode Winsock2, it is a completely new and different interface with unique characteristics such as asynchronous I/O that uses IRPs and event callbacks to enhance performance.

Kernel-mode network modules targeted for Windows Vista and later versions of Microsoft Windows should use WSK instead of [TDI](/previous-versions/windows/hardware/network/ff565094(v=vs.85)) because WSK provides improved performance and easier programming. Filter drivers should implement the [Windows Filtering Platform](introduction-to-windows-filtering-platform-callout-drivers.md) on Windows Vista, and TDI clients should implement WSK.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](introduction-to-windows-filtering-platform-callout-drivers.md) or [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista/#winsock-kernel-wsk) instead.

 

 

