---
title: CM_PROB_DISABLED_SERVICE
description: CM_PROB_DISABLED_SERVICE
keywords:
- CM_PROB_DISABLED_SERVICE
ms.date: 04/20/2017
---

# Code 32 - CM_PROB_DISABLED_SERVICE

This Device Manager error message indicates that the driver has been disabled.

## Error Code

32

### Display Message

"A driver (service) for this device has been disabled. An alternate driver may be providing this functionality. (Code 32)"

### Recommended Resolution

The start type for this service is set to Disabled in the registry. If the driver really is required, change the start type.
