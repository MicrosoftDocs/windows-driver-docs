---
title: Multipage Scanning and TWAIN
description: Multipage Scanning and TWAIN
ms.date: 04/20/2017
---

# Multipage Scanning and TWAIN





Starting with Windows XP, the TWAIN compatibility layer supports multipage scanning from scroll-fed devices, provided that all scanned pages are of the same length. The reason for this is that TWAIN obtains information from the calling application about page length only on the first page. TWAIN does not require the calling application to ask for image information between pages. Furthermore, TWAIN applies the information it receives from the application about the first page to all succeeding pages.

 

 




