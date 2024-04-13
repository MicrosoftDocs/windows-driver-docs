---
title: CM_PROB_NEED_CLASS_CONFIG
description: CM_PROB_NEED_CLASS_CONFIG
keywords:
- CM_PROB_NEED_CLASS_CONFIG
ms.date: 02/28/2020
---

# Code 56 - CM_PROB_NEED_CLASS_CONFIG

This Device Manager error message indicates that Windows is still setting up the class configuration for this device.


## Error Code

56

### Display Message

"Windows is still setting up the class configuration for this device. (Code 56)"


## For driver developers

This problem code is frequently transient.

In the case of some device setup classes, after the device is installed with a driver package, additional class configuration operations are required to make the device operational.  When configuration is complete, the device will be restarted and should no longer have this problem code.

For example, NET-class devices receive additional configuration based on `*IfType`, `UpperRange`, and other networking-specific INF directives.

If a NET-class device continues to have this problem code, the driver INF might have invalid networking-specific INF directives, or the system's network state may be corrupt and need to be reset.

To do this, use the Network Reset button in the Settings app.
