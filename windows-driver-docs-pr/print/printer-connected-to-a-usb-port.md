---
title: Printer Connected to a USB Port
author: windows-driver-content
description: Printer Connected to a USB Port
ms.assetid: 85e238e1-4dc1-4720-b383-d6aaed72e560
keywords:
- USB printers WDK
- bus-type printer driver WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer Connected to a USB Port


## <a href="" id="ddk-printer-connected-to-a-usb-port-gg"></a>


When a Universal Serial Bus (USB) printer is connected over a USB port, the USB bus driver creates a physical device object (PDO) with a [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) of the form VIDvvPIDpp, and [*compatible ID*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-compatible-id) Class\_7. The [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) for this is created under Enum\\USB\\ ...Class\_7 and identifies a printer device connected over a USB port. Plug and Play loads usbprint.sys using a compatible ID match on Class\_7 from usbprint.inf.

The entry from usbprint.inf that is used to load usbprint.sys for any USB printer device is:

```
[Microsoft]
%USBPRINT.DeviceDesc% = USBPRINT_Inst,USB\Class_07,GENERIC_USB_PRINTER
```

Usbprint.sys queries the Plug and Play printer to get the 1284 string, and generates a hardware ID that is compatible with the parallel bus enumerator. (For more information, see [USBPRINT Interface](usb-printing.md).) It creates a physical device object (PDO) whose devnode is under Enum\\USBPRINT, and with two hardware IDs in the following form:

```
USBPRINT\Company_NameModelNam1234
```

The following figure shows the driver stack for a printer connected over a USB port.

![plug and play for usb printers](images/pnpusb01.png)

The following example shows the entries in an [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) that can be used to install a USB or other bus-type printer driver. The first line guarantees a rank-0 hardware ID match if the printer is installed on a USB bus. The second line guarantees a rank-0 hardware ID match if the printer is installed on another bus. For more information, see [Installing a Custom Plug and Play Printer Driver](installing-a-custom-plug-and-play-printer-driver.md).

```
 "Model Name XYZ" = Install_Section_XYZ, USBPRINT\Company_NameModelNam1234, Company_NameModelNam1234 ; plus any other compatible IDs  
"Model Name XYZ" = Install_Section_XYZ, Company_NameModelNam1234, Company_NameModelNam1234 ; plus any other compatible IDs
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Connected%20to%20a%20USB%20Port%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


