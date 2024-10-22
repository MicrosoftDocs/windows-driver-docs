---
title: XPS Rasterization on the GPU
description: Windows Display Driver Model (WDDM) 1.2 and later drivers must be able to pass XPS rasterization display conformance tests in order to ensure high-quality Windows printing.
keywords:
- Windows Display Driver Model (WDDM) , XPS rasterization, debugging
ms.date: 10/21/2024
---

# XPS rasterization on the GPU

XML Paper Specification (XPS) rasterization on the GPU doesn't require any independent hardware vendor (IHV) code or behavioral changes in drivers. However, XPS rasterization is a usage pattern that can potentially expose bugs or improper assumptions in driver code. Windows Display Driver Model (WDDM) 1.2 and later drivers must be able to pass XPS rasterization display conformance tests in order to ensure high-quality Windows printing.

* Minimum WDDM version: 1.2

* Minimum Windows version: 8

* Driver implementation—Full graphics and Display only: Mandatory

* [WHLK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests: **Device.Graphics¦XPSRasterizationConformance**

## XPS rasterization conformance

The XPS rasterization display conformance requirement determines whether a WDDM GPU driver produces correct rasterization results when it's used by Direct2D in the context of the XPS rasterizer.

The XPS rasterizer is a system component used heavily by Windows print drivers to rasterize an XPS Print Descriptor Language (PDL). To determine the correctness of rasterization results, a comparison is performed between:

* The results that are obtained from the XPS rasterizer when executed on a system with the subject WDDM GPU driver.
* The results obtained from baseline use of the XPS rasterizer.
