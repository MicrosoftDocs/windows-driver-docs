---
title: Idle Power Management Scope
description: Idle Power Management Scope
ms.date: 04/20/2017
---

# Idle Power Management Scope

Storport Idle Power Management (IPM) provides idle power management for the LUN, not the adapter. Storport IPM does not attempt to place the adapter in a low power state if all its LUNs are in a low power state. The miniport driver is responsible for managing adapter power.

Storport IPM is supported in the following system configuration only:

- Systems that use a SATA adapter with a single SATA disk drive attached

Storport IPM is not supported in the following system configurations:

- Systems that have non-direct attached storage (FC, iSCSI, and others)

- Systems that have external storage arrays and RAID controllers

- Systems that have MPIO

- Systems that have non-SATA host bus adapters

- Systems that have more than one disk attached to a SATA adapter
