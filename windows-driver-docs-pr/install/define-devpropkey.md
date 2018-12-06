---
title: DEFINE_DEVPROPKEY
description: In Windows Vista and later versions of Windows, the DEFINE_DEVPROPKEY macro creates a DEVPROPKEY structure that represents a device property key in the unified device property model.
ms.assetid: 9723241d-939e-40b4-8f06-83c99b31c02e
keywords: ["DEFINE_DEVPROPKEY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEFINE_DEVPROPKEY
api_location:
- Devpropdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEFINE_DEVPROPKEY


In Windows Vista and later versions of Windows, the DEFINE_DEVPROPKEY macro creates a DEVPROPKEY structure that represents a device property key in the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

``` syntax
#ifdef INITGUID
#define DEFINE_DEVPROPKEY(name, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8, pid) EXTERN_C const DEVPROPKEY DECLSPEC_SELECTANY name = { { l, w1, w2, { b1, b2,  b3,  b4,  b5,  b6,  b7,  b8 } }, pid }
#else
#define DEFINE_DEVPROPKEY(name, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8, pid) EXTERN_C const DEVPROPKEY name
#endif // INITGUID
```

## Members


<a href="" id="name"></a>*name*  
The name of a DEVPROPKEY structure that represents a device property key.

<a href="" id="l"></a>*l*  
An unsigned long-typed variable that supplies the value of the **data1** member of the fmtid member of the DEVPROPKEY structure.

<a href="" id="w1"></a>*w1*  
An unsigned short-type variable that supplies the value of the **data2** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="w2"></a>*w2*  
An unsigned short-type variable that supplies the value of the **data3** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b1"></a>*b1*  
A byte-typed variable that supplies the value of the **data4\[0\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b2"></a>*b2*  
A byte-typed variable that supplies the value of the **data4\[1\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b3"></a>*b3*  
A byte-typed variable that supplies the value of the **data4\[2\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b4"></a>*b4*  
A byte-typed variable that supplies the value of the **data4\[3\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b5"></a>*b5*  
A byte-typed variable that supplies the value of the **data4\[4\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b6"></a>*b6*  
A byte-typed variable that supplies the value of the **data4\[5\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b7"></a>*b7*  
A byte-typed variable that supplies the value of the **data4\[6\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="b8"></a>*b8*  
A byte-typed variable that supplies the value of the **data4\[7\]** member of the **fmtid** member of the DEVPROPKEY structure.

<a href="" id="pid"></a>*pid*  
A DEVPROPID-typed variable that supplies the value of the **pid** (property identifier) member of the DEVPROPKEY structure. The property identifier must be greater than or equal to two.

Remarks
-------

The DEFINE_DEVPROPKEY structure is part of the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

The DEFINE_DEVPROPKEY macro can be used to create a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents a custom device property.

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


[**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)

 

 






