---
title: DEVPROPKEY structure
description: In Windows Vista and later versions of Windows, the DEVPROPKEY structure represents a device property key for a device property in the unified device property model.
keywords: ["DEVPROPKEY structure Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROPKEY
api_location:
- devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPROPKEY structure


In Windows Vista and later versions of Windows, the DEVPROPKEY structure represents a device property key for a device property in the [unified device property model](./unified-device-property-model--windows-vista-and-later-.md).

## Syntax

```ManagedCPlusPlus
struct DEVPROPKEY {
  DEVPROPGUID fmtid;
  DEVPROPID   pid;
};
```

## Members

**fmtid**  
A DEVPROPGUID-typed value that specifies a property category.

The DEVPROPGUID data type is defined as:

```cpp
typedef GUID  DEVPROPGUID, *PDEVPROPGUID;
```

**pid**  
A DEVPROPID-typed value that uniquely identifies the property within the property category. For internal system reasons, a property identifier must be greater than or equal to two.

The DEVPROPID data type is defined as:

```cpp
typedef ULONG DEVPROPID, *PDEVPROPID;
```

## Remarks

The DEVPROPKEY structure is part of the [unified device property model](./unified-device-property-model--windows-vista-and-later-.md).

The basic set of system-supplied device property keys are defined in *Devpkey.h*.

The [**DEFINE\_DEVPROPKEY**](./define-devpropkey.md) macro creates an instance of a DEVPROPKEY structure that represents a device property key.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Devpropdef.h (include Devpropdef.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEFINE\_DEVPROPKEY**](./define-devpropkey.md)

 

