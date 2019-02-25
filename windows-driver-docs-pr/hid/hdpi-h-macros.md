---
title: 'Hdpi.h Macros'
description: 'Macros contained in the Hdpi.h header.'
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Hdpi.h Macros

The Hdpi.h header file contains several macros. 
This topic documents the following macros:

* [**HidP\_GetButtons**](#HidPGetButtons)
* [**HidP\_GetButtonsEx**](#HidPGetButtonsEx)
* [**HidP\_SetButtons**](#HidPSetButtons)
* [**HidP\_UnsetButtons**](#HidPUnsetButtons)


##  HidP\_GetButtons


The **HidP\_GetButtons** macro is a mnemonic alias for the [**HidP\_GetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539742) routine.

```cpp
#define HidP_GetButtons(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe) \
        HidP_GetUsages(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe)
```

##  HidP\_GetButtonsEx


The **HidP\_GetButtonsEx** macro is an mnemonic alias for the [**HidP\_GetUsagesEx**](https://msdn.microsoft.com/library/windows/hardware/ff539745) routine.

```cpp
#define HidP_GetButtonsEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)  \
         HidP_GetUsagesEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)
```


##  HidP\_SetButtons


The **HidP\_SetButtons** macro is a mnemonic alias for the [**HidP\_SetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539792) routine.

```cpp
#define HidP_SetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_SetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
```

##  HidP\_UnsetButtons


The **HidP\_UnsetButtons** macro is a mnemonic alias for the [**HidP\_UnsetUsages**](https://msdn.microsoft.com/library/windows/hardware/ff539819) routine.

```cpp
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






