---
title: DEFINE\_DEVPROPKEY
description: In Windows Vista and later versions of Windows, the DEFINE\_DEVPROPKEY macro creates a DEVPROPKEY structure that represents a device property key in the unified device property model.
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
---

# DEFINE\_DEVPROPKEY


In Windows Vista and later versions of Windows, the DEFINE\_DEVPROPKEY macro creates a DEVPROPKEY structure that represents a device property key in the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

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

The DEFINE\_DEVPROPKEY structure is part of the [unified device property model](https://msdn.microsoft.com/library/windows/hardware/ff553515).

The DEFINE\_DEVPROPKEY macro can be used to create a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents a custom device property.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEFINE_DEVPROPKEY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





