---
title: CODECAPI_SETALLDEFAULTS
description: The CODECAPI_SETALLDEFAULTS property is used to reset all the internal settings of the minidriver to their default configurations.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# CODECAPI_SETALLDEFAULTS

The CODECAPI_SETALLDEFAULTS property is used to reset all the internal settings of the minidriver to their default configurations.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Filter | KSPROPERTY | N/A |

A set to this property set is a trigger that the device should reset all of its settings to their defaults.

## Comments

The minidriver should cache its entire list of changed parameters for [CODECAPI_CURRENTCHANGELIST](codecapi-currentchangelist.md) when this property is set.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)
