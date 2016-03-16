---
title: Restricting the Loading Location of UMDF Drivers
description: Restricting the Loading Location of UMDF Drivers
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: eac19fa8-2889-4cc3-9f4b-d11d7d3ed684
keywords: ["locations WDK UMDF", "binaries WDK UMDF", "directories WDK UMDF", "UMDriverCopy", "loading locations WDK UMDF", "INF files WDK UMDF loading locations"]
---

# Restricting the Loading Location of UMDF Drivers


The UMDF platform will fail to load the main UMDF driver binaries from any location other than the %SystemRoot%\\System32\\Drivers\\Umdf directory. Therefore, a UMDF INF file must restrict the location where it installs UMDF drivers to that directory. Installing in this directory also ensures that unprivileged users cannot tamper with the UMDF drivers.

To install UMDF driver binaries to %SystemRoot%\\System32\\Drivers\\Umdf, the UMDF driver INF file must include an [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383) that is similar to the following code example.

```
[DestinationDirs]
UMDriverCopy=12,UMDF ; copies to drivers\umdf
```

"UMDriverCopy" represents an INF-writer-determined name of a section that lists the UMDF driver binaries as shown in the following example.

```
[UMDriverCopy]
WUDFOsrUsbDriver.dll
```

The [**CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) must also reference the **UMDriverCopy** section to indicate the list of UMDF driver binaries for the operating system to copy from the source media to the destination as shown in the following example.

```
[OsrUsb_Install.NT]
CopyFiles=UMDriverCopy
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Restricting%20the%20Loading%20Location%20of%20UMDF%20Drivers%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




