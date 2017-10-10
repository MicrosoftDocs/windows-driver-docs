---
title: DEVPROPKEY structure
description: In Windows Vista and later versions of Windows, the DEVPROPKEY structure represents a device property key for a device property in the unified device property model.
ms.assetid: 98986d43-84c0-44e6-83f9-08e872ea5e6d
keywords: ["DEVPROPKEY structure Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPROPKEY
api_location:
- devpropdef.h
api_type:
- HeaderDef
---

# DEVPROPKEY structure


In Windows Vista and later versions of Windows, the DEVPROPKEY structure represents a device property key for a device property in the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

Syntax
------

```ManagedCPlusPlus
struct DEVPROPKEY {
  DEVPROPGUID fmtid;
  DEVPROPID   pid;
};
```

Members
-------

**fmtid**  
A DEVPROPGUID-typed value that specifies a property category.

The DEVPROPGUID data type is defined as:

```
typedef GUID  DEVPROPGUID, *PDEVPROPGUID;
```

**pid**  
A DEVPROPID-typed value that uniquely identifies the property within the property category. For internal system reasons, a property identifier must be greater than or equal to two.

The DEVPROPID data type is defined as:

```
typedef ULONG DEVPROPID, *PDEVPROPID;
```

Remarks
-------

The DEVPROPKEY structure is part of the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

The basic set of system-supplied device property keys are defined in *Devpkey.h*.

The [**DEFINE\_DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff541072) macro creates an instance of a DEVPROPKEY structure that represents a device property key.

Requirements
------------

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


[**DEFINE\_DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff541072)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPROPKEY%20structure%20%20RELEASE:%20%2810/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





