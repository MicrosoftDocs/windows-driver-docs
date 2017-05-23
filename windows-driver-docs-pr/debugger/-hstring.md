---
title: hstring
description: The hstring extension displays the fields of an HSTRING. The last item in the display is the string itself.
ms.assetid: 6FB85609-0FB1-457E-A58E-804F69016406
keywords: ["hstring Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- hstring
api_type:
- NA
---

# !hstring


The **!hstring** extension displays the fields of an **HSTRING**. The last item in the display is the string itself.

``` syntax
!hstring Address
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>*Address*  
The address of an **HSTRING**.

Remarks
-------

The **HSTRING** data type supports strings that have embedded NULL characters. However, the **!hstring** extension displays the string only up to the first NULL character. To see the entire string including the embedded NULL characters, use the [**!hstring2**](-hstring2.md) extension.

## <span id="see_also"></span>See also


[Windows Runtime Debugger Commands](windows-runtime-debugger-commands.md)

[**!hstring2**](-hstring2.md)

[**!winrterr**](-winrterr.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!hstring%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





