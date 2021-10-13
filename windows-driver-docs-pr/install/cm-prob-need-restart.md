---
title: CM_PROB_NEED_RESTART
description: CM_PROB_NEED_RESTART
keywords:
- CM_PROB_NEED_RESTART
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code 14 - CM_PROB_NEED_RESTART

This Device Manager error message indicates that the system must be restarted in order for the device to function.

## Error Code

14

### Display Message

"This device cannot work properly until you restart your computer. (Code 14)

"To restart your computer now, click Restart Computer."

### Recommended Resolution

Select **Restart Computer**, which restarts your computer.

## For driver developers

An operation performed on the device needs the system to be restarted before that operation can complete or take effect.  Some common situations that may result in a device needing the system to be restarted:

- A device installation was unable to copy a file to its proper destination location and that file copy was queued up to happen on next boot. See the [SetupApi logs](setupapi-text-logs.md) for more information.

- A device installation was unable to start or restart a service that was installed as part of the device installation. See the [SetupApi logs](setupapi-text-logs.md) for more information.

- There was a problem restarting a device or devices at the end of a device installation. See the [SetupApi logs](setupapi-text-logs.md) for more information.

- There was a problem enabling a disabled device.