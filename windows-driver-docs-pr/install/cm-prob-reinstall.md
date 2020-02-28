---
title: CM_PROB_REINSTALL
description: CM_PROB_REINSTALL
ms.assetid: 6af20659-a39e-44bc-874d-34078da1ba13
keywords:
- CM_PROB_REINSTALL
ms.date: 02/28/2020
ms.localizationpriority: medium
---

# CM_PROB_REINSTALL

This function is reserved for system use.

Drivers must be reinstalled.

## Error Code

18

### Display Message

"Reinstall the drivers for this device. (Code 18)"

### Recommended Resolution

To reinstall a device driver by using the Hardware Update wizard, follow these steps:

1. [Open Device Manager](using-device-manager.md).

2. Right-click the icon that represents the device in the Device Manager window.

3. On the menu that appears, click **Update Driver** to start the Hardware Update wizard.

Alternatively, you can reinstall a device driver by following these steps:

1. Open Device Manager.

2. Right-click the icon that represents the device in the Device Manager window.

3. On the menu that appears, click **Uninstall** to uninstall the device driver.

4. Click **Action** on the Device Manager menu bar.

5. On the **Action** menu, click **Scan for hardware changes** to reinstall the device driver.

## For driver developers

This problem code is frequently transient.
