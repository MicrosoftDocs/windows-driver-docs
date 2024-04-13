---
title: CODECAPI_CURRENTCHANGELIST
description: The CODECAPI_CURRENTCHANGELIST property is used to indicate which parameters changed.
ms.date: 10/08/2021
---

# CODECAPI_CURRENTCHANGELIST

The CODECAPI_CURRENTCHANGELIST property is used to indicate which parameters changed in a previous property "set" call, such as [CODECAPI_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI_SETALLDEFAULTS](codecapi-setalldefaults.md).

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSPROPERTY | Array of GUIDs |

The property value (operation data) is an array of GUIDs.

## Comments

On a property get call:

- If an application makes a property get call with a nonzero buffer size, the minidriver returns STATUS_BUFFER_TOO_SMALL if the supplied buffer is too small for the data block. If there are no items to return, the minidrivers returns STATUS_SUCCESS. Otherwise a list of GUIDs is returned (that is, where the sizeof(GUID) bytes equals 16 bytes). The returned size is the length of the list in bytes (that is, the number of GUIDS \* sizeof(GUID)).

On a property set call:

- The current list of changed GUIDs is reset.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[CODECAPI_ALLSETTINGS](codecapi-allsettings.md)

[CODECAPI_SETALLDEFAULTS](codecapi-setalldefaults.md)
