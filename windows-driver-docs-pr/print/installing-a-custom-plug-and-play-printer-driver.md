---
title: Installing a Custom Plug and Play Printer Driver
author: windows-driver-content
description: Installing a Custom Plug and Play Printer Driver
ms.assetid: 0269afbe-c7d1-4227-ad77-b921852d6a0c
keywords: ["customizing printer drivers WDK , Plug and Play"]
---

# Installing a Custom Plug and Play Printer Driver


## <a href="" id="ddk-installing-a-custom-plug-and-play-printer-driver-gg"></a>


On Windows XP, the Plug and Play manager loads drivers in this order (listed from highest to lowest preference):

1.  signed IHV drivers

2.  "in-box" drivers

3.  unsigned IHV drivers

On Windows 2000, there is no difference between in-box and signed IHV drivers: either type of driver is loaded in preference to an unsigned IHV driver. To learn more about applications designed to install drivers and INF files that replace "in-box" drivers, see [Writing a Device Installation Application](https://msdn.microsoft.com/library/windows/hardware/ff554015).

If you are developing a driver that replaces a Windows 2000 in-box driver, make sure that the [*hardware IDs*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) in the [**INF Models section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) of your INF file include the appropriate port enumerator. The Windows 2000 version of Ntprint.inf includes port enumerators in its entries in the INF Models section. If the same entries in your INF file omit port enumerators, Plug and Play selects the in-box Windows 2000 driver in preference to yours. If your driver replaces a Windows XP in-box driver, you do not have to include the port enumerator in a hardware ID.

An IHV can avoid a dialog box asking for user interaction in client-side installations by providing two lines in the INF Models section for each model, as in the following example.

```
; Models section

[OEM Company Name]
"XYZ PScript Printer" = OEMXYZ.PPD, LPTENUM\OEM_Company_NameXYZ_F84F, XYZ_PScript_Printer
"XYZ PScript Printer" = OEMXYZ.PPD, OEM_Company_NameXYZ_F84F, XYZ_PScript_Printer
.
.
.
```

In this example, the two lines are nearly identical, differing only by the inclusion of the bus enumerator (LPTENUM) in the hardware ID in the first line. In each line, the second and third entry values are the hardware ID and compatible ID, respectively. For a printer that is installed over a specific bus (the parallel port in this case), the hardware ID in the first line produces a hardware ID match, which is the best possible match. For a printer installed over any other bus, the hardware ID in the second line also produces a hardware ID match.

In either case, Setup does not require a response from the user on whether to install the driver, so does not display a dialog box asking for a response. Note, however, that if the match is not a hardware ID match, but rather a [*compatible ID*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-compatible-id) match, and installation occurs on the client side, Setup displays a dialog box asking for user interaction.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Custom%20Plug%20and%20Play%20Printer%20Driver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


