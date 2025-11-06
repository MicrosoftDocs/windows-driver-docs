---
title: Find and Fix Memory Leaks in Windows
description: Learn how to identify and troubleshoot memory leaks in Windows systems using Performance Monitor and debugging tools. Find kernel-mode and user-mode leaks.
keywords: ["memory leak", "memory leak, debugging"]
ms.date: 11/05/2025
ms.topic: troubleshooting
---

# Find a memory leak

A memory leak occurs when a process allocates memory from the paged or nonpaged pools but doesn't free it. As memory is depleted over time, Windows slows down and may experience system failures. 

This article helps you:

- Determine if your system has a memory leak
- Find kernel-mode memory leaks caused by drivers
- Find user-mode memory leaks in applications

Start by checking if a leak exists using Performance Monitor, then follow the appropriate troubleshooting path.

**Step 1: [Determine if your system has a memory leak](determining-whether-a-leak-exists.md)** - Not sure if your system has a leak? Start here to use Performance Monitor to confirm.

**Step 2: Find the source** 

- **[Kernel-mode memory leak](finding-a-kernel-mode-memory-leak.md)** - For leaks caused by drivers or Windows components
- **[User-mode memory leak](finding-a-user-mode-memory-leak.md)** - For leaks caused by applications

> [!TIP]
> Most users should start with Step 1 to confirm a leak exists before investigating further.
