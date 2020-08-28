---
title: 'Hdpi.h Macros'
description: 'Macros contained in the Hdpi.h header.'
ms.localizationpriority: medium
ms.date: 02/25/2020
---

# Hdpi.h Macros

The [Hdpi.h](/windows-hardware/drivers/ddi/hidpi/) header file contains the following macros:

- [HidP\_GetButtons](#hidp_getbuttons)
- [HidP\_GetButtonsEx](#hidp_getbuttonsex)
- [HidP\_SetButtons](#hidp_setbuttons)
- [HidP\_UnsetButtons](#hidp_unsetbuttons)

## HidP\_GetButtons

The **HidP\_GetButtons** macro is a mnemonic alias for the [**HidP\_GetUsages**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages) routine.

```cpp
#define HidP_GetButtons(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe) \
        HidP_GetUsages(Rty, UPa, LCo, ULi, ULe, Ppd, Rep, RLe)
```

## HidP\_GetButtonsEx

The **HidP\_GetButtonsEx** macro is an mnemonic alias for the [**HidP\_GetUsagesEx**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex) routine.

```cpp
#define HidP_GetButtonsEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)  \
         HidP_GetUsagesEx(Rty, LCo, BLi, ULe, Ppd, Rep, RLe)
```

## HidP\_SetButtons

The **HidP\_SetButtons** macro is a mnemonic alias for the [**HidP\_SetUsages**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages) routine.

```cpp
#define HidP_SetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_SetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
```

## HidP\_UnsetButtons

The **HidP\_UnsetButtons** macro is a mnemonic alias for the [**HidP\_UnsetUsages**](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages) routine.

```cpp
#define HidP_UnsetButtons(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle) \
        HidP_UnsetUsages(Rty, Up, Lco, ULi, ULe, Ppd, Rep, Rle)
```

### Requirements

**Header**: [hidpi.h](/windows-hardware/drivers/ddi/hidpi/) (include Hidpi.h)


## See also

[hidpi.h](/windows-hardware/drivers/ddi/hidpi/)

[HidP\_GetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusages)

[HidP\_GetUsagesEx](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_getusagesex)

[HidP\_SetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_setusages)

[HidP\_UnsetUsages](/windows-hardware/drivers/ddi/hidpi/nf-hidpi-hidp_unsetusages)