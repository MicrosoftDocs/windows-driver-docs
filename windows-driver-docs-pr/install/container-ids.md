---
title: Container ID
description: A container ID is a system-supplied device identification string that uniquely groups the functional devices associated with a single-function or multifunction device installed in the computer.
ms.assetid: 66e0c68a-c7bd-4d85-a438-0342c5943562
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container ID


A container ID is a system-supplied device identification string that uniquely groups the functional devices associated with a single-function or multifunction device installed in the computer.

Starting with Windows 7, the Plug and Play (PnP) manager uses the container ID to group one or more device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that originated from and belong to each instance of a particular physical device. This instance is referred to as the *device* *container*.

Grouping all the devnodes that originated from an instance of a single device achieves the following:

-   The operating system can determine how functionality is related among child devnodes and their container devnode.

-   The user or applications are presented with a device-centric view of devices instead of the traditional function-centric view.

This section contains topics that discuss the container ID in more detail:

[Overview of Container IDs](overview-of-container-ids.md)

[How Container IDs are Generated](how-container-ids-are-generated.md)

[Verifying the Implementation of Container IDs](verifying-the-implementation-of-container-ids.md)

[Troubleshooting the Implementation of Container IDs](troubleshooting-the-implementation-of-container-ids.md)

 

 





