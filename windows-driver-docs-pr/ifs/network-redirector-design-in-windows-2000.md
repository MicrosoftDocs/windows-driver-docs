---
title: Network Redirector Design in Windows 2000
description: Network Redirector Design in Windows 2000
keywords:
- network redirectors WDK , Windows 2000
- redirector drivers WDK , Windows 2000
- Redirected Drive Buffering Subsystem WDK file systems , Windows 2000
- RDBSS WDK file systems , Windows 2000
- buffering code WDK network redirectors
- kernel network redirectors WDK , Windows 2000
ms.date: 09/05/2024
---

# Network redirector design

This article describes the driver model for network redirectors that was introduced in Windows 2000.

A significant challenge in the design of network redirectors is the relatively complex translation that is performed from user-initiated operations to low-level network operations, both with respect to operation selection and timing. Dealing with the Windows I/O System, Cache Manager, and Memory Manager is a relatively complex undertaking. This statement is especially true when considering the variety of buffering modes that might be appropriate for a remote communication mechanism, such as a computer network where the speed and reliability can vary considerably. The implementation of these buffering operations in a network redirector represents a significant investment in function that would ideally be shared and reused by drivers.

Windows 2000 introduced a driver model for network redirectors based on a layered or miniport driver approach. This model is refered to as the mini-redirector architecture (*rdr2*). Rather than having to re-implement the complex code used for buffering and interaction with the I/O Manager and Cache Manager in each driver, this large block of code was pulled out and made available to all potential network redirectors. The shared common buffering code is called the Redirected Drive Buffering SubSystem (RDBSS).

A model of this architecture with multiple redirectors is shown below.

:::image type="content" source="images/redir-02.png" alt-text="Diagram illustrating network redirector design starting in Windows 2000.":::

This RDBSS design offers several of the following benefits:

- It simplifies the process of writing the kernel-mode driver (KMD) for a network redirector since a large amount of common code that was needed to deal with the I/O System, Cache Manager, and Memory Manager was provided.

- It makes available to other network redirector drivers a considerable amount of performance improvements based on buffering algorithms and kernel optimizations developed for Microsoft Networks.

- It simplifies maintenance since only one copy of the buffering code needs to be developed and maintained. In the pre-Windows 2000 model, a copy was required for each redirector.

- It provides a strong encapsulation of the network protocol-specific component of a network redirector, so driver developers can focus on these aspects of the network redirector that are unique and specific to their application or product.

- It simplifies debugging drivers for network redirectors by providing decoupling based on this layered approach.

The RDBSS model was introduced with Windows 2000. This same model is also used on Windows Server 2003 and Windows XP.

## Network Redirector Design in Windows NT

The original scheme introduced in Windows NT 3.0 used no shared components and was limited. This model is often called the original *rdr* driver model (rdr was an abbreviation for redirector). To simplify the process of writing a network redirector, the OS provided no special support. Each KMD implemented all of the functions required for a network redirector. Consequently, each KMD would include a large amount of code for interactions with the I/O Manager, Cache Manager, and Memory Manager. Each network redirector (LAN Manager, NetWare, and NFS, for example) installed on Windows had to implement all of these functions themselves. This design model was used for drivers for network redirectors through Windows NT 4.0. The following is a diagram of this architecture, with multiple redirectors.

:::image type="content" source="images/redir-01.png" alt-text="Diagram illustrating network redirector design in Windows NT.":::
