---
title: Implementation requirements for various form factors
description: This topic describes implementation requirements for various form factors.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Implementation requirements for various form factors

This topic describes implementation requirements for various form factors.

|Form factor|Form factor name|Definition|GPIO indicator implementation requirements|
|----|----|----|----|
|![slate form factor.](images/slate.jpg)|Slate|Tablet form factor with no attachable keyboard|When a stationary docking accessory is available, the docking indicator must be implemented.|
|![Laptop form factor.](images/laptop.jpg)|Laptop|Permanently attached keyboard that is always available for typing.|Statically set the mode to laptop.|
|![convertible form factor.](images/convertible.jpg)|Convertible|System that can be used as either a slate or a tablet. The keyboard can be detached, flipped, or swivelled.|Implement the laptop/slate indicator.</br>If a stationary docking accessory is available, the docking indicator must also be implemented.|
|![all-in-one form factor.](images/allinone.jpg)|All-in-One|Medium size desktop/semi-portable systems that have a keyboard that is attached as an accessory.|No implementation required because the keyboard is an optional accessory.|
