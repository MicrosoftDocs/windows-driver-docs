---
title: Hyper-V Extensible Switch Save and Restore Operations
description: Hyper-V Extensible Switch Save and Restore Operations
ms.assetid: 7F3A77E0-F1E9-49E4-8C78-62B8F412353D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Save and Restore Operations


When a Hyper-V child partition is stopped, saved, or live migrated, the run-time state of the partition is saved. When the partition is restarted or has completed the live migration to another host computer, the run-time state is restored. During the transition between saved and restored states, the settings of the network interfaces for the child partition are unchanged and network connections to the Hyper-V extensible switch are not torn down.

The extensible switch interface notifies underlying extensions of save and restore operations for the child partition. During the save operation, the extension can return run-time data for each extensible switch network adapter (NIC). During the restore operation, the interface returns the run-time data to the extension so that it can restore the state of the NIC.

This section includes the following topics:

[Hyper-V Extensible Switch Save Operations](hyper-v-extensible-switch-save-operations.md)

[Hyper-V Extensible Switch Restore Operations](hyper-v-extensible-switch-restore-operations.md)

[Hyper-V Extensible Switch Live Migration Support](hyper-v-extensible-switch-live-migration-support.md)

 

 





