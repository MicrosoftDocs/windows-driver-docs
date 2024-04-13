---
title: Kernel-mode Dump Files
description: Learn how to create and analyze kernel-mode memory dump files to resolve kernel-mode errors.
keywords: ["dump file, kernel mode"]
ms.date: 12/21/2023
---

# Kernel-mode dump files

When a kernel-mode error occurs, Microsoft Windows displays the blue screen with bug check data by default. However, you can choose from several alternative behaviors:

- A kernel debugger, such as WinDbg or KD, can be contacted.

- The system can automatically reboot.

- A memory dump file can be written.

- A memory dump file can be written, and the system can automatically reboot afterwards.

**Create and analyze kernel-mode memory dump files.**

There are three different [varieties of kernel-mode dump files](varieties-of-kernel-mode-dump-files.md). However, no dump file can ever be as useful and versatile as a live kernel debugger attached to the system that has failed.

- [Create a kernel-mode dump file](creating-a-kernel-mode-dump-file.md)

- [Enabling a Kernel-Mode dump file](enabling-a-kernel-mode-dump-file.md)

- [Analyze a kernel-mode dump file](analyzing-a-kernel-mode-dump-file.md)

- [Generate a kernel or complete crash dump](/troubleshoot/windows-client/performance/generate-a-kernel-or-complete-crash-dump)
