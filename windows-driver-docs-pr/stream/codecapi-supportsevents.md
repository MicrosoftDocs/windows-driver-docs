---
title: CODECAPI_SUPPORTSEVENTS
description: The CODECAPI_SUPPORTSEVENTS property is used to indicate whether the minidriver supports user-mode events.
ms.date: 10/08/2021
---

# CODECAPI_SUPPORTSEVENTS

The CODECAPI_SUPPORTSEVENTS property is used to indicate whether the minidriver supports user-mode events. That is, the minidriver implements the [CODECAPI_CHANGELISTS](codecapi-changelists.md) event.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSPROPERTY | BOOL |

The property value (operation data) is of type BOOL, which specifies whether the minidriver supports user-mode events. A value of **TRUE** indicates the minidriver provides support. The minidriver should not support this GUID if it does not support the event mechanism.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

### See also

[**KSPROPERTY**](ksproperty-structure.md)
