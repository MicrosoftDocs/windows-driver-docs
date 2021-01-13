---
title: CM_PROB_NORMAL_CONFLICT
description: CM_PROB_NORMAL_CONFLICT
keywords:
- CM_PROB_NORMAL_CONFLICT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 12 - CM_PROB_NORMAL_CONFLICT

This Device Manager error message indicates that two devices have been assigned the same I/O ports, the same interrupt, or the same DMA channel (either by the BIOS, the operating system, or a combination of the two).

## Error Code

12

### Display Message

"This device cannot find enough free resources that it can use. (Code 12)

"If you want to use this device, you will need to disable one of the other devices on this system."

### Recommended Resolution

[Use Device Manager](using-device-manager.md) to determine the source of the conflict and to resolve the conflict. For more information about how to resolve device conflicts, see the Help information about how to use Device Manager.

This error message can also appear if the BIOS did not allocate sufficient resources to a device. For example, this message will be displayed if the BIOS does not allocate an interrupt to a USB controller because of an invalid multiprocessor specification (MPS) table.
