---
title: CM_PROB_UNSIGNED_DRIVER
description: CM_PROB_UNSIGNED_DRIVER
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 52 - CM_PROB_UNSIGNED_DRIVER

This Device Manager error message indicates that the device did not start on a 64-bit version of Windows because it has a driver that is not digitally signed. For more information about how to sign drivers, see [Driver Signing](driver-signing.md).

## Error

52

### Display Message

"Windows cannot verify the digital signature for the drivers required for this device. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source. (Code 52)"

### Recommended Resolution

The driver does not comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

For end-users, the only way to avoid this error is to obtain and install a digitally signed driver for the device.

For driver developers, you can use various methods to load an unsigned driver on a 64-bit version of Windows. For more information, see [Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md).

## See Also

[Code Integrity Diagnostic System Log Events](./code-integrity-diagnostic-system-log-events.md)
