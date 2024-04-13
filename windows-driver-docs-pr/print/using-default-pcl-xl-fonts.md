---
title: Using Default PCL XL Fonts
description: Using Default PCL XL Fonts
keywords:
- PCL XL vector graphics WDK Unidrv , default fonts
- default PCL XL fonts
- fonts WDK PCL XL
ms.date: 02/06/2024
---

# Using Default PCL XL Fonts

[!include[Print Support Apps](../includes/print-support-apps.md)]

If you want to include the standard PCL XL fonts, you should include the standard resource DLL, *pclxl.dll*, that is part of the cab file. The following line, which should appear in the GPD, uses the \*ResourceDLL attribute to specify the resource DLL to be used.

```GPD
*ResourceDLL: "pclxl.dll"
```

The default PCL XL fonts that Unidrv supports are listed in the following table:

| Font name | Font file |
|--|--|
| "Albertus Medium" | ALBERTR.UFM |
| "Albertus Extra Bold" | ALBERTX.UFM |
| "Antique Olive" | AOLIVEB.UFM<br>AOLIVEI.UFM<br>AOLIVER.UFM |
| "Arial" | ARIALB.UFM<br>ARIALI.UFM<br>ARIALJ.UFM<br>ARIALR.UFM |
| "ITC Benguiat" | BENGUATB.UFM<br>BBENGUATJ.UFM<br>BENGUATJ.UFM<br>BENGUATR.UFM |
| "ITC Bookman Demi" | BOOKMANB.UFM<br>BOOKMANJ.UFM |
| "ITC Bookman Light" | BOOKMANI.UFM<br>BOOKMANR.UFM |
| "Brougham" | BROGHAMB.UFM<br>BROGHAMI.UFM<br>BROGHAMJ.UFM<br>BROGHAMR.UFM |
| "CG Omega" | CGOMEGAB.UFM<br>CGOMEGAI.UFM<br>CGOMEGAJ.UFM<br>CGOMEGAR.UFM |
| "CG Times" | CGTIMESB.UFM<br>CGTIMESI.UFM<br>CGTIMESJ.UFM<br>CGTIMESR.UFM |
| "Clarendon Condensed" | CLARCD.UFM |
| "Coronet" | CORONETR.UFM |
| "Courier" | COURIERB.UFM<br>COURIERI.UFM<br>COURIERJ.UFM<br>COURIERR.UFM |
| "Garamond" | GARMONDB.UFM<br>GARMONDI.UFM<br>GARMONDJ.UFM<br>GARMONDR.UFM |
| "Letter Gothic" | LETGOTHB.UFM<br>LETGOTHI.UFM<br>LETGOTHR.UFM |
| "Marigold" | MARGOLDR.UFM |
| "Times New Roman" | TIMESNRB.UFM<br>TIMESNRI.UFM<br>TIMESNRJ.UFM<br>TIMESNRR.UFM |
| "Univers Condensed" | UNIVERCB.UFM<br>UNIVERCI.UFM<br>UNIVERCJ.UFM<br>UNIVERCR.UFM |
| "Univers" | Universa.UFM<br>UNIVERSB.UFM<br>Universc.UFM<br>Universd.UFM<br>Universe.UFM<br>UNIVERSI.UFM<br>UNIVERSJ.UFM<br>UNIVERSR.UFM<br>UNIVERSR.UFM |
| "W Dingbats" | WDINGBAT.UFM |
| "Wingdings" | WINGDING.UFM |
| "Symbol" | SYMBOL.UFM |
