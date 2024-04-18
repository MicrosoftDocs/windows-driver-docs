---
title: Driver Pacakge Executable Rules
description: Policy defines how driver package executables will be evaluated. 
ms.topic: article
ms.date: 04/09/2024
---

# Driver Package Executable Evaluation Rules

In the interest of ensuring quality and reliability of audio drivers shipped to Windows users, there are policies for evaluating executables in driver packages.

Executable files (.sys, .exe, .dll, .cpl) that are included as part of a driver package model need to include version numbering so that bugs and fixes and be tracked and verfied.

The driver submission will be rejected in the case of missing, blank, nulled, or "0.0.0.0" executable version number.
