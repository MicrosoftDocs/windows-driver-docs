---
title: WHQL Release Signature
description: WHQL Release Signature
ms.assetid: edc815d4-596c-4f50-9bff-029b8ea19a0a
keywords: ["driver signing WDK , WHQL digital signatures", "signing drivers WDK , WHQL digital signatures", "digital signatures WDK , WHQL", "signatures WDK , WHQL", "WHQL digital signatures WDK", "public release driver signing WDK , WHQL", "release signing WDK , WHQL"]
---

# WHQL Release Signature


[Driver packages](driver-packages.md) that pass [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893) testing can be digitally-signed by WHQL. If your driver package is digitally-signed by WHQL, it can be distributed through the [Windows Update](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8) program or other Microsoft-supported distribution mechanisms.

Obtaining a WHQL release signature is part of the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893). A WHQL release signature consists of a digitally-signed [catalog file](catalog-files.md). The digital signature does not change the driver binary files or the INF file that you submit for testing.

Obtaining a WHQL release signature consists of the following:

-   Testing the [driver package](driver-packages.md) with the Windows HCK to verify that the driver package is compatible with Microsoft Windows. Once the HCK is installed, the Driver Test Manager (DTM) is run to test and verify the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

-   Submitting DTM test logs to the Windows Quality Online Services to obtain a WHQL release signature for the driver package. For more information, see the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

For more information about WHQL, see the [Windows Hardware Quality Labs](http://go.microsoft.com/fwlink/p/?linkid=8705) website.

**Note**  WHQL does not embed signatures in driver files. If you embed a signature in a driver file, you should use a third-party commercial [release certificate](release-certificates.md). Embed the signature in the driver file before submitting the driver package to WHQL.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20WHQL%20Release%20Signature%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




