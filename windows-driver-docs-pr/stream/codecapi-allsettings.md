---
title: CODECAPI_ALLSETTINGS
description: The CODECAPI_ALLSETTINGS property is used to pass back and forth a minidriver-generated block of data.
ms.date: 10/08/2021
---

# CODECAPI_ALLSETTINGS

The CODECAPI_ALLSETTINGS property is used to pass back and forth a minidriver-generated block of data.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSPROPERTY | PVOID |

The property value (operation data) is of type PVOID, which is a pointer to a user-mode buffer for the minidriver-generated block of data.

## Comments

On a property get call:

If an application makes a property get call with a zero length buffer, the minidriver must return STATUS_BUFFER_OVERFLOW and specify the required buffer size in the **Irp->IoStatus.Information** field. If the length buffer is nonzero, the minidriver must return STATUS_BUFFER_TOO_SMALL if the supplied buffer is too small for the data block, otherwise the minidriver packs its settings into a data block that can be restored later.

It is the minidriver's responsibility to add data integrity checks to the data, such as a unique GUID to indicate the minidriver generated the data, a cyclic redundancy check (CRC), and a header length.

The data returned should be lightweight and contain only information required to reconstruct the current settings.

Applications will use this property for multilevel undos, stored with their projects, and so on.

On a property set call:

The minidriver must verify the data's integrity and check that the data block size is under the maximum data size (for example, reject anything over a certain size). It must also verify the CRC and the header length. The minidriver must also cache any changes to be propagated for [CODECAPI_CURRENTCHANGELIST](codecapi-currentchangelist.md).

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[CODECAPI_CURRENTCHANGELIST](codecapi-currentchangelist.md)
