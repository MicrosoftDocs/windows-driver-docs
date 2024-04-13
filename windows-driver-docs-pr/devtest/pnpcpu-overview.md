---
title: PNPCPU Overview
description: PNPCPU Overview
keywords:
- PNPCPU WDK , about PNPCPU
ms.date: 04/20/2017
---

# PNPCPU Overview


PNPCPU is a command line tool that performs the following functions:

-   Install
    -   To install the tool, run Pnpcpu.exe with the **-install** option.
    -   Pnpcpu installs all relevant drivers.
    -   Pnpcpu updates the Boot Configuration Data store with the appropriate parameters.
-   Add
    -   PNPCPU attempts to hot add all logical processors in the system, up to the maximum supported by the license for the installed edition.
-   Removal
    -   To remove the tool, run Pnpcpu.exe with the **-uninstall** option. This results in a complete undo of all steps performed by **-install**.
    -   This option leaves the binaries on the disk for subsequent reinstallation and use.

