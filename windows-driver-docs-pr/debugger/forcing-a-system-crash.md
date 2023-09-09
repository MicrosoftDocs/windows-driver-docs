---
title: Forcing a System Crash
description: Forcing a System Crash
keywords: ["system crash, overview"]
ms.date: 06/08/2020
---

# Forcing a System Crash

Once kernel-mode dump files have been [enabled](enabling-a-kernel-mode-dump-file.md), most system crashes should cause a crash file to be written and the blue screen to be displayed.

However, there are times that a system freezes without actually initiating a kernel crash. Possible symptoms of such a freeze include:

- The mouse pointer moves, but can't do anything.

- All video is frozen, the mouse pointer does not move, but paging continues.

- There is no response at all to the mouse or keyboard, and no use of the disk.

If an experienced debugging technician is present, they can attach a kernel debugger and analyze the problem. For some tips on what to look for when this situation occurs, see [Debugging a Stalled System](debugging-a-stalled-system.md).

However, if no technician is present, you may wish to create a kernel-mode dump file and send it to an off-site technician. This dump file can be used to analyze the cause of the error.

There are three ways to deliberately cause a system crash:

[Forcing a System Crash from the Debugger](forcing-a-system-crash-from-the-debugger.md)

[Forcing a System Crash from the Keyboard](forcing-a-system-crash-from-the-keyboard.md)

[Forcing a System Crash with the Power Button](forcing-a-system-crash-with-the-power-button.md)
