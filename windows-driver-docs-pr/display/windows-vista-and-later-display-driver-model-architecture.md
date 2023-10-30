---
title: WDDM Architecture
description: Windows Display Driver Model (WDDM) Architecture
keywords:
- display driver model WDK Windows Vista , architecture
- Windows Vista display driver model WDK , architecture
- architecture WDK display
- user-mode display drivers WDK Windows Vista , architecture
ms.date: 03/20/2023
---

# WDDM Architecture

The WDDM display driver model architecture is composed of user-mode and kernel-mode parts. The following figure shows the architecture required to support WDDM.

:::image type="content" source="images/dx10arch.png" alt-text="Diagram showing the WDDM architecture with user-mode and kernel-mode parts.":::

A graphics hardware vendor must supply a user-mode display driver and display miniport driver (also known as a kernel-mode display driver or KMD).

* The user-mode display driver is a dynamic-link library (DLL) that the Direct3D runtime loads.

* The display miniport driver communicates with the DirectX graphics kernel subsystem.

For more information about the user-mode display driver and display miniport driver, see the [Windows Display Driver Model (WDDM) Reference](/windows-hardware/drivers/ddi/_display/).
