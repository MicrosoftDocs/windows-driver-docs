---
title: Providing Support for Asian Layout
author: windows-driver-content
description: Providing Support for Asian Layout
ms.assetid: 38c7dfca-ce30-4967-84a4-e2f40bba8c57
keywords:
- print processors WDK , Asian languages
- Asian languages WDK print
- booklets WDK print
- N-up printing WDK
- reverse orientation WDK print
- Arabic print support WDK
- Japanese print support WDK
- Urdu print support WDK
- international considerations WDK
- printing Asian languages WDK
- languages WDK print
- right to left reading languages WDk print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing Support for Asian Layout


The Microsoft Windows print processor supports Asian languages that read from right to left, such as Arabic, Japanese, and Urdu, with the following features:

-   **N-Up Direction**: When printing multiple pages on a single sheet, users can print the pages in a right-to-left order on the sheet.

-   **Booklet Edge**: When printing a booklet, in which sheets are folded and pages are laid out side-by-side, users can order the booklet pages from right to left. The following diagram shows the page layout for a booklet by using the BOOKLET\_EDGE\_RIGHT flag.![diagram illustrating the page layout for a booklet by using the booklet\-edge\-right flag](images/asian-booklet.png)

The flags that enable you to change the N-up direction and booklet edge in a driver to support an Asian layout are available in Windows Vista. For details about how to set these values, see [**DrvQueryJobAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff548581) and [**ATTRIBUTE\_INFO\_4**](https://msdn.microsoft.com/library/windows/hardware/ff545096).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Providing%20Support%20for%20Asian%20Layout%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


