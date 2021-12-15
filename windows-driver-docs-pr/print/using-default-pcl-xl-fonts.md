---
title: Using Default PCL XL Fonts
description: Using Default PCL XL Fonts
keywords:
- PCL XL vector graphics WDK Unidrv , default fonts
- default PCL XL fonts
- fonts WDK PCL XL
ms.date: 04/20/2017
---

# Using Default PCL XL Fonts





If you want to include the standard PCL XL fonts, you should include the standard resource DLL, *pclxl.dll*, that is part of the cab file. The following line, which should appear in the GPD, uses the \*ResourceDLL attribute to specify the resource DLL to be used.

```cpp
*ResourceDLL: "pclxl.dll"
```

The default PCL XL fonts that Unidrv supports are listed in the following table:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Font Name</th>
<th>Font File</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>"Albertus Medium"</p></td>
<td><p>ALBERTR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Albertus Extra Bold"</p></td>
<td><p>ALBERTX.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Antique Olive"</p></td>
<td><p>AOLIVEB.UFM</p>
<p>AOLIVEI.UFM</p>
<p>AOLIVER.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Arial"</p></td>
<td><p>ARIALB.UFM</p>
<p>ARIALI.UFM</p>
<p>ARIALJ.UFM</p>
<p>ARIALR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"ITC Benguiat"</p></td>
<td><p>BENGUATB.UFM</p>
<p>BBENGUATJ.UFM</p>
<p>BENGUATJ.UFM</p>
<p>BENGUATR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"ITC Bookman Demi"</p></td>
<td><p>BOOKMANB.UFM</p>
<p>BOOKMANJ.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"ITC Bookman Light"</p></td>
<td><p>BOOKMANI.UFM</p>
<p>BOOKMANR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Brougham"</p></td>
<td><p>BROGHAMB.UFM</p>
<p>BROGHAMI.UFM</p>
<p>BROGHAMJ.UFM</p>
<p>BROGHAMR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"CG Omega"</p></td>
<td><p>CGOMEGAB.UFM</p>
<p>CGOMEGAI.UFM</p>
<p>CGOMEGAJ.UFM</p>
<p>CGOMEGAR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"CG Times"</p></td>
<td><p>CGTIMESB.UFM</p>
<p>CGTIMESI.UFM</p>
<p>CGTIMESJ.UFM</p>
<p>CGTIMESR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Clarendon Condensed"</p></td>
<td><p>CLARCD.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Coronet"</p></td>
<td><p>CORONETR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Courier"</p></td>
<td><p>COURIERB.UFM</p>
<p>COURIERI.UFM</p>
<p>COURIERJ.UFM</p>
<p>COURIERR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Garamond"</p></td>
<td><p>GARMONDB.UFM</p>
<p>GARMONDI.UFM</p>
<p>GARMONDJ.UFM</p>
<p>GARMONDR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Letter Gothic"</p></td>
<td><p>LETGOTHB.UFM</p>
<p>LETGOTHI.UFM</p>
<p>LETGOTHR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Marigold"</p></td>
<td><p>MARGOLDR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Times New Roman"</p></td>
<td><p>TIMESNRB.UFM</p>
<p>TIMESNRI.UFM</p>
<p>TIMESNRJ.UFM</p>
<p>TIMESNRR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Univers Condensed"</p></td>
<td><p>UNIVERCB.UFM</p>
<p>UNIVERCI.UFM</p>
<p>UNIVERCJ.UFM</p>
<p>UNIVERCR.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Univers"</p></td>
<td><p>Universa.UFM</p>
<p>UNIVERSB.UFM</p>
<p>Universc.UFM</p>
<p>Universd.UFM</p>
<p>Universe.UFM</p>
<p>UNIVERSI.UFM</p>
<p>UNIVERSJ.UFM</p>
<p>UNIVERSR.UFM</p>
<p>UNIVERSR.UFM</p></td>
</tr>
<tr class="even">
<td><p>"W Dingbats"</p></td>
<td><p>WDINGBAT.UFM</p></td>
</tr>
<tr class="odd">
<td><p>"Wingdings"</p></td>
<td><p>WINGDING.UFM</p></td>
</tr>
<tr class="even">
<td><p>"Symbol"</p></td>
<td><p>SYMBOL.UFM</p></td>
</tr>
</tbody>
</table>

 

 

 




