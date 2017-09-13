---
title: 'Hdpi.h Macros'
author: windows-driver-content
description: 'Macros contained in the Hdpi.h header.'
---

# Hdpi.h Macros

The Hdpi.h header file contains several macros. 
This topic documents the following macros:

* [**HidP\_GetButtons**](#HidPGetButtons)
* [**HidP\_GetButtonsEx**](#HidPGetButtonsEx)
* [**HidP\_SetButtons**](#HidPSetButtons)
* [**HidP\_UnsetButtons**](#HidPUnsetButtons)


## <a href="" id="HidPGetButtons"></a> HidP\_GetButtons


The **HidP\_GetButtons** macro is a mnemonic alias for the [**HidP\_GetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539742) routine.

```
#define HidP_GetButtons(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe) \
        HidP_GetUsages(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe)
```

## <a href="" id="HidPGetButtonsEx"></a> HidP\_GetButtonsEx


The **HidP\_GetButtonsEx** macro is an mnemonic alias for the [**HidP\_GetUsagesEx**](https://msdn.microsoft.com/library/windows/hardware/ff539745) routine.

```
#define HidP_GetButtonsEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)  \
         HidP_GetUsagesEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)
```


## <a href="" id="HidPSetButtons"></a> HidP\_SetButtons


The **HidP\_SetButtons** macro is a mnemonic alias for the [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792) routine.

```
#define HidP_SetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_SetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
```

## <a href="" id="HidPUnsetButtons"></a> HidP\_UnsetButtons


The **HidP\_UnsetButtons** macro is a mnemonic alias for the [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819) routine.

```
#define HidP_UnsetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_UnsetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Hidpi.h (include Hidpi.h)</td>
</tr>
</tbody>
</table>

## See also

[**HidP\_GetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539742)

[**HidP\_GetUsagesEx**](https://msdn.microsoft.com/library/windows/hardware/ff539745)

[**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792)

[**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819)


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Hdpi_Macros%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




