---
title: PoolMon Requirements
description: PoolMon Requirements
keywords:
- PoolMon WDK , requirements
- Memory Pool Monitor WDK , requirements
- PoolMon WDK , displays
- Memory Pool Monitor WDK , displays
- files WDK PoolMon
ms.date: 04/20/2017
ms.topic: checklist
---

# PoolMon Requirements

PoolMon requires the following system configuration, permissions, and files.

## System Requirements

The version of PoolMon included in the Windows Driver Kit (WDK) and described in this document runs only on Microsoft Windows XP and later versions of Windows.

## Pool Tagging Requirement

The pool tagging feature collects and calculates statistics about pool memory sorted by the tag value of the allocation.

To enable pool tagging, use GFlags, a tool included in Debugging Tools for Windows. Open the **Global Flags** dialog box, check the **Enable Pool Tagging** check box, and then restart the computer.

## Requirements for Terminal Services Session Pool Monitoring

PoolMon displays allocations from the Terminal Services session pools only on Windows Server 2003 and later versions of Windows.

Windows allocates memory from Terminal Services session pools only when the computer is configured as a Terminal Server. On Terminal Servers, the kernel-mode portions of the Win32 subsystem allocate memory from the session pools. Otherwise, Windows allocates pool memory for Terminal Services from the system pool.

## Display Requirements

To see the entire PoolMon display, the Command Prompt window size must be at least 80 characters wide (width=80) and at least 53 rows high (height=53), and the Command Prompt window buffer must be at least 500 characters wide (width=500) and at least 2000 rows high (height=2000). Otherwise, the display might be truncated.

## Required Files

poolmon.exe

msdis130.dll

msvcp70.dll

msvcr70.dll

pooltag.txt
