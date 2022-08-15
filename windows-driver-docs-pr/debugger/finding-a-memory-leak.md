---
title: Finding a Memory Leak
description: Finding a Memory Leak
keywords: ["memory leak", "memory leak, debugging"]
ms.date: 05/23/2017
---

# Finding a Memory Leak

A memory leak occurs when a process allocates memory from the paged or nonpaged pools, but does not free the memory. As a result, these limited pools of memory are depleted over time, causing Windows to slow down. If memory is completely depleted, failures may result.

This section includes the following:

- [Determining Whether a Leak Exists](determining-whether-a-leak-exists.md) describes a technique you can use if you are not sure whether there is a memory leak on your system.

- [Finding a Kernel-Mode Memory Leak](finding-a-kernel-mode-memory-leak.md) describes how to find a leak that is caused by a kernel-mode driver or component.

- [Finding a User-Mode Memory Leak](finding-a-user-mode-memory-leak.md) describes how to find a leak that is caused by a user-mode driver or application.

