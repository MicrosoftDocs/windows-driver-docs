---
title: Executable version numbers for audio drivers 
description: Policy defines how driver package executables are evaluated. 
ms.topic: article
ms.date: 04/09/2024
---
# Executable version numbers for audio drivers 

In the interest of ensuring quality and reliability of audio drivers shipped to Windows users, there are policies for evaluating executables in driver packages.

Executable files (.sys, .exe, .dll, .cpl) that are included as part of a driver package model need to include version numbering so that bugs and fixes and be tracked and verified.

The driver submission is rejected rejected in the case of missing, blank, nulled, or "0.0.0.0" executable version number.

Learn more about how to add a version number to an executable file with [VERSIONINFO resource](/windows/desktop/menurc/versioninfo-resource).

## What to Do If Your Shipping Label is Rejected
If your shipping label has been rejected for one of the above reasons, contact the Windows Audio Team at audio-partners@microsoft.com.
