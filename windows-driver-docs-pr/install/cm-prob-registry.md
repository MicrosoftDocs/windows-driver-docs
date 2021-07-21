---
title: CM_PROB_REGISTRY
description: CM_PROB_REGISTRY
keywords:
- CM_PROB_REGISTRY
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 19 - CM_PROB_REGISTRY

This Device Manager error message indicates that a registry problem was detected.

## Error Code

19

### Display Message

"Windows cannot start this hardware device because its configuration information (in the registry) is incomplete or damaged. (Code 19)"

### Recommended Resolution

This error can result if more than one service is defined for a device, there is a failure opening the service key, or the driver name cannot be obtained from the service key.

Try either uninstalling and reinstalling the driver or rolling back the system to the most recent successful configuration of the registry.

To uninstall and reinstall a device driver, follow these steps:

1. [Open Device Manager](using-device-manager.md).

2. Right-click the icon that represents the device in the Device Manager window.

3. On the menu that appears, click **Uninstall** to uninstall the device driver.

4. Click **Action** on the Device Manager menu bar.

5. On the **Action** menu, click **Scan for hardware changes** to reinstall the device driver.

To roll a system back to the most recent successful configuration of the registry, restart the computer in Safe Mode and select the Last Known Good Configuration option.
