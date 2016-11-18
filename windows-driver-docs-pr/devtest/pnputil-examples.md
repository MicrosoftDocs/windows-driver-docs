---
title: PnPUtil Examples
description: PnPUtil Examples
ms.assetid: 4805edb9-e4f8-441d-a7f4-0c962ddeae4e
---

# PnPUtil Examples


This topic provides the following examples on how to use the PnPUtil tool:

-   [Adding a driver package to the driver store](#adding-a-driver-package-to-the-driver-store)

-   [Listing the driver packages within the driver store](#listing-the-driver-packages-within-the-driver-store)

-   [Deleting a driver package from the driver store](#deleting-a-driver-package-from-the-driver-store)

### <span id="adding_a_driver_package_to_the_driver_store"></span><span id="ADDING_A_DRIVER_PACKAGE_TO_THE_DRIVER_STORE"></span> Adding a driver package to the driver store

The following example adds a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), which contains the [INF](https://msdn.microsoft.com/library/windows/hardware/ff547402) file that is named MyDriver.inf, to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868):

```
C:\>pnputil /a m:\MyDriver.inf
Microsoft PnP Utility

Processing inf : MyDriver.inf
Driver package added successfully.
Published name : oem22.inf
```

As soon as it is added to the driver store, the INF file for the driver package is referenced within the store through its published named (oem22.inf).

### <span id="listing_the_driver_packages_within_the_driver_store"></span><span id="LISTING_THE_DRIVER_PACKAGES_WITHIN_THE_DRIVER_STORE"></span> Listing the driver packages within the driver store

The following example lists the [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) that are currently in the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). Only driver packages that are not in-box packages are listed. An *in-box* driver package is one which is included in the default installation of Windows or its service packs:

```
C:\>pnputil /e
Microsoft PnP Utility

Published name : oem0.inf
Driver package provider : Microsoft
Class : Printers
Driver version and date : Unknown driver version and date
Signer name : microsoft windows

Published name : oem22.inf
Driver package provider : Fabrikam, Inc.
Class : Network adapters
Driver version and date : 10/07/2009 1.0.200.0
Signer name : microsoft windows hardware compatibility publisher
```

In this example, information is displayed about the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) that is referenced by the published INF file (oem22.inf). This information includes the publisher (Fabrikam, Inc.), setup class (Network adapter) and version (1.0.200.0) of the driver package.

**Note**   In this example, the data for the "Signer Name" field indicates that the sample driver package was digitally signed by a [Windows Hardware Quality Labs (WHQL) release signature](https://msdn.microsoft.com/library/windows/hardware/ff553976). If the driver package was not digitally signed, there would be no data displayed in the "Signer Name" field.

 

### <span id="deleting_a_driver_package_from_the_driver_store"></span><span id="DELETING_A_DRIVER_PACKAGE_FROM_THE_DRIVER_STORE"></span> Deleting a driver package from the driver store

The following example removes the [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) from the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868). The driver package is referenced by its published INF file (oem22.inf):

```
C:\>pnputil /d oem22.inf
Microsoft PnP Utility

Driver package deleted successfully.
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PnPUtil%20Examples%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




